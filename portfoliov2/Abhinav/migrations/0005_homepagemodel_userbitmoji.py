# Generated by Django 4.1.2 on 2022-11-18 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Abhinav', '0004_homepagemodel_uservideo'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepagemodel',
            name='UserBitmoji',
            field=models.ImageField(null=True, upload_to='images-bitmoji'),
        ),
    ]
