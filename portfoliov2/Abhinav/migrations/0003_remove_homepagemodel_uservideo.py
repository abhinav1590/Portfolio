# Generated by Django 4.1.2 on 2022-11-03 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Abhinav', '0002_remove_homepagemodel_experties_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepagemodel',
            name='UserVideo',
        ),
    ]