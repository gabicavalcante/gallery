# Generated by Django 2.0.9 on 2018-12-08 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo_gallery', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='is_approve',
            new_name='is_approved',
        ),
    ]
