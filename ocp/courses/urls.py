from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.index, name='index'),
    path('category_list/', views.category_list, name='category_list'),
    path('course_list/', views.course_list, name='course_list'),
    path('category_details/<pkSlug>/', views.category_details, name='category_details'),
    path('course_details/<pkSlug>/', views.course_details, name='course_details'),
    path('category_add/', views.category_add, name='category_add'),
    path('course_add/<pkSlug>/', views.course_add, name='course_add'),
    path('<slug>/incharge/', views.incharge, name='incharge'),
    path('<slug>/enrollment/', views.enrollment, name='enrollment'),
    path('<slug>/enrollment_undo/', views.enrollment_undo, name='enrollment_undo'),
    path('<slug>/announcements/', views.announcements, name='announcements'),
    path('<slug>/announcement_detail/<pk>)/', views.announcement_detail, name='announcement_detail'),
    path('<slug>/list_lessons/', views.lesson_list, name='lesson_list'),
    path('<slug>/lesson/<pk>)/', views.lesson_detail, name='lesson_detail'),
    path('<slug>/material/<pk>)/', views.material_detail, name='material_detail'),
    path('video/<vid>)/', views.video_show, name='video_show'),
]


# from django.conf.urls import patterns, url
#
# app_name = 'courses'
#
# urlpatterns = patterns('ead.courses.views',
#     url(r'^$', 'index', name='index'),
#     url(r'^category_list/$', 'category_list', name='category_list'),
#     url(r'^course_list/$', 'course_list', name='course_list'),
#     url(r'^category_details/(?P<pkSlug>[\w_-]+)/$', 'category_details', name='category_details'),
#     url(r'^course_details/(?P<pkSlug>[\w_-]+)/$', 'course_details', name='course_details'),
#     url(r'^category_add/$', 'category_add', name='category_add'),
#     url(r'^course_add/(?P<pkSlug>[\w_-]+)/$', 'course_add', name='course_add'),
#     url(r'^(?P<slug>[\w_-]+)/incharge/$', 'incharge', name='incharge'),
#     url(r'^(?P<slug>[\w_-]+)/enrollment/$', 'enrollment', name='enrollment'),
#     url(r'^(?P<slug>[\w_-]+)/enrollment_undo/$', 'enrollment_undo', name='enrollment_undo'),
#     url(r'^(?P<slug>[\w_-]+)/announcements/$', 'announcements', name='announcements'),
#     url(r'^(?P<slug>[\w_-]+)/announcement_detail/(?P<pk>\d+)/$', 'announcement_detail', name='announcement_detail'),
#     url(r'^(?P<slug>[\w_-]+)/list_lessons/$', 'lesson_list', name='lesson_list'),
#     url(r'^(?P<slug>[\w_-]+)/lesson/(?P<pk>\d+)/$', 'lesson_detail', name='lesson_detail'),
#     url(r'^(?P<slug>[\w_-]+)/material/(?P<pk>\d+)/$', 'material_detail', name='material_detail'),
#     url(r'^video/(?P<vid>\w+)/$', 'video_show', name='video_show'),
# )
#
