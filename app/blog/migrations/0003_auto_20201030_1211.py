# Generated by Django 3.1.2 on 2020-10-30 09:11

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201030_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
