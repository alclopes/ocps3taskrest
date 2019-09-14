from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('cadastre-se/', views.register, name='register'),
    path('nova-senha/', views.password_reset, name='password_reset'),
    path('confirmar-nova-senha/<key>/', views.password_reset_confirm, name='password_reset_confirm'),
    path('editar/', views.edit, name='edit'),
    path('editar-senha/', views.edit_password, name='edit_password'),
]

# from django.conf.urls import patterns, include, url
# urlpatterns = patterns('',
#     url(r'^$', 'ocp.accounts.views.dashboard', name='dashboard'),
#     url(r'^entrar/$', 'django.contrib.auth.views.login', {'template_name': 'accounts/login.html'}, name='login'),
#     url(r'^sair/$', 'django.contrib.auth.views.logout', {'next_page': 'core:home'}, name='logout'),
#     url(r'^cadastre-se/$', 'ocp.accounts.views.register', name='register'),
#     url(r'^nova-senha/$', 'ocp.accounts.views.password_reset', name='password_reset'),
#     url(r'^confirmar-nova-senha/(?P<key>\w+)/$', 'ocp.accounts.views.password_reset_confirm', name='password_reset_confirm'),
#     url(r'^editar/$', 'ocp.accounts.views.edit', name='edit'),
#     url(r'^editar-senha/$', 'ocp.accounts.views.edit_password', name='edit_password'),
# )
