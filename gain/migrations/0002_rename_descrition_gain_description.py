# Generated by Django 5.1.1 on 2024-09-12 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gain', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gain',
            old_name='descrition',
            new_name='description',
        ),
    ]
