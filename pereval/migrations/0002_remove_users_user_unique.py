# Generated by Django 4.2.5 on 2023-12-27 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pereval', '0001_initial'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='users',
            name='user_unique',
        ),
    ]