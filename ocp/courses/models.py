# -*- coding: utf-8 -*-
from django.conf import settings
from django.utils import timezone
from ocp.core.mail import send_mail_template
from django.db.models.signals import post_save
from django.db import models
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
from autoslug import AutoSlugField
from django.urls import reverse
from decouple import config


class Category(models.Model):
    name = models.CharField(_('Name'), max_length=128, unique=True)
    description = models.CharField(_('Description'), max_length=256, blank=True)
    slug = AutoSlugField(_('Slug'), populate_from='name', unique=True)
    status = models.BooleanField(_('Status'), default=True)
    created_at = models.DateTimeField(_('Create at'), null=True, auto_now_add=True)
    updated_at = models.DateTimeField(_('Update at'), null=True, auto_now=True)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ['name']

    def __str__(self):
        return self.name


# Set task to delete image more later.
@receiver(post_save, sender=Category)
def category_post_create_handler(sender, **kwargs):
    USE_POPULATE = config('USE_POPULATE', default=False, cast=bool)
    if not USE_POPULATE:
        from .tasks import category_delete_set_task
        category_delete_set_task.apply_async(([1]))


class CourseManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(
            # __icontains é um field-lookups da queryset para indicar maior ou igual a hoje
            # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#field-lookups
            models.Q(name__icontains=query) | \
            models.Q(description__icontains=query)
        )


class Course(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_of_course')
    name = models.CharField(_('Name'), max_length=100, unique=True)
    slug = AutoSlugField(_('Slug'), populate_from='name', unique=True)
    description = models.TextField(_('Description'), blank=True)
    about = models.TextField(_('About'), blank=True)
    phone = models.CharField(max_length=15, blank=True)
    url = models.URLField(help_text="Example: '/about/contact/'. Make sure to have leading and trailing slashes.")
    start_date = models.DateField(
        _('Start Date'), null=True, blank=True)
    image = models.ImageField(
        upload_to='courses/images', verbose_name=_('Image'),
        default='courses/images/None/no-img.jpg',
        null=True, blank=True)
    # somente na criação do registro esta data é salva com a data atual.
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    # toda vez que altera este registro esta data é atualizada com a data atual.
    updated_at = models.DateTimeField(_('Updated at'), auto_now=True)
    hascertification = models.BooleanField(_('Has Certification'), default=False)
    status = models.BooleanField(_('Status'), default=True)
    views = models.IntegerField(_('Views'), default=0)
    qualification = models.IntegerField(_('Qualification'), default=0)

    objects = CourseManager()

    class Meta:
        verbose_name = _('Course')
        verbose_name_plural = _('Courses')
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('courses:course_details', kwargs={'slug': self.slug})

    def release_lessons(self):
        # Evite usar o datetime pois ele usa a data do micro que pode estar em qualquer timezone
        # from datetime import datetime
        # datetime.now()
        # /Importante para datas usar o time zone que é uma data com referencia internacional
        today = timezone.now().date()
        # O release_date é uma data, não é um datetime
        # _gte é um field-lookups da queryset para indicar maior ou igual a hoje
        # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#field-lookups
        return self.lessons.filter(release_date__gte=today)


# Set task to delete image more later.
@receiver(post_save, sender=Course)
def course_post_create_handler(sender, **kwargs):
    USE_POPULATE = config('USE_POPULATE', default=False, cast=bool)
    if not USE_POPULATE: 
        from .tasks import course_delete_set_task
        course_delete_set_task.apply_async(([1]))


class Teacher(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, verbose_name=_('User'),
        on_delete=models.CASCADE, related_name='teach'
    )
    course = models.ManyToManyField(Course, blank=True, related_name="teachers")

    class Meta:
        verbose_name = _('Teacher')
        verbose_name_plural = _('Teachers')
        ordering = ['user']

    def __str__(self):
        return str(self.user)


class Lesson(models.Model):
    name = models.CharField(_('Name'), max_length=100, unique=True)
    description = models.TextField(_('Description'), blank=True)
    number = models.IntegerField(_('Number'), blank=True, default=0)
    release_date = models.DateField(_('Releasing Date'), blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=_('Course'), related_name='lessons')
    created_at = models.DateTimeField(_('Create at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Update at'), auto_now=True)

    class Meta:
        verbose_name = _('Lesson')
        verbose_name_plural = _('Lessons')
        ordering = ['number']

    def __str__(self):
        return 'Lesson: {0} '.format(self.name)

    def is_available(self):
        if self.release_date:
            today = timezone.now().date()
            # O release_date é uma data, não é um datetime
            return self.release_date >= today
        return False


# Material: videos, pdfs, flash...
class Material(models.Model):
    name = models.CharField(_('name'), max_length=100, unique=True)

    embedded = models.TextField(_('Text Embedded'), blank=True)
    file = models.FileField(upload_to="lessons/materials", blank=True, null=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name=_('Lesson'), related_name='materials')

    class Meta:
        verbose_name = _('Material')
        verbose_name_plural = _('Materials')

    def __str__(self):
        return 'Material: {0}'.format(self.name)

    def is_embedded(self):
        return bool(self.embedded)


class Enrollment(models.Model):
    STATUS_CHOICES = (
        (0, _('Pending Approval')),
        (1, _('Approved to take the course')),
        (2, _('Canceled')),
        (3, _('Awaiting Course Release'))
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name=_('User'),
        on_delete=models.CASCADE, related_name='enrollments'
    )
    course = models.ForeignKey(
        Course, verbose_name=_('Course'),
        on_delete=models.CASCADE, related_name='Enrollments'
    )
    status = models.IntegerField(
        _('Situation'), choices=STATUS_CHOICES, default=1, blank=True
    )
    created_at = models.DateTimeField(_('Create at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated at'), auto_now=True)

    class Meta:
        verbose_name = _('Enrollment')
        verbose_name_plural = _('Enrollments')
        unique_together = (('user', 'course'),)

    def __str__(self):
        return '{0} enrolled in {1}'.format(self.user, self.course)

    def active(self):
        self.status = 1
        self.save()

    def is_approved(self):
        return self.status == 1


class Announcement(models.Model):
    course = models.ForeignKey(
        Course, verbose_name=_('Course'),
        on_delete=models.CASCADE, related_name='announcements'
    )
    title = models.CharField(_('Title'), max_length=100)
    content = models.TextField(_('Content'))
    created_at = models.DateTimeField(_('Create at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Update at'), auto_now=True)

    def __str__(self):
        return self.title[:50]

    class Meta:
        verbose_name = _('Advertisement')
        verbose_name_plural = _('Advertisements')
        ordering = ['-created_at']


class Comment(models.Model):
    announcement = models.ForeignKey(
        Announcement, verbose_name=_('Advertisement'),
        on_delete=models.CASCADE, related_name='comments'
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('User'))
    comment = models.TextField(_('Comment'))
    created_at = models.DateTimeField(_('Create at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated at'), auto_now=True)

    def __str__(self):
        return self.comment[:50]

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')
        ordering = ['created_at']


def post_save_announcement(instance, created, **kwargs):
    if created:
        subject = instance.title
        context = {
            'announcement': instance
        }
        template_name = 'courses/announcement_mail.html'
        enrollments = Enrollment.objects.filter(
            course=instance.course, status=1
        )
        for enrollment in enrollments:
            recipient_list = [enrollment.user.email]
            send_mail_template(subject, template_name, context, recipient_list)


models.signals.post_save.connect(
    post_save_announcement, sender=Announcement,
    dispatch_uid='post_save_announcement'
)

