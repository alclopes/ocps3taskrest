from django.test import Client, TestCase
from .models import User

class AccountsTestCase(TestCase):

    def setUp(self):

        User(id='1', password='pbkdf2_sha256$20000$GDG2ExejLdID$+jZqG9jb9QQPASguwBlIxiWLH09h/DldlB5+SCvoa40=',
             last_login='2019-08-06 17:16:57.015753', is_superuser='1', email='admin@ocpplus.com', name='Admin',
             phone='900004674', is_active='1', is_staff='1', date_joined='2019-07-29 08:12:08.986190',
             username='admin').save()
        User(id='2', password='pbkdf2_sha256$20000$zqU1gSN1lM8L$qC1r5BL/5wWktffKMGXcu0P+URhxp9l6Y3ff05rUiMA=',
             last_login='2019-08-05 08:00:31.032668', is_superuser='0', email='user01@user.com', name='User01',
             phone='900004674', is_active='1', is_staff='0', date_joined='2019-07-31 09:01:57.362757',
             username='user01').save()
        User(id='3', password='pbkdf2_sha256$20000$nx0FkSP8DmTb$bBsSIR5Sr9flhp5E5QJNmbTuDMBBJlDsbkYJG/00Mc4=',
             last_login='2019-08-03 13:11:10.939870', is_superuser='0', email='teacher01@ocpplus.com', name='Teacher01',
             phone='900004674', is_active='1', is_staff='0', date_joined='2019-07-31 09:18:47.450824',
             username='teacher01').save()

        self.client = Client()


    def test_authenticated_access_page(self):
        ok = False
        c = Client()
        c.login(username='admin', password='admin')
        response = c.get(f"/account/")
        self.assertEqual(response.status_code, 200)

    def test_not_authenticated_access_page(self):
        c = Client()
        c.login(username='admin', password='wrong')
        response = c.get(f"/account/")
        self.assertNotEqual(response.status_code, 200)
        c.logout()

    def test_success_login_page(self):
        c = Client()
        c.login(username='admin', password='admin')
        c.post('/login/', {'name': 'fred', 'passwd': 'secret'})
        response = c.post('/account/login/', {'name': 'admin', 'password': 'admin'})
        # print(response['Location'])   # "/"
        self.assertEqual(response.status_code, 200)

    def test_fail_login_page(self):
        c = Client()
        response = c.post('/account/login/', {'username': 'admin', 'password': 'user'})
        self.assertNotEqual(response.status_code, 302)  # 302 redirect to login
