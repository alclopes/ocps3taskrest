from django import forms
from django.conf import settings
from ocp.core.mail import send_mail_template
from .models import Comment, Course, Category, Material
from functools import partial
from autoslug import AutoSlugField
from django.utils.translation import ugettext as _
from django.core.exceptions import ValidationError

DateInput = partial(forms.DateInput, {'class': 'datepicker form-control'})


class CategoryForm(forms.ModelForm):
    name = forms.CharField(label=_('Name'), max_length=128, help_text=_("Please enter the category name."))
    description = forms.CharField(label=_('Description'), max_length=256, required=False, help_text=_("Please enter the description of the category."))
    views = forms.IntegerField(label=_('Views'), widget=forms.HiddenInput(), initial=0)
    status = forms.BooleanField(label=_('Status'),
                               required=False,
                               help_text=_("Is this category still active?"))

    # An inline class to provide additional information on the form.
    class Meta:
        model = Category
        fields = ('name', 'description')


class CourseForm(forms.ModelForm):
    name = forms.CharField(label=_('Name'), max_length=128, widget=forms.TextInput(attrs={"class": "form-control",
                                                                          'placeholder': _('Course Title')}))
    description = forms.CharField(label=_('Description'), max_length=128, required=False, widget=forms.TextInput(attrs={"class": "form-control",
                                                                          'placeholder': _('Course Summary')}))
    about = forms.CharField(label=_('About'), max_length=600, required=False,
                                  widget=forms.TextInput(attrs={"class": "form-control",
                                                                'placeholder': _('Course About')}))
    url = forms.URLField(label=_('URL'), max_length=200, widget=forms.URLInput(attrs={"class": "form-control validate-url",
                                                                          'placeholder': _('Course URL')}))
    phone = forms.CharField(label=_('Phone'), max_length=15, widget=forms.TextInput(attrs={"class": "form-control bfh-phone",
                                                                           "data-format" : "ddd-ddd-dddd"}))
    start_date = forms.DateField(label=_('Start Date'), input_formats=['%m/%d/%Y'], widget=DateInput(format='%m/%d/%Y'), help_text=_("MM/DD/YYYY"))
    image = forms.ImageField()
    status = forms.BooleanField(label=_('Status'),
                               required=False,
                               help_text=_("Is this category still active?"))
    hascertification = forms.BooleanField(label=_('Has Certification Test? '),
                               required=False,
                               help_text=_("Please check here if the course offers certification test."))

    class Meta:
        model = Course
        fields = ('name', 'url', 'description', 'about', 'phone', 'start_date', 'image', 'status', 'hascertification',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']


class ContactCourseForm(forms.Form):
    name = forms.CharField(label=_('Name'), max_length=100)
    email = forms.EmailField(label=_('Email'))
    message = forms.CharField(label=_('Message/Questions'), widget=forms.Textarea)

    def send_mail(self, course):
        subject = '[%s] Contact' % course
        context = {
            'name': self.cleaned_data['name'],
            'email': self.cleaned_data['email'],
            'message': self.cleaned_data['message'],
        }
        template_name = 'courses/contact_email.html'
        send_mail_template(subject, template_name, context, [settings.CONTACT_EMAIL]
        )


class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['name', 'embedded', 'file', 'lesson']

    def clean(self):
        super().clean()
        if self.cleaned_data['embedded'] != "" and self.cleaned_data['file'] != "":
            raise ValidationError(_('Not allow the fill to embedded and file fields in the same Material, please choice only one for fill'))
        elif self.cleaned_data['embedded'] == "" and self.cleaned_data['file'] == None:
            raise ValidationError(_('Please choice and fill one material to lesson: embedded or file'))