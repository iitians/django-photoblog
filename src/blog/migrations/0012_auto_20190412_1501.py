# Generated by Django 2.0.1 on 2019-04-12 13:01

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0011_auto_20180204_2109'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Photo',
            new_name='ImagePost',
        ),
    ]
