import os
from decouple import config

os.environ.setdefault('DJANGO_SETTINGS_MODULE', config('SETTINGS_MODULE_PATH'))

import django
django.setup()

from ocp.accounts.models import User
from ocp.courses.models import Category, Course, Lesson, Material, Announcement, Teacher, Comment, Enrollment
from ocp.forum.models import Thread, Reply
from taggit.models import Tag, TaggedItem

def populate():

    # ############################ Delete all tables
    TaggedItem.objects.all().delete()
    Tag.objects.all().delete()
    Reply.objects.all().delete()
    Thread.objects.all().delete()
    Enrollment.objects.all().delete()
    Comment.objects.all().delete()
    Teacher.objects.all().delete()
    User.objects.all().delete()
    Announcement.objects.all().delete()
    Material.objects.all().delete()
    Lesson.objects.all().delete()
    Course.objects.all().delete()
    Category.objects.all().delete()

    # ############################ Start creates

    # Category
    Category(id='1', name='Category01', description='Description Category01', slug='category01', status='1',
             created_at='2019-07-29 09:49:41.696960', updated_at='2019-07-29 09:49:41.696960').save()
    Category(id='2', name='Category02', description='Description Category02', slug='category02', status='1',
             created_at='2019-07-29 10:31:53.672477', updated_at='2019-07-29 10:31:53.672477').save()
    Category(id='3', name='Category03', description='Description Category03', slug='category03', status='1',
             created_at='2019-07-29 10:31:53.672477', updated_at='2019-07-29 10:31:53.672477').save()
    Category(id='4', name='Category04', description='Description Category04', slug='category04', status='1',
             created_at='2019-07-29 10:31:53.672477', updated_at='2019-07-29 10:31:53.672477').save()
    Category(id='5', name='Category05', description='Description Category05', slug='category05', status='1',
             created_at='2019-07-29 10:31:53.672477', updated_at='2019-07-29 10:31:53.672477').save()
    Category(id='6', name='Category06', description='Description Category06', slug='category06', status='1',
             created_at='2019-07-29 10:31:53.672477', updated_at='2019-07-29 10:31:53.672477').save()
    Category(id='7', name='Category08', description='Description Category08', slug='category08', status='1',
             created_at='2019-08-03 15:37:36.457265', updated_at='2019-08-03 15:37:36.457265').save()
    Category(id='8', name='Category07', description='Description Category', slug='category07', status='1',
             created_at='2019-08-04 14:00:34.929835', updated_at='2019-08-04 14:00:34.929835').save()
    Category(id='9', name='Category09', description='Description Category', slug='category09', status='1',
             created_at='2019-08-06 19:07:09.407013', updated_at='2019-08-06 19:07:09.407013').save()
    # Course
    Course(id='1', name='Course01', phone='34444444', url='http://127.0.0.1:8000/admin/courses',
           description='description Course01 description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course ',
           about='about Course01 about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course ',
           start_date='2018-07-01', image='courses/images/Course_1.png', created_at='2019-07-29 10:31:15.998613',
           updated_at='2019-08-06 17:23:29.576034', hascertification='1', status='1', views='1', category_id='1',
           qualification='0', slug='course01').save()
    Course(id='2', name='Course02', phone='4236423624', url='http://127.0.0.1:8000/admin/courses',
           description='description Course02 description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course',
           about='about Course02 about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course ',
           start_date='2018-08-15', created_at='2019-07-29 13:42:22.693867', updated_at='2019-08-06 17:23:58.835743',
           hascertification='1', status='1', views='2', category_id='1', qualification='20', slug='course02').save()
    Course(id='3', name='Course03', phone='5341345123', url='http://127.0.0.1:8000/admin/courses',
           description='description Course03 description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course',
           about='about Course03 about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course ',
           start_date='2019-07-02', image='courses/images/Course_3.png', created_at='2019-07-29 13:44:06.586065',
           updated_at='2019-08-04 10:25:31.654796', hascertification='1', status='1', views='7', category_id='1',
           qualification='15', slug='course03').save()
    Course(id='4', name='Course04', phone='4232323523', url='http://127.0.0.1:8000/admin/courses',
           description='description Course04 description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course',
           about='about Course04 about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course ',
           start_date='2018-08-16', created_at='2019-07-29 13:45:41.900255', updated_at='2019-07-29 13:47:48.051965',
           hascertification='1', status='1', views='4', category_id='2', qualification='12', slug='course04').save()
    Course(id='5', name='Course05', phone='2564352352', url='http://127.0.0.1:8000/admin/courses',
           description='description Course05 description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course',
           about='about Course05 about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course ',
           start_date='2018-07-03', created_at='2019-07-29 13:47:20.099848', updated_at='2019-07-29 13:48:34.690914',
           hascertification='1', status='1', views='8', category_id='2', qualification='19', slug='course05').save()
    Course(id='6', name='Course06', phone='2564352352', url='http://127.0.0.1:8000/admin/courses',
           description='description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description CourseXX description Course description Course description Course description Course',
           about='about CourseXX about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course ',
           start_date='2019-09-17', image='courses/images/Course_6.png', created_at='2019-07-29 13:47:20.099848',
           updated_at='2019-08-04 10:25:11.983579', hascertification='1', status='1', views='6', category_id='3',
           qualification='6', slug='course06').save()
    Course(id='7', name='Course07', phone='2564352352', url='http://127.0.0.1:8000/admin/courses',
           description='description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description CourseXX description Course description Course description Course description Course',
           about='about CourseXX about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course ',
           start_date='2018-07-04', created_at='2019-07-29 13:47:20.099848', updated_at='2019-07-29 13:48:34.690914',
           hascertification='1', status='1', views='7', category_id='2', qualification='2', slug='course07').save()
    Course(id='8', name='Course08', phone='2564352352', url='http://127.0.0.1:8000/admin/courses',
           description='description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description CourseXX description Course description Course description Course description Course',
           about='about CourseXX about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course ',
           start_date='2018-08-18', created_at='2019-07-29 13:47:20.099848', updated_at='2019-07-29 13:48:34.690914',
           hascertification='1', status='1', views='5', category_id='1', qualification='9', slug='course08').save()
    Course(id='9', name='Course09', phone='2564352352', url='http://127.0.0.1:8000/admin/courses',
           description='description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description CourseXX description Course description Course description Course description Course',
           about='about CourseXX about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course ',
           start_date='2019-07-05', created_at='2019-07-29 13:47:20.099848', updated_at='2019-07-29 13:48:34.690914',
           hascertification='1', status='1', views='4', category_id='5', qualification='3', slug='course09').save()
    Course(id='10', name='Course10', phone='4322452', url='http://127.0.0.1:8000/course/course_add',
           description='description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description CourseXX description Course description Course description Course description Course',
           about='about CourseXX about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course ',
           start_date='2020-08-19', image='courses/images/Course_10.png', created_at='2019-08-04 09:43:05.139746',
           updated_at='2019-08-04 10:25:22.795716', hascertification='1', status='1', views='7', category_id='1',
           qualification='0', slug='course10').save()
    Course(id='11', name='Course11', phone='234542', url='http://127.0.0.1:8000/course/',
           description='Course Description', about='Course About', start_date='2018-07-06',
           created_at='2019-08-04 09:46:57.063586', updated_at='2019-08-04 09:46:57.063586', hascertification='0',
           status='0', views='3', category_id='5', qualification='0', slug='course11').save()
    Course(id='12', name='Course12', phone='34252535', url='http://127.0.0.1:8000/course/course_add/',
           description='Course Description', about='Course About', start_date='2019-08-20',
           image='courses/images/Course_12.png', created_at='2019-08-04 09:55:39.188205',
           updated_at='2019-08-04 10:25:00.093396', hascertification='1', status='1', views='8', category_id='5',
           qualification='0', slug='course12').save()
    Course(id='13', name='Course13', phone='34222', url='http://127.0.0.1:8000/course/course_add',
           description='Course Description', about='Course About', start_date='2020-07-07',
           created_at='2019-08-04 14:02:05.036201', updated_at='2019-08-04 14:02:05.036201', hascertification='1',
           status='1', views='4', category_id='8', qualification='0', slug='course13').save()
    Course(id='14', name='Course14', phone='342242325', url='http://127.0.0.1:8000/course/',
           description='Course Description', about='Course About', start_date='2018-08-21',
           image='courses/images/Course_14.png', created_at='2019-08-05 09:29:34.383215',
           updated_at='2019-08-05 09:29:34.383215', hascertification='1', status='1', views='3', category_id='6',
           qualification='0', slug='course14').save()
    # Lesson
    Lesson(id='1',
           description='Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson ',
           number='1', release_date='2018-07-01', created_at='2019-08-01 14:34:54.175060',
           updated_at='2019-08-02 05:30:04.356337', course_id='2', name='Lesson05 C1').save()
    Lesson(id='2',
           description='Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson ',
           number='7', release_date='2018-08-15', created_at='2019-08-01 14:34:54.175060',
           updated_at='2019-08-01 14:34:54.175060', course_id='2', name='Lesson04 C1').save()
    Lesson(id='3',
           description='Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson ',
           number='6', release_date='2019-07-02', created_at='2019-08-01 14:34:54.175060',
           updated_at='2019-08-01 14:34:54.175060', course_id='2', name='Lesson03 C1').save()
    Lesson(id='4',
           description='Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson ',
           number='5', release_date='2018-08-16', created_at='2019-08-01 14:34:54.175060',
           updated_at='2019-08-01 14:34:54.175060', course_id='2', name='Lesson02 C1').save()
    Lesson(id='5',
           description='Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson ',
           number='4', release_date='2018-07-03', created_at='2019-08-01 14:34:54.175060',
           updated_at='2019-08-01 14:34:54.175060', course_id='2', name='Lesson10 C1').save()
    Lesson(id='6',
           description='Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson ',
           number='3', release_date='2020-08-17', created_at='2019-08-01 14:34:54.175060',
           updated_at='2019-08-01 14:34:54.175060', course_id='2', name='Lesson08 C1').save()
    Lesson(id='7',
           description='Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson ',
           number='2', release_date='2018-07-04', created_at='2019-08-01 14:34:54.175060',
           updated_at='2019-08-01 14:34:54.175060', course_id='2', name='Lesson07 C1').save()
    Lesson(id='8',
           description='Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson ',
           number='7', release_date='2018-08-18', created_at='2019-08-01 14:34:54.175060',
           updated_at='2019-08-01 14:34:54.175060', course_id='3', name='Lesson06 C2').save()
    Lesson(id='9',
           description='Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson ',
           number='6', release_date='2019-07-05', created_at='2019-08-01 14:34:54.175060',
           updated_at='2019-08-02 05:30:24.636899', course_id='3', name='Lesson05 C2').save()
    Lesson(id='10',
           description='Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson ',
           number='5', release_date='2018-07-01', created_at='2019-08-01 14:34:54.175060',
           updated_at='2019-08-01 14:34:54.175060', course_id='3', name='Lesson04 C2').save()
    Lesson(id='11',
           description='Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson ',
           number='4', release_date='2018-08-15', created_at='2019-08-01 14:34:54.175060',
           updated_at='2019-08-01 14:34:54.175060', course_id='4', name='Lesson03 C2').save()
    Lesson(id='12',
           description='Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson ',
           number='3', release_date='2019-07-02', created_at='2019-08-01 14:34:54.175060',
           updated_at='2019-08-01 14:34:54.175060', course_id='5', name='Lesson02 C2').save()
    Lesson(id='13',
           description='Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson ',
           number='2', release_date='2018-08-16', created_at='2019-08-01 14:34:54.175060',
           updated_at='2019-08-01 14:34:54.175060', course_id='6', name='Lesson01 C2').save()
    Lesson(id='14',
           description='Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson ',
           number='1', release_date='2018-07-03', created_at='2019-08-01 14:34:54.175060',
           updated_at='2019-08-01 14:34:54.175060', course_id='5', name='Lesson09 C2').save()
    Lesson(id='15',
           description='Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson ',
           number='9', release_date='2020-08-17', created_at='2019-08-01 14:34:54.175060',
           updated_at='2019-08-01 14:34:54.175060', course_id='7', name='Lesson07 C3').save()
    Lesson(id='16',
           description='Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson ',
           number='8', release_date='2018-07-04', created_at='2019-08-01 14:34:54.175060',
           updated_at='2019-08-01 14:34:54.175060', course_id='4', name='Lesson06 C3').save()
    Lesson(id='17',
           description='Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson ',
           number='7', release_date='2018-08-18', created_at='2019-08-01 14:34:54.175060',
           updated_at='2019-08-02 05:30:17.090284', course_id='5', name='Lesson05 C3').save()
    Lesson(id='18',
           description='Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson ',
           number='6', release_date='2019-07-05', created_at='2019-08-01 14:34:54.175060',
           updated_at='2019-08-01 14:34:54.175060', course_id='6', name='Lesson04 C3').save()
    Lesson(id='19',
           description='Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson ',
           number='5', release_date='2020-08-19', created_at='2019-08-01 14:34:54.175060',
           updated_at='2019-08-01 14:34:54.175060', course_id='7', name='Lesson09 C3').save()
    Lesson(id='20',
           description='Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson ',
           number='4', release_date='2018-07-06', created_at='2019-08-01 14:34:54.175060',
           updated_at='2019-08-01 14:34:54.175060', course_id='8', name='Lesson02 C3').save()
    Lesson(id='21',
           description='Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson ',
           number='3', release_date='2019-08-20', created_at='2019-08-01 14:34:54.175060',
           updated_at='2019-08-01 14:34:54.175060', course_id='8', name='Lesson01 C3').save()
    Lesson(id='23',
           description='Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson ',
           number='1', release_date='2020-07-07', created_at='2019-08-01 14:34:54.175060',
           updated_at='2019-08-02 05:30:32.985779', course_id='4', name='Lesson08 C3').save()
    Lesson(id='24',
           description='Description Lesson Description Lesson Description Lesson Description Lesson Description Lesson Description Lesson Description Lesson Description Lesson Description Lesson Description Lesson Description Lesson Description Lesson Description Lesson Description Lesson Description Lesson Description Lesson Description Lesson Description Lesson Description Lesson Description Lesson Description Lesson Description Lesson Description Lesson Description Lesson Description Lesson Description Lesson Description Lesson Description Lesson Description Lesson Description Lesson Description Lesson Description Lesson Description Lesson Description Lesson ',
           number='7', release_date='2018-08-21', created_at='2019-08-02 05:22:30.330215',
           updated_at='2019-08-02 05:22:30.330215', course_id='2', name='Lesson01 C1').save()
    # Material
    Material(id='1', file='Lessons/Materials/Video01.mp4', lesson_id='1', name='Material01V').save()
    Material(id='2', file='Lessons/Materials/Lesson01.json', lesson_id='5', name='Material02V').save()
    Material(id='3', file='Lessons/Materials/Lesson01.html', lesson_id='6', name='Material03T').save()
    Material(id='4', file='Lessons/Materials/Lesson01.html', lesson_id='3', name='Material04T').save()
    Material(id='5', embedded='Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto ', lesson_id='3', name='Material05V').save()
    Material(id='6', embedded='Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto ', lesson_id='2', name='Material06V').save()
    Material(id='7', file='Lessons/Materials/Lesson01.txt', lesson_id='1', name='Material07T').save()
    Material(id='8', file='Lessons/Materials/Lesson06.txt', lesson_id='5', name='Material08T').save()
    Material(id='9', file='Lessons/Materials/Lesson01.html', lesson_id='4', name='Material09T').save()
    Material(id='10', file='Lessons/Materials/Video01.mp4', lesson_id='4', name='Material10V').save()
    Material(id='11', file='Lessons/Materials/Video01.mp4', lesson_id='2', name='Material11V').save()
    Material(id='12', file='Lessons/Materials/Lesson01.json', lesson_id='6', name='Material12V').save()
    Material(id='13', embedded='Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto ', lesson_id='1', name='Material13T').save()
    Material(id='14', file='Lessons/Materials/Lesson01.json', lesson_id='2', name='Material14T').save()
    Material(id='15', embedded='Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto ', lesson_id='10', name='Material15 V').save()
    Material(id='16', embedded='Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto ', lesson_id='20', name='Material16').save()
    Material(id='17', file='lessons/materials/Lesson05.txt', lesson_id='10', name='Material17').save()
    Material(id='18', file='lessons/materials/Lesson05.txt', lesson_id='13', name='Material18').save()
    Material(id='19', file='lessons/materials/Lesson05.txt', lesson_id='20', name='Material19').save()
    Material(id='20', file='lessons/materials/Lesson06.txt', lesson_id='20', name='Material20').save()
    # Announcement
    Announcement(id='1', title='Advertisement Course06', content='Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course ', created_at='2019-07-31 15:04:19.556484', updated_at='2019-08-01 14:32:23.596700', course_id='2').save()
    Announcement(id='2', title='Advertisement Course03', content='Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course ', created_at='2019-07-31 15:20:11.283803', updated_at='2019-08-01 14:32:31.846414', course_id='4').save()
    Announcement(id='3', title='Advertisement Course02', content='Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course ', created_at='2019-07-31 15:21:09.594207', updated_at='2019-08-01 14:32:38.721183', course_id='3').save()
    Announcement(id='4', title='Advertisement Course04 ', content='Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course ', created_at='2019-07-31 15:23:35.328462', updated_at='2019-08-01 14:32:47.648123', course_id='5').save()
    Announcement(id='5', title='Advertisement Course05', content='Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course ', created_at='2019-07-31 15:27:33.715816', updated_at='2019-08-01 14:32:55.241615', course_id='6').save()
    Announcement(id='6', title='Advertisement Course01', content='Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course ', created_at='2019-07-31 15:29:52.653546', updated_at='2019-08-01 14:54:06.007688', course_id='2').save()
    Announcement(id='7', title='Advertisement 02', content='Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement ', created_at='2019-08-01 14:54:38.990939', updated_at='2019-08-01 14:54:38.990939', course_id='2').save()
    Announcement(id='8', title='Advertisement02 C4', content='Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement ', created_at='2019-08-01 14:55:12.161685', updated_at='2019-08-01 14:55:12.161685', course_id='5').save()
    Announcement(id='9', title='a', content='Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement ', created_at='2019-08-01 14:55:23.083186', updated_at='2019-08-01 14:55:23.083186', course_id='6').save()
    Announcement(id='10', title='d', content='Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement ', created_at='2019-08-01 14:55:30.739174', updated_at='2019-08-01 14:55:30.739174', course_id='4').save()
    Announcement(id='11', title='ert', content='Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement ', created_at='2019-08-01 14:55:41.379436', updated_at='2019-08-01 14:55:41.379436', course_id='5').save()
    Announcement(id='12', title='45wertrqe', content='Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement ', created_at='2019-08-01 14:55:50.644750', updated_at='2019-08-01 14:55:50.644750', course_id='3').save()
    Announcement(id='13', title='rwder', content='Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement ', created_at='2019-08-01 14:55:59.102959', updated_at='2019-08-01 14:55:59.102959', course_id='4').save()
    Announcement(id='14', title='qtweq', content='Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement ', created_at='2019-08-01 14:56:07.087064', updated_at='2019-08-01 14:56:07.087064', course_id='5').save()
    Announcement(id='15', title='sdagg', content='Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement ', created_at='2019-08-01 14:56:16.821109', updated_at='2019-08-01 14:56:16.821109', course_id='7').save()
    Announcement(id='16', title='sdfgsdf', content='Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement ', created_at='2019-08-01 14:56:25.180194', updated_at='2019-08-01 14:56:25.180194', course_id='8').save()
    Announcement(id='17', title='sadg', content='Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement ', created_at='2019-08-01 14:56:32.929934', updated_at='2019-08-01 14:56:32.929934', course_id='9').save()
    # User
    User(id='1', password='pbkdf2_sha256$20000$GDG2ExejLdID$+jZqG9jb9QQPASguwBlIxiWLH09h/DldlB5+SCvoa40=', last_login='2019-08-06 17:16:57.015753', is_superuser='1', email='admin@ocpplus.com', name='Admin', phone='900004674', is_active='1', is_staff='1', date_joined='2019-07-29 08:12:08.986190', username='admin').save()
    User(id='2', password='pbkdf2_sha256$20000$zqU1gSN1lM8L$qC1r5BL/5wWktffKMGXcu0P+URhxp9l6Y3ff05rUiMA=', last_login='2019-08-05 08:00:31.032668', is_superuser='0', email='user01@user.com', name='User01', phone='900004674', is_active='1', is_staff='0', date_joined='2019-07-31 09:01:57.362757', username='user01').save()
    User(id='3', password='pbkdf2_sha256$20000$nx0FkSP8DmTb$bBsSIR5Sr9flhp5E5QJNmbTuDMBBJlDsbkYJG/00Mc4=', last_login='2019-08-03 13:11:10.939870', is_superuser='0', email='teacher01@ocpplus.com', name='Teacher01', phone='900004674', is_active='1', is_staff='0', date_joined='2019-07-31 09:18:47.450824', username='teacher01').save()
    User(id='4', password='pbkdf2_sha256$20000$zqU1gSN1lM8L$qC1r5BL/5wWktffKMGXcu0P+URhxp9l6Y3ff05rUiMA=', last_login='2019-08-02 13:38:34.332377', is_superuser='0', email='user02@user.com', name='User02', phone='900004674', is_active='1', is_staff='0', date_joined='2019-07-31 15:43:39.712962', username='user02').save()
    User(id='10', password='pbkdf2_sha256$20000$zqU1gSN1lM8L$qC1r5BL/5wWktffKMGXcu0P+URhxp9l6Y3ff05rUiMA=', last_login='2019-07-31 15:43:40.228602', is_superuser='0', email='user03@user.com', name='User03', phone='900014181', is_active='1', is_staff='0', date_joined='2019-07-31 15:43:39.712962', username='user03').save()
    User(id='11', password='pbkdf2_sha256$20000$zqU1gSN1lM8L$qC1r5BL/5wWktffKMGXcu0P+URhxp9l6Y3ff05rUiMA=', last_login='2019-07-31 15:43:40.228602', is_superuser='0', email='user04@user.com', name='User04', phone='900004674', is_active='1', is_staff='0', date_joined='2019-07-31 15:43:39.712962', username='user04').save()
    User(id='12', password='pbkdf2_sha256$20000$zqU1gSN1lM8L$qC1r5BL/5wWktffKMGXcu0P+URhxp9l6Y3ff05rUiMA=', last_login='2019-07-31 15:43:40.228602', is_superuser='0', email='user05@user.com', name='User05', phone='900022380', is_active='1', is_staff='0', date_joined='2019-07-31 15:43:39.712962', username='user05').save()
    User(id='13', password='pbkdf2_sha256$20000$zqU1gSN1lM8L$qC1r5BL/5wWktffKMGXcu0P+URhxp9l6Y3ff05rUiMA=', last_login='2019-07-31 15:43:40.228602', is_superuser='0', email='user06@user.com', name='User06', phone='900030349', is_active='1', is_staff='0', date_joined='2019-07-31 15:43:39.712962', username='user06').save()
    User(id='14', password='pbkdf2_sha256$20000$zqU1gSN1lM8L$qC1r5BL/5wWktffKMGXcu0P+URhxp9l6Y3ff05rUiMA=', last_login='2019-07-31 15:43:40.228602', is_superuser='0', email='user07@user.com', name='User07', phone='900018698', is_active='1', is_staff='0', date_joined='2019-07-31 15:43:39.712962', username='user07').save()
    User(id='15', password='pbkdf2_sha256$20000$ymlpXTezDSCp$znXWxn3eHNUI9DvGYI9MakPpnTyt4rybrC0MC2P2WUE=', last_login='2019-07-31 15:43:40.228602', is_superuser='0', email='teacher02@ocpplus.com', name='teacher02', phone='900029467', is_active='1', is_staff='0', date_joined='2019-07-31 15:43:39.712962', username='teacher02').save()
    User(id='16', password='pbkdf2_sha256$20000$ymlpXTezDSCp$znXWxn3eHNUI9DvGYI9MakPpnTyt4rybrC0MC2P2WUE=', last_login='2019-07-31 15:43:40.228602', is_superuser='0', email='teacher03@ocpplus.com', name='teacher03', phone='900014781', is_active='1', is_staff='0', date_joined='2019-07-31 15:43:39.712962', username='teacher03').save()
    User(id='17', password='pbkdf2_sha256$20000$ymlpXTezDSCp$znXWxn3eHNUI9DvGYI9MakPpnTyt4rybrC0MC2P2WUE=', last_login='2019-07-31 15:43:40.228602', is_superuser='0', email='teacher04@ocpplus.com', name='teacher04', phone='900003986', is_active='1', is_staff='0', date_joined='2019-07-31 15:43:39.712962', username='teacher04').save()
    # Teacher
    Teacher(id='3', user_id='3').save()
    Teacher(id='4', user_id='15').save()
    Teacher(id='5', user_id='16').save()
    Teacher(id='6', user_id='17').save()
    # Teacher_courses
    teacher = Teacher.objects.get(pk='3')
    course = Course.objects.get(pk='2')
    teacher.course.add(course)
    teacher = Teacher.objects.get(pk='5')
    course = Course.objects.get(pk='8')
    teacher.course.add(course)
    teacher = Teacher.objects.get(pk='6')
    course = Course.objects.get(pk='2')
    teacher.course.add(course)
    teacher = Teacher.objects.get(pk='3')
    course = Course.objects.get(pk='10')
    teacher.course.add(course)
    teacher = Teacher.objects.get(pk='5')
    course = Course.objects.get(pk='9')
    teacher.course.add(course)
    teacher = Teacher.objects.get(pk='6')
    course = Course.objects.get(pk='12')
    teacher.course.add(course)
    teacher = Teacher.objects.get(pk='4')
    course = Course.objects.get(pk='4')
    teacher.course.add(course)
    teacher = Teacher.objects.get(pk='4')
    course = Course.objects.get(pk='5')
    teacher.course.add(course)
    teacher = Teacher.objects.get(pk='4')
    course = Course.objects.get(pk='8')
    teacher.course.add(course)
    teacher = Teacher.objects.get(pk='4')
    course = Course.objects.get(pk='9')
    teacher.course.add(course)
    teacher = Teacher.objects.get(pk='4')
    course = Course.objects.get(pk='6')
    teacher.course.add(course)
    # Comment
    Comment(id='1',
            comment='Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement ',
            created_at='2019-08-01 14:30:42.365773', updated_at='2019-08-01 14:30:42.365773', announcement_id='1',
            user_id='10').save()
    Comment(id='2',
            comment='Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement ',
            created_at='2019-08-01 14:57:05.303827', updated_at='2019-08-01 14:57:05.303827', announcement_id='17',
            user_id='4').save()
    Comment(id='3',
            comment='Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement ',
            created_at='2019-08-01 14:57:23.178218', updated_at='2019-08-01 14:57:23.178218', announcement_id='12',
            user_id='11').save()
    Comment(id='4',
            comment='Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement ',
            created_at='2019-08-01 14:57:31.912298', updated_at='2019-08-01 14:57:31.912298', announcement_id='15',
            user_id='12').save()
    Comment(id='5',
            comment='Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement ',
            created_at='2019-08-01 14:57:41.677589', updated_at='2019-08-01 14:57:41.677589', announcement_id='12',
            user_id='13').save()
    Comment(id='6',
            comment='Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement ',
            created_at='2019-08-01 14:57:51.396004', updated_at='2019-08-01 14:57:51.396004', announcement_id='7',
            user_id='4').save()
    Comment(id='7',
            comment='Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement ',
            created_at='2019-08-01 14:58:02.676874', updated_at='2019-08-01 14:58:02.676874', announcement_id='1',
            user_id='3').save()
    Comment(id='8',
            comment='Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement ',
            created_at='2019-08-01 14:58:13.129638', updated_at='2019-08-01 14:58:13.129638', announcement_id='4',
            user_id='11').save()
    Comment(id='9',
            comment='Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement ',
            created_at='2019-08-01 14:58:21.488733', updated_at='2019-08-01 14:58:21.488733', announcement_id='2',
            user_id='11').save()
    Comment(id='10',
            comment='Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement ',
            created_at='2019-08-01 14:58:29.754077', updated_at='2019-08-01 14:58:29.754077', announcement_id='1',
            user_id='10').save()
    Comment(id='11',
            comment='Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement ',
            created_at='2019-08-01 14:58:37.753798', updated_at='2019-08-01 14:58:37.753798', announcement_id='12',
            user_id='3').save()
    Comment(id='12',
            comment='Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement ',
            created_at='2019-08-01 14:58:46.019145', updated_at='2019-08-01 14:58:46.019145', announcement_id='15',
            user_id='2').save()
    Comment(id='13',
            comment='Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement ',
            created_at='2019-08-01 14:58:54.721971', updated_at='2019-08-01 14:59:01.055154', announcement_id='9',
            user_id='2').save()
    Comment(id='14',
            comment='Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement ',
            created_at='2019-08-01 14:59:09.351747', updated_at='2019-08-01 14:59:09.351747', announcement_id='10',
            user_id='11').save()
    Comment(id='15',
            comment='Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement ',
            created_at='2019-08-01 14:59:17.351472', updated_at='2019-08-01 14:59:17.351472', announcement_id='10',
            user_id='3').save()
    Comment(id='16',
            comment='Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement ',
            created_at='2019-08-01 14:59:26.226170', updated_at='2019-08-01 14:59:26.226170', announcement_id='15',
            user_id='2').save()
    Comment(id='17',
            comment='Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement ',
            created_at='2019-08-01 14:59:36.975803', updated_at='2019-08-01 14:59:36.975803', announcement_id='6',
            user_id='11').save()
    Comment(id='18',
            comment='Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement ',
            created_at='2019-08-01 14:59:45.788004', updated_at='2019-08-01 14:59:45.788004', announcement_id='6',
            user_id='13').save()
    Comment(id='19',
            comment='Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement ',
            created_at='2019-08-01 14:59:56.881372', updated_at='2019-08-01 14:59:56.881372', announcement_id='6',
            user_id='14').save()
    Comment(id='20',
            comment='Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement ',
            created_at='2019-08-01 15:00:09.052831', updated_at='2019-08-01 15:00:09.052831', announcement_id='6',
            user_id='16').save()
    Comment(id='21',
            comment='Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement ',
            created_at='2019-08-01 15:00:21.896148', updated_at='2019-08-01 15:00:21.896148', announcement_id='2',
            user_id='10').save()
    # Enrollment
    Enrollment(id='4', status='1', created_at='2019-07-31 12:06:13.569597', updated_at='2019-08-01 14:34:14.285794',
               course_id='2', user_id='14').save()
    Enrollment(id='5', status='1', created_at='2019-07-31 15:35:29.214550', updated_at='2019-08-01 14:34:06.692305',
               course_id='3', user_id='4').save()
    Enrollment(id='6', status='1', created_at='2019-07-31 15:36:29.681131', updated_at='2019-08-01 14:34:01.254991',
               course_id='5', user_id='4').save()
    Enrollment(id='7', status='1', created_at='2019-07-31 18:44:03.716743', updated_at='2019-08-01 14:33:52.880277',
               course_id='2', user_id='11').save()
    Enrollment(id='8', status='1', created_at='2019-08-02 05:19:22.597044', updated_at='2019-08-02 05:19:22.597044',
               course_id='2', user_id='2').save()
    Enrollment(id='9', status='1', created_at='2019-08-03 14:16:25.162438', updated_at='2019-08-03 14:16:25.162438',
               course_id='2', user_id='1').save()
    Enrollment(id='13', status='1', created_at='2019-08-05 16:14:23.470757', updated_at='2019-08-05 16:14:23.470757',
               course_id='7', user_id='1').save()
    # Thread
    Thread(id='1', title='Forum01', slug='forum01',
           body='Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum ',
           answers='5', created='2019-07-29 10:14:15.311377', modified='2019-08-05 08:13:43.142206', author_id='2',
           views='15').save()
    Thread(id='2', title='Forum06', slug='forum06',
           body='Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum ',
           answers='1', created='2019-07-29 10:14:15.311377', modified='2019-08-01 14:52:16.756149', author_id='4',
           views='3').save()
    Thread(id='3', title='Forum05', slug='forum05',
           body='Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum ',
           answers='1', created='2019-07-29 10:14:15.311377', modified='2019-08-01 14:53:41.211658', author_id='2',
           views='9').save()
    Thread(id='4', title='Forum04', slug='forum04',
           body='Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum ',
           answers='3', created='2019-07-29 10:14:15.311377', modified='2019-08-01 14:53:29.680805', author_id='1',
           views='5').save()
    Thread(id='5', title='Forum03', slug='forum03',
           body='Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum ',
           answers='1', created='2019-07-29 10:14:15.311377', modified='2019-08-05 07:40:59.867738', author_id='4',
           views='9').save()
    Thread(id='6', title='Forum02', slug='forum02',
           body='Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum ',
           answers='2', created='2019-07-29 10:14:15.311377', modified='2019-08-01 14:53:08.806515', author_id='2',
           views='1').save()
    Thread(id='7', title='Forum08', slug='forum08',
           body='Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum ',
           answers='0', created='2019-07-29 10:14:15.311377', modified='2019-08-04 13:34:01.029358', author_id='2',
           views='15').save()
    Thread(id='8', title='Forum07', slug='forum07',
           body='Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum ',
           answers='0', created='2019-07-29 10:14:15.311377', modified='2019-08-01 14:52:16.756149', author_id='4',
           views='2').save()
    Thread(id='9', title='Forum09', slug='forum09',
           body='Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum ',
           answers='0', created='2019-07-29 10:14:15.311377', modified='2019-08-01 14:53:41.211658', author_id='2',
           views='7').save()
    Thread(id='10', title='Forum10', slug='forum10',
           body='Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum ',
           answers='0', created='2019-07-29 10:14:15.311377', modified='2019-08-01 14:53:29.680805', author_id='1',
           views='3').save()
    Thread(id='11', title='Forum11', slug='forum11',
           body='Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum ',
           answers='0', created='2019-07-29 10:14:15.311377', modified='2019-07-31 18:47:29.094846', author_id='4',
           views='4').save()
    Thread(id='12', title='Forum12', slug='forum12',
           body='Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum ',
           answers='0', created='2019-07-29 10:14:15.311377', modified='2019-08-06 14:33:53.326895', author_id='2',
           views='4').save()
    # Reply
    Reply(id='1',
          reply='Answer01 Forum01 Answer01 Forum01 Answer01 Forum01 Answer01 Forum01 Answer01 Forum01 Answer01 Forum01 Answer01 Forum01 Answer01 Forum01 Answer01 Forum01 Answer01 Forum01 Answer01 Forum01 ',
          correct='1', created='2019-07-29 10:14:59.997269', modified='2019-07-29 10:14:59.997269', author_id='1',
          thread_id='1').save()
    Reply(id='2',
          reply='Answer02 Forum01 Answer02 Forum01 Answer02 Forum01 Answer02 Forum01 Answer02 Forum01 Answer02 Forum01 Answer02 Forum01 Answer02 Forum01 Answer02 Forum01 Answer02 Forum01 Answer02 Forum01 Answer02 Forum01 Answer02 Forum01 Answer02 Forum01 Answer02 Forum01 Answer02 Forum01 Answer02 Forum01 Answer02 Forum01 Answer02 Forum01 Answer02 Forum01 Answer02 Forum01 Answer02 Forum01 Answer02 Forum01 Answer02 Forum01 Answer02 Forum01 Answer02 Forum01 Answer02 Forum01 Answer02 Forum01 Answer02 Forum01 Answer02 Forum01 Answer02 Forum01 Answer02 Forum01 ',
          correct='0', created='2019-07-31 12:06:55.025128', modified='2019-07-31 12:06:55.025128', author_id='1',
          thread_id='1').save()
    Reply(id='3',
          reply='Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum ',
          correct='0', created='2019-08-01 14:52:04.678433', modified='2019-08-01 14:52:04.678433', author_id='10',
          thread_id='1').save()
    Reply(id='4',
          reply='Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum ',
          correct='0', created='2019-08-01 14:52:16.756149', modified='2019-08-01 14:52:16.756149', author_id='12',
          thread_id='2').save()
    Reply(id='5',
          reply='Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum ',
          correct='0', created='2019-08-01 14:52:27.630776', modified='2019-08-01 14:52:27.630776', author_id='14',
          thread_id='1').save()
    Reply(id='6',
          reply='Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum ',
          correct='0', created='2019-08-01 14:52:39.520998', modified='2019-08-01 14:52:39.520998', author_id='14',
          thread_id='4').save()
    Reply(id='7',
          reply='Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum ',
          correct='0', created='2019-08-01 14:52:50.317505', modified='2019-08-01 14:52:50.317505', author_id='10',
          thread_id='6').save()
    Reply(id='8',
          reply='Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum ',
          correct='0', created='2019-08-01 14:53:00.041187', modified='2019-08-01 14:53:00.041187', author_id='13',
          thread_id='4').save()
    Reply(id='9',
          reply='Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum ',
          correct='0', created='2019-08-01 14:53:08.806515', modified='2019-08-01 14:53:08.806515', author_id='14',
          thread_id='6').save()
    Reply(id='10',
          reply='Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum ',
          correct='0', created='2019-08-01 14:53:18.384310', modified='2019-08-01 14:53:18.384310', author_id='14',
          thread_id='1').save()
    Reply(id='11',
          reply='Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum ',
          correct='0', created='2019-08-01 14:53:29.680805', modified='2019-08-01 14:53:29.680805', author_id='10',
          thread_id='4').save()
    Reply(id='12',
          reply='Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum ',
          correct='0', created='2019-08-01 14:53:41.196034', modified='2019-08-01 14:53:41.196034', author_id='4',
          thread_id='3').save()
    Reply(id='13',
          reply='Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum ',
          correct='0', created='2019-08-05 07:40:59.383344', modified='2019-08-05 07:40:59.383344', author_id='1',
          thread_id='5').save()
    # Tag
    Tag(id='1', name='Tag01', slug='tag01').save()
    Tag(id='2', name='TagNew', slug='tagnew').save()
    Tag(id='3', name='Tag12', slug='tag12').save()
    Tag(id='4', name='Tag05', slug='tag05').save()
    Tag(id='5', name='Tag07', slug='tag07').save()
    Tag(id='6', name='TagOld', slug='tagold').save()
    Tag(id='7', name='Tag10', slug='tag10').save()
    # Taggeditem
    TaggedItem(id='2', object_id='12', content_type_id='19', tag_id='2').save()
    TaggedItem(id='3', object_id='12', content_type_id='19', tag_id='3').save()
    TaggedItem(id='4', object_id='1', content_type_id='19', tag_id='1').save()
    TaggedItem(id='5', object_id='1', content_type_id='19', tag_id='2').save()
    TaggedItem(id='6', object_id='3', content_type_id='19', tag_id='2').save()
    TaggedItem(id='7', object_id='3', content_type_id='19', tag_id='4').save()
    TaggedItem(id='8', object_id='8', content_type_id='19', tag_id='5').save()
    TaggedItem(id='9', object_id='10', content_type_id='19', tag_id='6').save()
    TaggedItem(id='10', object_id='10', content_type_id='19', tag_id='7').save()
    TaggedItem(id='11', object_id='2', content_type_id='19', tag_id='6').save()
    TaggedItem(id='12', object_id='11', content_type_id='19', tag_id='6').save()
    TaggedItem(id='13', object_id='7', content_type_id='19', tag_id='6').save()


# Start execution here!
if __name__ == '__main__':
    print("Starting course population script...")
    populate()
