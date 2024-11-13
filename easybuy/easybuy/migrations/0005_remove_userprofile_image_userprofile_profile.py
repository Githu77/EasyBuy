# Generated by Django 5.1.2 on 2024-11-13 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easybuy', '0004_userprofile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='image',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='profile',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics/'),
        ),
    ]
