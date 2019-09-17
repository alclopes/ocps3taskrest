from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from ..models import Course, Category, Teacher


# Serializers define the API representation.
class CategorySerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'slug', 'status', 'created_at', 'updated_at')


# Serializers define the API representation.
class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        depth = 1  # Nível de profundidade que você quer exibir no JSON
        fields = ('id', 'name', 'slug', 'category', 'phone', 'url', 'description', 'about',
                  'start_date', 'hascertification', 'status')

# Serializers define the API representation.
class TeacherSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('user', 'course')


# Serializers define the API representation.
class LessonSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ( 'name', 'description', 'release_date', 'course', 'created_at')
