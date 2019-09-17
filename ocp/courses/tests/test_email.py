from django.core import mail
from django.test import TestCase
from decouple import config


class EmailTest(TestCase):
    def test_send_email(self):
        sender = [config('EMAIL_HOST_USER')]
        receiver = [config('RECEIVE_EMAIL')]
        mail.send_mail('SubjectMail', 'MessageMail.',
            sender, receiver, fail_silently=False)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'SubjectMail')
        self.assertEqual(mail.outbox[0].to, receiver)
