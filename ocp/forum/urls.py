from django.urls import path
from . import views

app_name = 'forum'

urlpatterns = [
    path('', views.index, name='index'),
    path('tag/<tag>/', views.index, name='index_tagged'),
    path('anwers/<pk>/correta/', views.reply_correct, name='reply_correct'),
    path('anwers/<pk>/incorreta/', views.reply_incorrect, name='reply_incorrect'),
    path('<slug>/', views.thread, name='thread')
]


#
# from django.conf.urls import patterns, include, url
#
# urlpatterns = patterns('ead.forum.views',
#     url(r'^$', 'index', name='index'),
#     url(r'^tag/(?P<tag>[\w_-]+)/$', 'index', name='index_tagged'),
#     url(r'^Anwers/(?P<pk>\d+)/correta/$', 'reply_correct',
#         name='reply_correct'),
#     url(r'^Anwers/(?P<pk>\d+)/incorreta/$', 'reply_incorrect',
#         name='reply_incorrect'),
#     url(r'^(?P<slug>[\w_-]+)/$', 'thread', name='thread'),
# )
#
