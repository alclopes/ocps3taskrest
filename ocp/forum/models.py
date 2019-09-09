from django.db import models
from django.conf import settings
from taggit.managers import TaggableManager
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse

# Model of topic's forum
class Thread(models.Model):
    title = models.CharField(_('Title'), max_length=100)
    slug = models.SlugField(_('Slug'), max_length=100, unique=True)
    body = models.TextField(_('Message'))
    # O uso do related_name será por exemplo: thread__author=request.user
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        verbose_name=_('Author'), related_name='threads'
    )
    views = models.IntegerField(_('Views'), blank=True, default=0)
    # Quantidade de respostas deste topico
    answers = models.IntegerField(_('Anwers'), blank=True, default=0)
    
    tags = TaggableManager()
    created = models.DateTimeField(_('Create at'), auto_now_add=True)
    modified = models.DateTimeField(_('Update at'), auto_now=True)

    class Meta:
        verbose_name = _('Topic')
        verbose_name_plural = _('Topic')
        ordering = ['-modified']

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('forum:thread', kwargs={'slug': self.slug})


# Model of answer to topics of forum
class Reply(models.Model):
    thread = models.ForeignKey(
        Thread, verbose_name=_('Topic'),
        on_delete=models.CASCADE, related_name='replies'
    )
    reply = models.TextField(_('Answer'))
    # O Autor é a pessoa que estará logada na maquina respondendo.
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name=_('Author'),
        on_delete=models.CASCADE, related_name='replies'
    )
    # Valoriza para informar se a resposta foi considerada correta
    correct = models.BooleanField(_('Correct?'), blank=True, default=False)
    created = models.DateTimeField(_('Create at'), auto_now_add=True)
    modified = models.DateTimeField(_('Updated at'), auto_now=True)
    # Pega somente as 100  primeiras letras

    class Meta:
        verbose_name = _('Answer')
        verbose_name_plural = _('Anwers')
        ordering = ['-correct', 'created']

    def __str__(self):
        return self.reply[:100]


# Criando um signals apos salvar uma resposta com objetivo de
# incrementar 1 ao total de respostas no model tópico
def post_save_reply(created, instance, **kwargs):
    # Usou o comando count em vez de incrementar para garantir que
    # a informação esta atualizada.
    instance.thread.answers = instance.thread.replies.count()
    instance.thread.save()
    if instance.correct:
        # atualiza todas as outras respostas como falsas
        instance.thread.replies.exclude(pk=instance.pk).update(
            correct=False
        )


# Criando um signals apos salvar uma resposta com objetivo de
# diminuir 1 ao total de respostas no model tópico
def post_delete_reply(instance, **kwargs):
    # Usou o comando count em vez de incrementar para garantir que
    # a informação esta atualizada.
    instance.thread.answers = instance.thread.replies.count()
    instance.thread.save()
# Sobreescreve o signal post_save do model


models.signals.post_save.connect(
    post_save_reply, sender=Reply, dispatch_uid='post_save_reply'
)


# Sobreescreve o signal post_delete do model
models.signals.post_delete.connect(
    post_delete_reply, sender=Reply, dispatch_uid='post_delete_reply'
)