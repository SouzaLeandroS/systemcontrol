# Generated by Django 5.1.1 on 2024-09-21 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gain', '0002_rename_descrition_gain_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gain',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
