from rest_framework import status
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response

from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny

from .serializers import CategorySerializer, CourseSerializer, TeacherSerializer
from ..models import Course, Category, Teacher


# Create API methods/verbs automatic, only gets (list and search one)
class CategoryViewSet(ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = (AllowAny, )


# Create API methods/verbs automatic
class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticated, )


# Create API methods/verbs automatic
class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticated, )


