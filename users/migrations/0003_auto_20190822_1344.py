# Generated by Django 2.2.3 on 2019-08-22 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.UUIDField(null=True),
        ),
    ]