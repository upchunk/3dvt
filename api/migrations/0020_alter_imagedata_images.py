# Generated by Django 4.1 on 2022-09-05 18:02

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_alter_imagedata_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagedata',
            name='images',
            field=models.FileField(help_text='Image File to be Processed', upload_to=api.models.ImageDataset, verbose_name='images'),
        ),
    ]