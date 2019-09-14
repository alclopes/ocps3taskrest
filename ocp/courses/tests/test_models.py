from django.test import TestCase
from django.test.client import Client
from django.db.models import Q

from model_mommy import mommy

from ocp.courses.models import Category, Course


# Verifica a existencia de certos atributos no model
class CourseTestCase(TestCase):
    def test_should_return_attributes(self):
        self.assertTrue(hasattr(Course, 'name'))
        self.assertTrue(hasattr(Course, 'slug'))
        self.assertTrue(hasattr(Course, 'description'))



class CourseManagerTestCase(TestCase):
    def setUp(self):

        # Category(id='1', name='Category01', description='Description Category01', slug='category01', status='1',
        #          created_at='2019-07-29 09:49:41.696960', updated_at='2019-07-29 09:49:41.696960').save()

        Category.objects.create(id='1', name='Category01', description='Description Category01', slug='category01', status='1',
                 created_at='2019-07-29 09:49:41.696960', updated_at='2019-07-29 09:49:41.696960')

        Course(id='1', name='Name Course01', phone='34444444', url='http://127.0.0.1:8000/admin/courses',
               description='description Course',
               about='about Course01 about Course ',
               start_date='2018-07-01', image='courses/images/Course_1.png', created_at='2019-07-29 10:31:15.998613',
               updated_at='2019-08-06 17:23:29.576034', hascertification='1', status='1', views='1', category_id='1',
               qualification='0', slug='course01').save()
        Course(id='2', name='Name Course02', phone='4236423624', url='http://127.0.0.1:8000/admin/courses',
               description='description Course02 ',
               about='about Course02 about Course ',
               start_date='2018-07-01', created_at='2019-07-29 13:42:22.693867',
               updated_at='2019-08-06 17:23:58.835743',
               hascertification='1', status='0', views='2', category_id='1', qualification='20', slug='course02').save()
        Course(id='3', name='Name Course03', phone='5341345123', url='http://127.0.0.1:8000/admin/courses',
               description='description Course03',
               about='about Course03 about Course',
               start_date='3000-07-02', image='courses/images/Course_3.png', created_at='2019-07-29 13:44:06.586065',
               updated_at='2019-08-04 10:25:31.654796', hascertification='1', status='1', views='7', category_id='1',
               qualification='15', slug='course03').save()
        Course(id='4', name='Name Course04', phone='34444444', url='http://127.0.0.1:8000/admin/courses',
               description='description Course',
               about='about Course01 about Course ',
               start_date='3000-07-02', image='courses/images/Course_1.png', created_at='2019-07-29 10:31:15.998613',
               updated_at='2019-08-06 17:23:29.576034', hascertification='1', status='0', views='1', category_id='1',
               qualification='0', slug='course04').save()

        self.client = Client()

    def tearDown(self):
        Course.objects.all().delete()

    def test_course_search(self):
        search = Course.objects.search('Name')
        self.assertEqual(len(search), 4)

        search = Course.objects.search('Course02')
        self.assertEqual(len(search), 1)

    def test_active_course(self):
        # assertTrue
        course = Course.objects.get(id=2)
        self.assertTrue(course.is_active_course())

    def test_inactive_course(self):
        # assertFalse
        course = Course.objects.get(id=1)
        self.assertFalse(course.is_active_course())
        course = Course.objects.get(id=3)
        self.assertFalse(course.is_active_course())
        course = Course.objects.get(id=4)
        self.assertFalse(course.is_active_course())

