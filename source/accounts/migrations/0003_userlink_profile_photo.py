# Generated by Django 2.2.1 on 2019-11-01 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20191101_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlink',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to='user_pics', verbose_name='Avatar'),
        ),
    ]
