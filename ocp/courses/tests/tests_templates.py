from django.db.models import Max
from django.test import Client, TestCase

from ...accounts.models import User
from ..models import Category, Course, Enrollment, Announcement, Lesson, Material, Teacher


class CoursesTestCase(TestCase):

    def setUp(self):

        User(id='1', password='pbkdf2_sha256$20000$GDG2ExejLdID$+jZqG9jb9QQPASguwBlIxiWLH09h/DldlB5+SCvoa40=',
             last_login='2019-08-06 17:16:57.015753', is_superuser='1', email='admin@ocpplus.com', name='Admin',
             phone='900004674', is_active='1', is_staff='1', date_joined='2019-07-29 08:12:08.986190',
             username='admin').save()
        Category.objects.create(id='1', name='Name Category01', description='Description Category01', slug='category01', status='1',
                 created_at='2019-07-29 09:49:41.696960', updated_at='2019-07-29 09:49:41.696960')

        Course(id='1', name='Name Course01', phone='34444444', url='http://127.0.0.1:8000/admin/courses',
               description='description Course',
               about='about Course01 about Course ',
               start_date='2018-07-01', image='courses/images/Course_1.png', created_at='2019-07-29 10:31:15.998613',
               updated_at='2019-08-06 17:23:29.576034', hascertification='1', status='1', views='1', category_id='1',
               qualification='0', slug='course01').save()
        Lesson(id='1',
               description='Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson ',
               number='1', release_date='2018-07-01', created_at='2019-08-01 14:34:54.175060',
               updated_at='2019-08-02 05:30:04.356337', course_id='1', name='Lesson05 C1').save()
        Material(id='1', file='Lessons/Materials/Video01.mp4', lesson_id='1', name='Material01V').save()

        self.client = Client()

    def test_index(self):
        c = Client()
        response = c.get("/")
        self.assertEqual(response.status_code, 200)

    def test_empty_category_list_page(self):
        c = Client()
        response = c.get("/course/category_list/")
        self.assertEqual(response.status_code, 200)

    def test_category_details_page(self):
        category = Category.objects.get(slug='category01')
        c = Client()
        response = c.get(f"/course/category_details/{category.slug}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual('Name Category01', response.context["category_name"])

    def test_course_details_page(self):
        course = Course.objects.get(slug='course01')
        c = Client()
        response = c.get(f"/course/course_details/{course.slug}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual('Name Course01', response.context[0].dicts[3]['course'].name)

    def test_valid_Lesson_page(self):
        course = Course.objects.get(slug='course01')
        lesson = Lesson.objects.get(id='1')
        c = Client()
        response = c.get(f"/course/{course.slug}/lesson/{lesson.id}/")
        # print(response['location'])
        self.assertEqual(response.status_code, 302)
        # self.assertContains(response, "You must be logged in", status_code=200)
        c = Client()
        c.login(username='admin', password='admin')
        response = c.get(f"/course/{course.slug}/lesson/{lesson.id}/")
        self.assertEqual(response.status_code, 200)

    def test_invalid_Lesson_page(self):
        course = Course.objects.get(slug='course01')
        max_id = Lesson.objects.all().aggregate(Max("id"))["id__max"]
        c = Client()
        response = c.get(f"/course/{course.slug}/lesson/{max_id + 1}/")
        self.assertEqual(response.status_code, 302)
        c = Client()
        c.login(username='admin', password='admin')
        response = c.get(f"/course/{course.slug}/lesson/{max_id + 1}/")
        self.assertEqual(response.status_code, 404)
