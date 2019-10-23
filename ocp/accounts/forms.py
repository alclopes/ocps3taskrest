from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from ocp.core.mail import send_mail_template
from ocp.core.utils import generate_hash_key
from django.utils.translation import gettext_lazy as _
# from django.utils.translation import ugettext as _
from .models import PasswordReset

# Aqui informamos ao form que o usuário que iremos utilizar
# não será o user padrão do django,
# iremos usar o user que criamos no accounts.model.user
User = get_user_model()


class PasswordResetForm(forms.Form):
    email = forms.EmailField(label='E-mail')
    # Verifica se o email existe no banco de dados,
    # se não encontrar retorna erro, senão retorna o email.

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            return email
        raise forms.ValidationError(_('There isnt user with this email'),)

    def save(self):
        user = User.objects.get(email=self.cleaned_data['email'])
        key = generate_hash_key(user.username)
        reset = PasswordReset(key=key, user=user)
        reset.save()
        template_name = 'accounts/password_reset_mail.html'
        subject = _('Change your password'),
        context = {
            'reset': reset,
        }
        send_mail_template(subject, template_name, context, [user.email])


# Como não estamos usando o user do django, t=
# temos que criar uma herança da model form e reescreve-la.
class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label=_('Password'), widget=forms.PasswordInput)
    password2 = forms.CharField(
        label=_('Confirm your password'), widget=forms.PasswordInput
    )
    # Verifica se as passwords são diferentes,
    # senão retorna a password.

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(_l('The Confirm is wrong'))
        return password2

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'email']


class EditAccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'name']