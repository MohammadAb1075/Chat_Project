# Generated by Django 2.2.3 on 2019-08-22 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20190822_1723'),
        ('users', '0004_auto_20190822_1347'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
