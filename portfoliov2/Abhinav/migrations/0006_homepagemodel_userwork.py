# Generated by Django 4.1.2 on 2022-11-18 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Abhinav', '0005_homepagemodel_userbitmoji'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepagemodel',
            name='UserWork',
            field=models.ImageField(null=True, upload_to='images-bitmoji'),
        ),
    ]
