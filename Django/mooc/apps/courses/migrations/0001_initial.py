# Generated by Django 2.0.1 on 2018-01-12 14:18

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseResoure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='视频')),
                ('download', models.FileField(upload_to='course/resource/%y/%m', verbose_name='下载地址')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='课程名')),
                ('desc', models.CharField(max_length=300, verbose_name='课程描述')),
                ('detail', models.TextField(verbose_name='课程详情')),
                ('degree', models.CharField(choices=[('cj', '初级'), ('zj', '中级'), ('gj', '高级')], max_length=10, verbose_name='难度')),
                ('learn_times', models.IntegerField(default=0, verbose_name='学习时长(分钟)')),
                ('students', models.IntegerField(default=0, verbose_name='学习人数')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='收藏人数')),
                ('image', models.ImageField(upload_to='courses/%Y/%m', verbose_name='封面图')),
                ('click_nums', models.IntegerField(default=0, verbose_name='点击量')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='章节')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Courses', verbose_name='课程')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='视频名')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Lesson', verbose_name='章节')),
            ],
        ),
        migrations.AddField(
            model_name='courseresoure',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Courses', verbose_name='课程'),
        ),
    ]
