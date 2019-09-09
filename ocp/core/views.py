from django.shortcuts import render
from .forms import ContactSite
from django.contrib import messages
from django.utils.translation import ugettext as _


def home(request):
    return render(request, 'home.html')


# Create template Speak with us
def contact(request):
    context = {}
    if request.method == 'POST':
        form = ContactSite(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            title = _("Speak with Us")
            form.send_mail(title)
            form = ContactSite()
            message = _('Your messsage was sended with success')
            messages.success(request, message)
        else:
            message = _('Sorry your message not be sended. Please, Try again or choice other type of contact')
            messages.success(request, message)
    else:
        form = ContactSite()
    context['form'] = form
    template_name = 'core/contact.html'
    return render(request, template_name, context)
