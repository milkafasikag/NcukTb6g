# Generated by Django 4.2.4 on 2023-10-30 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0013_testmoni_image_worker_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccess',
            name='referer',
            field=models.URLField(null=True),
        ),
    ]
