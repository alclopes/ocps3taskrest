from django.core import mail
from django.test import TestCase
from django.test.client import Client
from django.urls import reverse
from django.conf import settings

from ocp.courses.models import Category, Course


class ContactTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Category 01', slug='category_01')
        self.course = Course.objects.create(name='Course 01', slug='course_01', category_id=self.category.id)

    def tearDown(self):
        self.course.delete()

    def test_contact_form_error(self):
        data = {'name': '', 'email': '', 'message': ''}
        client = Client()
        path = reverse('core:contact')
        response = client.post(path, data)
        self.assertFormError(response, 'form', 'name', 'This field is required.')
        self.assertFormError(response, 'form', 'email', 'This field is required.')
        self.assertFormError(response, 'form', 'message', 'This field is required.')

    def test_contact_form_success(self):
        data = {
            'name': 'Nome Contato 01',
            'email': 'admin@admin.com',
            'message': 'Oi'
        }

        client = Client()
        path = reverse('courses:course_details', args=[self.course.slug])

        response = client.post(path, data)

        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].to, [settings.EMAIL_HOST_USER])
