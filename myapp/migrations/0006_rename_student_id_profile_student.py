# Generated by Django 3.2.9 on 2022-08-15 01:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='student_id',
            new_name='student',
        ),
    ]
