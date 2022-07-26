# Generated by Django 3.2.14 on 2022-07-30 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hikes', '0002_auto_20220730_0036'),
    ]

    operations = [
        migrations.AddField(
            model_name='hike',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='hike',
            name='image_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
    ]
