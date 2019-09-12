from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import Category, Course
import time
from django.db.models import Q
from decouple import config
from django.utils import timezone
from datetime import datetime


# task to delete images and register after some time
# if populate, delete only after that occur.
@shared_task()
def course_delete_set_task(one_ago):
    # Started task, after 900 seconds / 15 min...
    time.sleep(5)
    populate_date = config('POPULATE_DATE')
    if populate_date == "":
        time_finish = timezone.now() - timezone.timedelta(seconds=3)
        Course.objects.filter(Q(created_at__lte=time_finish)).delete()
    else:
        time_start = populate_date
        time_start = datetime.strptime(time_start, '%Y-%m-%d %H:%M:%S.%f')
        time_finish = timezone.now() - timezone.timedelta(seconds=3)
        Course.objects.filter(Q(created_at__gt=time_start) & Q(created_at__lte=time_finish)).delete()
    return True


# task to delete images and register after some time
# if populate, delete only after that occur.
@shared_task()
def category_delete_set_task(one_ago):
    # Started task, after 900 seconds / 15 min...
    time.sleep(5)
    populate_date = config('POPULATE_DATE')
    if populate_date == "":
        time_finish = timezone.now() - timezone.timedelta(seconds=3)
        Category.objects.filter(Q(created_at__lte=time_finish)).delete()
    else:
        time_start = populate_date
        time_start = datetime.strptime(time_start, '%Y-%m-%d %H:%M:%S.%f')
        time_finish = timezone.now() - timezone.timedelta(seconds=3)
        Category.objects.filter(Q(created_at__gt=time_start) & Q(created_at__lte=time_finish)).delete()
    return True


# # Best Practice to task //TODO
# from myapp import app
# from celery.exceptions import SoftTimeLimitExceeded
#
# @app.task
# def mytask():
#     try:
#         do_work()
#     except SoftTimeLimitExceeded:
#         clean_up_in_a_hurry()
