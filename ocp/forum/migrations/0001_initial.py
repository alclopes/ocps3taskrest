# Generated by Django 2.2.4 on 2019-09-18 09:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Slug')),
                ('body', models.TextField(verbose_name='Message')),
                ('views', models.IntegerField(blank=True, default=0, verbose_name='Views')),
                ('answers', models.IntegerField(blank=True, default=0, verbose_name='Anwers')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Create at')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Update at')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='threads', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Topic',
                'verbose_name_plural': 'Topic',
                'ordering': ['-modified'],
            },
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply', models.TextField(verbose_name='Answer')),
                ('correct', models.BooleanField(blank=True, default=False, verbose_name='Correct?')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Create at')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('thread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='forum.Thread', verbose_name='Topic')),
            ],
            options={
                'verbose_name': 'Answer',
                'verbose_name_plural': 'Anwers',
                'ordering': ['-correct', 'created'],
            },
        ),
    ]