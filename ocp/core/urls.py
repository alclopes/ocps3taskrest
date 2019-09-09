from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('contato/', views.contact, name='contact'),
]


#
# from django.conf.urls import patterns, url
#
# app_name = 'core'
#
# urlpatterns = patterns('ead.core.views',
#     url(r'^$', 'home', name='home'),
#     url(r'^contato/$', 'contact', name='contact'),
# )
#
