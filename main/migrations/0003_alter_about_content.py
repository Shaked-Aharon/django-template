# Generated by Django 5.0.6 on 2024-06-18 16:28

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_about_alter_category_options_alter_product_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='תוכן'),
        ),
    ]