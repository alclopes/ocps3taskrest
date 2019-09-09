from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from django.http import HttpResponseRedirect
from django.conf.urls.static import static
from decouple import config

from rest_framework import routers
from ocp.accounts.api.viewsets import UserViewSet
from ocp.courses.api.viewsets import CategoryViewSet, CourseViewSet, TeacherViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users/v1', UserViewSet)
router.register(r'categories/v1', CategoryViewSet)
router.register(r'courses/v1', CourseViewSet)
router.register(r'teacher/v1', TeacherViewSet)

admin.autodiscover()

urlpatterns = [
    path('', include('ocp.core.urls', namespace='core')),
    path('language/', include('ocp.languages.urls', namespace='languages')),
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
]

# Add Router URL
urlpatterns += [
    path('api/', include(router.urls)),
    # path('api-token-auth/', obtain_auth_token),
]

# Add URLConf for courses (Category, Course, teachers).
urlpatterns += [
    path('account/', include('ocp.accounts.urls', namespace='accounts')),
    path('course/', include('ocp.courses.urls', namespace='courses')),
    path('forum/', include('ocp.forum.urls', namespace='forum')),
]

# Use mapping to fix favicon.ico (#google chrome, firefox)
urlpatterns += [
    path('favicon.ico/', lambda x: HttpResponseRedirect(settings.STATIC_URL+'images/favicon.ico')),
]

# ##########################Media/Static
USE_S3 = config('USE_S3', default=True, cast=bool)
if settings.DEBUG and not USE_S3:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# ################### Django 1.X
# from django.contrib import admin
# from django.conf import settings
# from django.conf.urls.static import static
# from decouple import config
# from django.conf.urls import patterns, include, url
#
# urlpatterns = patterns('',
#     url(r'^', include('ead.core.urls', namespace='core')),
#     url(r'^account/', include('ocp.accounts.urls', namespace='accounts')),
#     url(r'^course/', include('ocp.courses.urls', namespace='courses')),
#     url(r'^forum/', include('ocp.forum.urls', namespace='forum')),
#     url(r'^language/', include('ocp.languages.urls', namespace='languages')),
#     url(r'^i18n/', include('django.conf.urls.i18n')),
#     url(r'^admin/', include(admin.site.urls)),
# )
#

