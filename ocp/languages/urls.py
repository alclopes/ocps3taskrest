from django.urls import path
from . import views

app_name = 'languages'

urlpatterns = [
    path('', views.index, name='index'),
    path('set_language/<user_language>/', views.set_language_from_url, name="set_language_from_url")
]

#
# from django.conf.urls import patterns, url
# from . import views
# app_name = 'languages'
# urlpatterns = patterns('ead.languages.views',
#     url(r'^$', 'index', name='index'),
#     url(r'/set_language/(?P<user_language>\w+)/$', views.set_language_from_url, name="set_language_from_url")
# )
#
