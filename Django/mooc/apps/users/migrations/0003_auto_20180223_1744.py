# Generated by Django 2.0.1 on 2018-02-23 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180112_1645'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banner',
            options={'verbose_name': '轮播图', 'verbose_name_plural': '轮播图'},
        ),
        migrations.AlterModelOptions(
            name='emailverifyrecord',
            options={'verbose_name': '邮箱验证码', 'verbose_name_plural': '邮箱验证码'},
        ),
    ]
