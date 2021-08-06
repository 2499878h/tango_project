# Generated by Django 2.2.13 on 2021-08-04 17:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('img', models.CharField(default='/static/img/article/1.png', max_length=200)),
                ('tags', models.CharField(blank=True, help_text='segment by comma', max_length=200, null=True, verbose_name='tag')),
                ('summary', models.TextField(verbose_name='summary')),
                ('content', models.TextField(verbose_name='content')),
                ('view_times', models.IntegerField(default=0)),
                ('zan_times', models.IntegerField(default=0)),
                ('is_top', models.BooleanField(default=False, verbose_name='top')),
                ('rank', models.IntegerField(default=0, verbose_name='order')),
                ('status', models.IntegerField(choices=[(0, 'normal'), (1, 'draft'), (2, 'delete')], default=0, verbose_name='status')),
                ('pub_time', models.DateTimeField(default=False, verbose_name='pub_date')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='create_time')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='update_time')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='author')),
            ],
            options={
                'verbose_name': 'article',
                'verbose_name_plural': 'article',
                'ordering': ['rank', '-is_top', '-pub_time', '-create_time'],
            },
        ),
        migrations.CreateModel(
            name='Nav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='nav content')),
                ('url', models.CharField(blank=True, max_length=200, null=True, verbose_name='redirect url')),
                ('status', models.IntegerField(choices=[(0, 'normal'), (1, 'draft'), (2, 'delete')], default=0, verbose_name='status')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='create_time')),
            ],
            options={
                'verbose_name': 'nav',
                'verbose_name_plural': 'nav',
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='name')),
                ('rank', models.IntegerField(default=0, verbose_name='order')),
                ('status', models.IntegerField(choices=[(0, 'normal'), (1, 'draft'), (2, 'delete')], default=0, verbose_name='status')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='create_date')),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='tango_center.Category', verbose_name='parent category')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'category',
                'ordering': ['rank', '-create_time'],
            },
        ),
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('summary', models.TextField(blank=True, null=True, verbose_name='summary')),
                ('img', models.CharField(default='/static/img/carousel/avatar.jpg', max_length=200, verbose_name='img')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='create_date')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tango_center.Article', verbose_name='article')),
            ],
            options={
                'verbose_name': 'carousel',
                'verbose_name_plural': 'carousel',
                'ordering': ['-create_time'],
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tango_center.Category', verbose_name='category'),
        ),
    ]
