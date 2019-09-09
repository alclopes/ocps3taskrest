from django import forms
from django.conf import settings
from ocp.core.mail import send_mail_template
from django.utils.translation import ugettext as _


class ContactSite(forms.Form):
    name = forms.CharField(label=_('Name'), max_length=100)
    email = forms.EmailField(label=_('Email'))
    message = forms.CharField(label=_('Message/Questions'), widget=forms.Textarea)

    def send_mail(self, title):
        subject = '[%s] Contact' % title
        context = {
            'name': self.cleaned_data['name'],
            'email': self.cleaned_data['email'],
            'message': self.cleaned_data['message'],
        }
        template_name = 'core/contact_email.html'
        send_mail_template(subject, template_name, context, [settings.CONTACT_EMAIL]
        )

