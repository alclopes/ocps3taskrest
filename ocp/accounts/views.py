from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import (UserCreationForm, PasswordChangeForm,
    SetPasswordForm)
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
from django.utils.translation import ugettext as _
from ocp.core.utils import generate_hash_key
from ocp.courses.models import Enrollment
from .forms import RegisterForm, EditAccountForm, PasswordResetForm
from .models import PasswordReset
# Aqui informamos ao form que o usuário que iremos utilizar
# não será o user padrão do django,
# iremos usar o user que criamos no accounts.model.user
User = get_user_model()


def logout_view(request):
    logout(request)
    return redirect(reverse('core:home'))


@login_required
def dashboard(request):
    template_name = 'accounts/account_dashboard.html'
    context = {}
    return render(request, template_name, context)


def register(request):
    template_name = 'accounts/register.html'
    #Evite este caso temos instancia do form em qualquer situação
    #  Usar conforme view announcement_detail na View Course
    #      form = CommentForm(request.POST or None)
    if request.method == 'POST':
        form = RegisterForm(request.POST) #instancia
        if form.is_valid():
            user = form.save()
            user = authenticate(
                username=user.username, password=form.cleaned_data['password1']
            )
            login(request, user)
            return redirect(reverse('core:home'))
    else:
        form = RegisterForm() #instancia
    context = {
        'form': form
    }
    return render(request, template_name, context)


def password_reset(request):
    template_name = 'accounts/password_reset.html'
    context = {}
    # /Importante Quando passamos um post que pode ir vazio o html já irá validar e emitir mensagens de erro
    # Para evitar isso colocamos "or Nome", pois se o post estiver vazio o python interpretara
    # que é um valor errado de post e enviara o valor "None"
    # O email pode vir vazio pois não era um campo obrigatorio no registro.
    form = PasswordResetForm(request.POST or None)
    # Se o valor do form é None o formulario HTML não irá mais validar
    if form.is_valid():
        form.save()
        context['success'] = True
    context['form'] = form
    return render(request, template_name, context)


def password_reset_confirm(request, key):
    template_name = 'accounts/password_reset_confirm.html'
    context = {}
    reset = get_object_or_404(PasswordReset, key=key)
    form = SetPasswordForm(user=reset.user, data=request.POST or None)
    if form.is_valid():
        form.save()
        context['success'] = True
    context['form'] = form
    return render(request, template_name, context)


@login_required
def edit(request):
    template_name = 'accounts/edit_account.html'
    context = {}
    if request.method == 'POST':
        form = EditAccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(
                request, _('Your datas was updated with success')
            )
            return redirect('accounts:dashboard')
    else:
        form = EditAccountForm(instance=request.user)
    context['form'] = form
    return render(request, template_name, context)


@login_required
def edit_password(request):
    template_name = 'accounts/edit_password.html'
    context = {}
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            context['success'] = True
    else:
        form = PasswordChangeForm(user=request.user)
    context['form'] = form
    return render(request, template_name, context)
