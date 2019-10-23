import os
from decouple import config

os.environ.setdefault('DJANGO_SETTINGS_MODULE', config('SETTINGS_MODULE_PATH'))

import django
django.setup()

from ocp.accounts.models import User
from ocp.courses.models import Category, Course, Lesson, Material, Announcement, Teacher, Comment, Enrollment, CourseUpload
from ocp.forum.models import Thread, Reply
from taggit.models import Tag, TaggedItem

def populate():
    print("\nStarted process ...")

    # # ############################ Delete all tables
    print("Step 1/2: Delete table's content ...")
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
    CourseUpload.objects.all().delete()
    Course.objects.all().delete()
    Category.objects.all().delete()


    load = True
    if load:
        print("Step 2/2: Starting course population process ", end="")
        # ############################ Start creates

        print(".", end="")
        # User (12)
        User(password='pbkdf2_sha256$20000$GDG2ExejLdID$+jZqG9jb9QQPASguwBlIxiWLH09h/DldlB5+SCvoa40=',
             last_login='2019-08-06 17:16:57.015753', is_superuser='1', email='admin@ocpplus.com', name='Admin',
             phone='900004674', is_active='1', is_staff='1', date_joined='2019-07-29 08:12:08.986190',
             username='admin').save()
        User(password='pbkdf2_sha256$20000$zqU1gSN1lM8L$qC1r5BL/5wWktffKMGXcu0P+URhxp9l6Y3ff05rUiMA=',
             last_login='2019-08-05 08:00:31.032668', is_superuser='0', email='user01@user.com', name='User01',
             phone='900004674', is_active='1', is_staff='0', date_joined='2019-07-31 09:01:57.362757',
             username='user01').save()
        User(password='pbkdf2_sha256$20000$nx0FkSP8DmTb$bBsSIR5Sr9flhp5E5QJNmbTuDMBBJlDsbkYJG/00Mc4=',
             last_login='2019-08-03 13:11:10.939870', is_superuser='0', email='teacher01@ocpplus.com', name='Teacher01',
             phone='900004674', is_active='1', is_staff='0', date_joined='2019-07-31 09:18:47.450824',
             username='teacher01').save()
        User(password='pbkdf2_sha256$20000$zqU1gSN1lM8L$qC1r5BL/5wWktffKMGXcu0P+URhxp9l6Y3ff05rUiMA=',
             last_login='2019-08-02 13:38:34.332377', is_superuser='0', email='user02@user.com', name='User02',
             phone='900004674', is_active='1', is_staff='0', date_joined='2019-07-31 15:43:39.712962',
             username='user02').save()
        User(password='pbkdf2_sha256$20000$zqU1gSN1lM8L$qC1r5BL/5wWktffKMGXcu0P+URhxp9l6Y3ff05rUiMA=',
             last_login='2019-07-31 15:43:40.228602', is_superuser='0', email='user03@user.com', name='User03',
             phone='900014181', is_active='1', is_staff='0', date_joined='2019-07-31 15:43:39.712962',
             username='user03').save()
        User(password='pbkdf2_sha256$20000$zqU1gSN1lM8L$qC1r5BL/5wWktffKMGXcu0P+URhxp9l6Y3ff05rUiMA=',
             last_login='2019-07-31 15:43:40.228602', is_superuser='0', email='user04@user.com', name='User04',
             phone='900004674', is_active='1', is_staff='0', date_joined='2019-07-31 15:43:39.712962',
             username='user04').save()
        User(password='pbkdf2_sha256$20000$zqU1gSN1lM8L$qC1r5BL/5wWktffKMGXcu0P+URhxp9l6Y3ff05rUiMA=',
             last_login='2019-07-31 15:43:40.228602', is_superuser='0', email='user05@user.com', name='User05',
             phone='900022380', is_active='1', is_staff='0', date_joined='2019-07-31 15:43:39.712962',
             username='user05').save()
        User(password='pbkdf2_sha256$20000$zqU1gSN1lM8L$qC1r5BL/5wWktffKMGXcu0P+URhxp9l6Y3ff05rUiMA=',
             last_login='2019-07-31 15:43:40.228602', is_superuser='0', email='user06@user.com', name='User06',
             phone='900030349', is_active='1', is_staff='0', date_joined='2019-07-31 15:43:39.712962',
             username='user06').save()
        User(password='pbkdf2_sha256$20000$zqU1gSN1lM8L$qC1r5BL/5wWktffKMGXcu0P+URhxp9l6Y3ff05rUiMA=',
             last_login='2019-07-31 15:43:40.228602', is_superuser='0', email='user07@user.com', name='User07',
             phone='900018698', is_active='1', is_staff='0', date_joined='2019-07-31 15:43:39.712962',
             username='user07').save()
        User(password='pbkdf2_sha256$20000$ymlpXTezDSCp$znXWxn3eHNUI9DvGYI9MakPpnTyt4rybrC0MC2P2WUE=',
             last_login='2019-07-31 15:43:40.228602', is_superuser='0', email='teacher02@ocpplus.com', name='teacher02',
             phone='900029467', is_active='1', is_staff='0', date_joined='2019-07-31 15:43:39.712962',
             username='teacher02').save()
        User(password='pbkdf2_sha256$20000$ymlpXTezDSCp$znXWxn3eHNUI9DvGYI9MakPpnTyt4rybrC0MC2P2WUE=',
             last_login='2019-07-31 15:43:40.228602', is_superuser='0', email='teacher03@ocpplus.com', name='teacher03',
             phone='900014781', is_active='1', is_staff='0', date_joined='2019-07-31 15:43:39.712962',
             username='teacher03').save()
        User(password='pbkdf2_sha256$20000$ymlpXTezDSCp$znXWxn3eHNUI9DvGYI9MakPpnTyt4rybrC0MC2P2WUE=',
             last_login='2019-07-31 15:43:40.228602', is_superuser='0', email='teacher04@ocpplus.com', name='teacher04',
             phone='900003986', is_active='1', is_staff='0', date_joined='2019-07-31 15:43:39.712962',
             username='teacher04').save()

        print(".", end="")
        # Category (3)
        Category(name='Category01', description='Description Category01', slug='category01', status='1').save()
        Category(name='Category02', description='Description Category02', slug='category02', status='1').save()
        Category(name='Category03', description='Description Category03', slug='category03', status='1').save()

        print(".", end="")
        # Course (6)
        Course(name='Course01', phone='34444444', url='http://127.0.0.1:8000/admin/courses',
               description='description Course01 description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course ',
               about='about Course01 about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course ',
               start_date='2018-07-01', image='courses/images/Course_1.png', hascertification='1', status='1',
               views='1', category_id='1', qualification='0', slug='course01').save()
        Course(name='Course02', phone='4236423624', url='http://127.0.0.1:8000/admin/courses',
               description='description Course02 description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course',
               about='about Course02 about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course ',
               start_date='2018-08-15', hascertification='1', status='1', views='2', category_id='1',
               qualification='20', slug='course02').save()
        Course(name='Course03', phone='5341345123', url='http://127.0.0.1:8000/admin/courses',
               description='description Course03 description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course',
               about='about Course03 about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course ',
               start_date='2019-07-02', image='courses/images/Course_3.png', hascertification='1', status='1',
               views='7', category_id='1', qualification='15', slug='course03').save()
        Course(name='Course04', phone='4232323523', url='http://127.0.0.1:8000/admin/courses',
               description='description Course04 description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course',
               about='about Course04 about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course ',
               start_date='2018-08-16', hascertification='1', status='1', views='4', category_id='2',
               qualification='12', slug='course04').save()
        Course(name='Course05', phone='2564352352', url='http://127.0.0.1:8000/admin/courses',
               description='description Course05 description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course',
               about='about Course05 about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course ',
               start_date='2018-07-03', hascertification='1', status='1', views='8', category_id='2',
               qualification='19', slug='course05').save()
        Course(name='Course06', phone='2564352352', url='http://127.0.0.1:8000/admin/courses',
               description='description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description CourseXX description Course description Course description Course description Course',
               about='about CourseXX about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course ',
               start_date='2019-09-17', image='courses/images/Course_6.png', hascertification='1', status='1',
               views='6', category_id='3', qualification='6', slug='course06').save()
        Course(name='Course07', phone='2564352352', url='http://127.0.0.1:8000/admin/courses',
               description='description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description Course description CourseXX description Course description Course description Course description Course',
               about='about CourseXX about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course about Course ',
               start_date='2019-09-17', image='courses/images/Course_7.png',hascertification='1', status='1',
               views='6', category_id='3', qualification='6', slug='course07').save()

        print(".", end="")
        # Lesson (6)
        Lesson(description='Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson ',
               number='1', release_date='2018-07-01', course_id='1', name='Lesson01').save()
        Lesson(description='Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson ',
               number='1', release_date='2018-08-15', course_id='2', name='Lesson02').save()
        Lesson(description='Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson ',
               number='1', release_date='2019-07-02', course_id='3', name='Lesson03').save()
        Lesson(description='Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson ',
               number='1', release_date='2018-08-16', course_id='4', name='Lesson04').save()
        Lesson(description='Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson ',
               number='1', release_date='2018-07-03', course_id='5', name='Lesson05').save()
        Lesson(description='Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson ',
               number='1', release_date='2020-08-17', course_id='6', name='Lesson06').save()
        Lesson(description='Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson ',
               number='1', release_date='2018-07-01', course_id='1', name='Lesson07').save()
        Lesson(description='Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson ',
               number='1', release_date='2018-08-15', course_id='2', name='Lesson08').save()
        Lesson(description='Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson ',
               number='1', release_date='2019-07-02', course_id='3', name='Lesson09').save()
        Lesson(description='Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson ',
               number='1', release_date='2018-08-16', course_id='4', name='Lesson10').save()
        Lesson(description='Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson ',
               number='1', release_date='2018-07-03', course_id='5', name='Lesson11').save()
        Lesson(description='Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson Lesson ',
               number='1', release_date='2020-08-17', course_id='6', name='Lesson12').save()

        print(".", end="")
        # Material
        Material(file='Lessons/Materials/Video01.mp4', lesson_id='1', name='Material01V').save()
        Material(file='Lessons/Materials/Lesson01.json', lesson_id='5', name='Material02V').save()
        Material(file='Lessons/Materials/Lesson01.html', lesson_id='6', name='Material03T').save()
        Material(file='Lessons/Materials/Lesson01.html', lesson_id='3', name='Material04T').save()
        Material(embedded='Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto ', lesson_id='3', name='Material05V').save()
        Material(embedded='Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto ', lesson_id='2', name='Material06V').save()
        Material(file='Lessons/Materials/Lesson01.txt', lesson_id='1', name='Material07T').save()
        Material(file='Lessons/Materials/Lesson06.txt', lesson_id='5', name='Material08T').save()
        Material(file='Lessons/Materials/Lesson01.html', lesson_id='4', name='Material09T').save()
        Material(file='Lessons/Materials/Video01.mp4', lesson_id='4', name='Material10V').save()
        Material(file='Lessons/Materials/Video01.mp4', lesson_id='2', name='Material11V').save()

        print(".", end="")
        # Announcement (11)
        Announcement(title='Notice 01', content='Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course Content Title Course ', course_id='1').save()
        Announcement(title='Advertisement 02', content='Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course ', course_id='2').save()
        Announcement(title='Notice 03', content='Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course ', course_id='3').save()
        Announcement(title='Advertisement 04 ', content='Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course ', course_id='4').save()
        Announcement(title='Notice 05', content='Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course ', course_id='5').save()
        Announcement(title='Advertisement 06', content='Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course Content Course ', course_id='6').save()
        Announcement(title='Notice 07', content='Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement ', course_id='1').save()
        Announcement(title='Advertisement 08', content='Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement ', course_id='2').save()
        Announcement(title='Notice 09', content='Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement ', course_id='3').save()
        Announcement(title='Advertisement 10', content='Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement ', course_id='4').save()
        Announcement(title='Notice 11', content='Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement ', course_id='5').save()

        print(".", end="")
        # Comment
        Comment(comment='Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement ',
             announcement_id='1', user_id='10').save()
        Comment(
            comment='Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement ',
             announcement_id='2', user_id='4').save()
        Comment(
            comment='Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement ',
             announcement_id='3', user_id='11').save()
        Comment(
            comment='Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement ',
              announcement_id='4', user_id='12').save()
        Comment(
            comment='Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement ',
              announcement_id='5', user_id='1').save()
        Comment(
            comment='Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement ',
             announcement_id='6', user_id='2').save()
        Comment(
            comment='Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement ',
            announcement_id='7', user_id='3').save()
        Comment(
            comment='Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement ',
             announcement_id='8', user_id='4').save()
        Comment(
            comment='Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement ',
             announcement_id='9', user_id='5').save()
        Comment(
            comment='Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement ',
             announcement_id='10', user_id='6').save()
        Comment(
            comment='Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement ',
             announcement_id='1', user_id='7').save()
        Comment(
            comment='Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement ',
             announcement_id='2', user_id='8').save()
        Comment(
            comment='Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement ',
             announcement_id='3', user_id='9').save()
        Comment(
            comment='Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement ',
             announcement_id='4', user_id='10').save()
        Comment(
            comment='Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement ',
             announcement_id='5', user_id='11').save()
        Comment(
            comment='Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement ',
             announcement_id='6', user_id='2').save()
        Comment(
            comment='Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement ',
             announcement_id='7', user_id='3').save()
        Comment(
            comment='Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement ',
             announcement_id='8', user_id='3').save()
        Comment(
            comment='Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement ',
             announcement_id='9', user_id='3').save()
        Comment(
            comment='Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement ',
             announcement_id='10', user_id='3').save()
        Comment(
            comment='Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement ',
             announcement_id='7', user_id='4').save()
        Comment(
            comment='Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement ',
             announcement_id='7', user_id='5').save()
        Comment(
            comment='Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement Coment Advertisement ',
             announcement_id='7', user_id='6').save()

        print(".", end="")
        # Teacher
        Teacher(user_id='3').save()
        Teacher(user_id='10').save()
        Teacher(user_id='11').save()
        Teacher(user_id='12').save()

        print(".", end="")
        # Teacher_courses
        teacher = Teacher.objects.get(pk='1')
        course = Course.objects.get(pk='2')
        teacher.course.add(course)
        teacher = Teacher.objects.get(pk='2')
        course = Course.objects.get(pk='6')
        teacher.course.add(course)
        teacher = Teacher.objects.get(pk='3')
        course = Course.objects.get(pk='2')
        teacher.course.add(course)
        teacher = Teacher.objects.get(pk='4')
        course = Course.objects.get(pk='4')
        teacher.course.add(course)
        teacher = Teacher.objects.get(pk='1')
        course = Course.objects.get(pk='3')
        teacher.course.add(course)
        teacher = Teacher.objects.get(pk='2')
        course = Course.objects.get(pk='1')
        teacher.course.add(course)
        teacher = Teacher.objects.get(pk='3')
        course = Course.objects.get(pk='1')
        teacher.course.add(course)
        teacher = Teacher.objects.get(pk='4')
        course = Course.objects.get(pk='5')
        teacher.course.add(course)
        teacher = Teacher.objects.get(pk='1')
        course = Course.objects.get(pk='6')
        teacher.course.add(course)
        teacher = Teacher.objects.get(pk='2')
        course = Course.objects.get(pk='5')
        teacher.course.add(course)
        teacher = Teacher.objects.get(pk='3')
        course = Course.objects.get(pk='4')
        teacher.course.add(course)

        print(".", end="")
        # Enrollment (7)
        Enrollment(status='1', course_id='1',user_id='11').save()
        Enrollment(status='1', course_id='2', user_id='4').save()
        Enrollment(status='1', course_id='3', user_id='4').save()
        Enrollment(status='1', course_id='3', user_id='11').save()
        Enrollment(status='1', course_id='5', user_id='2').save()
        Enrollment(status='1', course_id='5', user_id='1').save()

        print(".", end="")
        # Thread (12)
        Thread(title='Forum01', slug='forum01',
               body='Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum ',
               answers='2', author_id='2', views='15').save()
        Thread(title='Forum02', slug='forum02',
               body='Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum ',
               answers='2', author_id='4', views='3').save()
        Thread(title='Forum03', slug='forum03',
               body='Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum ',
               answers='2', author_id='2', views='9').save()
        Thread(title='Forum04', slug='forum04',
               body='Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum ',
               answers='2', author_id='1', views='5').save()
        Thread(title='Forum05', slug='forum05',
               body='Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum ',
               answers='5', author_id='4', views='9').save()
        Thread(title='Forum06', slug='forum06',
               body='Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum ',
               answers='2', author_id='2', views='1').save()
        Thread(title='Forum07', slug='forum07',
               body='Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum ',
               answers='2', author_id='2', views='15').save()
        Thread(title='Forum08', slug='forum08',
               body='Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum ',
               answers='2', author_id='4', views='2').save()
        Thread(title='Forum09', slug='forum09',
               body='Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum ',
               answers='2', author_id='2', views='7').save()
        Thread(title='Forum10', slug='forum10',
               body='Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum ',
               answers='0', author_id='1', views='3').save()
        Thread(title='Forum11', slug='forum11',
               body='Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum ',
               answers='0', author_id='4', views='4').save()
        Thread(title='Forum12', slug='forum12',
               body='Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum ',
               answers='0', author_id='2', views='4').save()

        print(".", end="")
        # Reply
        Reply(reply='Answer01 Forum01 Answer01 Forum01 Answer01 Forum01 Answer01 Forum01 Answer01 Forum01 Answer01 Forum01 Answer01 Forum01 Answer01 Forum01 Answer01 Forum01 Answer01 Forum01 Answer01 Forum01 ',
              correct='1', author_id='1', thread_id='1').save()
        Reply(reply='Answer02 Forum01 Answer02 Forum01 Answer02 Forum01 Answer02 Forum01 Answer02 Forum01 Answer02 Forum01 Answer02 Forum01 Answer02 Forum01 Answer02 Forum01 Answer02 Forum01 Answer02 Forum01 Answer02 Forum01 Answer02 Forum01 Answer02 Forum01 Answer02 Forum01 Answer02 Forum01 Answer02 Forum01 Answer02 Forum01 Answer02 Forum01 Answer02 Forum01 Answer02 Forum01 Answer02 Forum01 Answer02 Forum01 Answer02 Forum01 Answer02 Forum01 Answer02 Forum01 Answer02 Forum01 Answer02 Forum01 Answer02 Forum01 Answer02 Forum01 Answer02 Forum01 Answer02 Forum01 ',
              correct='0', author_id='1', thread_id='2').save()
        Reply(reply='Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum ',
              correct='0', author_id='10', thread_id='3').save()
        Reply(reply='Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum ',
              correct='0', author_id='11', thread_id='4').save()
        Reply(reply='Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum ',
              correct='0', author_id='12', thread_id='5').save()
        Reply(reply='Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum ',
              correct='0', author_id='11', thread_id='6').save()
        Reply(reply='Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum ',
              correct='0', author_id='10', thread_id='7').save()
        Reply(reply='Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum ',
              correct='0', author_id='12', thread_id='8').save()
        Reply(reply='Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum ',
              correct='0', author_id='11', thread_id='9').save()
        Reply(reply='Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum ',
              correct='0', author_id='12', thread_id='1').save()
        Reply(reply='Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum ',
              correct='0', author_id='10', thread_id='2').save()
        Reply(reply='Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum Answer Forum ',
              correct='0', author_id='4', thread_id='3').save()
        Reply(reply='Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum ',
              correct='0', author_id='1', thread_id='4').save()
        Reply(reply='Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum ',
              correct='0', author_id='1', thread_id='5').save()
        Reply(reply='Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum ',
              correct='0', author_id='1', thread_id='6').save()
        Reply(reply='Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum ',
              correct='0', author_id='1', thread_id='7').save()
        Reply(reply='Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum ',
              correct='0', author_id='1', thread_id='8').save()
        Reply(reply='Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum ',
              correct='0', author_id='1', thread_id='9').save()
        Reply(reply='Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum ',
              correct='0', author_id='1', thread_id='5').save()
        Reply(reply='Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum ',
              correct='0', author_id='2', thread_id='5').save()
        Reply(reply='Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum Message Forum ',
              correct='0', author_id='3', thread_id='5').save()

        print(".", end="")
        # Tag (7)
        Tag(name='Tag01', slug='tag01').save()
        Tag(name='Tag02', slug='tag02').save()
        Tag(name='Tag03', slug='tag03').save()
        Tag(name='Tag04', slug='tag04').save()
        Tag(name='Tag05', slug='tag05').save()
        Tag(name='Tag06', slug='tag06').save()
        Tag(name='Tag07', slug='tag07').save()

        print(".", end="")
        # Taggeditem (12)
        TaggedItem(object_id='1', content_type_id='1', tag_id='1').save()
        TaggedItem(object_id='1', content_type_id='1', tag_id='2').save()
        TaggedItem(object_id='1', content_type_id='1', tag_id='3').save()
        TaggedItem(object_id='2', content_type_id='1', tag_id='4').save()
        TaggedItem(object_id='2', content_type_id='1', tag_id='5').save()
        TaggedItem(object_id='2', content_type_id='1', tag_id='6').save()
        TaggedItem(object_id='3', content_type_id='2', tag_id='7').save()
        TaggedItem(object_id='3', content_type_id='2', tag_id='1').save()
        TaggedItem(object_id='3', content_type_id='2', tag_id='2').save()
        TaggedItem(object_id='4', content_type_id='2', tag_id='3').save()
        TaggedItem(object_id='5', content_type_id='2', tag_id='4').save()
        TaggedItem(object_id='6', content_type_id='2', tag_id='5').save()

    print("\nFinished process ...")


# Start execution here!
if __name__ == '__main__':
    populate()
