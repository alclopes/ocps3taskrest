import re
from django.db import models
from django.core import validators
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin,
                                        UserManager)
from django.conf import settings
#Internacionalização use: No models.py use o ugettext_lazy,
# nos demais use ugettext
from django.utils.translation import ugettext_lazy as _
#Internacionalização: Pluralização é com o ngettext
from django.utils.translation import ngettext
# nesta versõa do django precisa herdar as duas classes abaixo para herdar do User do django
# quando fazemos esta herança o django deixa de usar sua classe user
# e usa esta herdada (irá criar o superuser e os demais usuários nesta herdada
# se olharmos no banco apos a migração veremos que não será mais a tabela auth.user
# ele irá criar a tabela accounts.user.
# No Django2.0+ você não herda mais estas classes.


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        _('User Name'), max_length=30, unique=True,
        validators=[validators.RegexValidator(re.compile('^[\w.@+-]+$'),
                                              _('Username can only contain letters, digits, or the following characters: @/./+/-/_'), 'invalid'
                                              )]
    )

    email = models.EmailField(_('Email'), unique=True)
    name = models.CharField(_('Name'), max_length=100, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    # Algumas funcões futuras precisarão da informação se o usuario esta ativo.
    is_active = models.BooleanField(_('Is Active?'), blank=True, default=True)
    # se for staff pode a acessar a área administrativa?
    is_staff = models.BooleanField(_('Is Staff?'), blank=True, default=False)
    # somente na criação do registro esta data é salva.
    date_joined = models.DateTimeField(_('Date Joined'), auto_now_add=True)
    # É o manager para gerenciador do usuario
    objects = UserManager()
    # variável que define para a criação do superuser o campo username
    # este campo será unico e referencia para o login, poderia se o email
    USERNAME_FIELD = 'username'
    # variáveis que também serão exigidas durante a criação do superuser
    REQUIRED_FIELDS = ['email']
    # string para identificar o usuário
    # Neste caso se tiver nome irá  mostrar o nome (como nã é obrigatorio), senão mostrará o email.


    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.name or self.username

    # irá retornar o username
    def get_short_name(self):
        return self.username

    # ira retornar a saida do def __str(self)
    def get_full_name(self):
        return str(self)



# A classe PasswordReset é criada pois o reset de semha será por email,
# Nesta classe salvaremos a chave randomica/um link de acesso que passaremos
# ao cliente para mudar a senha
class PasswordReset(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name=_('User'),
        on_delete=models.CASCADE, related_name='resets'
    )
    key = models.CharField(_('Key'), max_length=100, unique=True)
    created_at = models.DateTimeField(_('Create at'), auto_now_add=True)
    confirmed = models.BooleanField(_('Confirm?'), default=False, blank=True)

    class Meta:
        verbose_name = _('New Password')
        verbose_name_plural = _('New Passords')
        ordering = ['-created_at']

    def __str__(self):
        return '{0} em {1}'.format(self.user, self.created_at)

