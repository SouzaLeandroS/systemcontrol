# Generated by Django 5.1.1 on 2024-09-10 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('customer', models.CharField(blank=True, max_length=200, null=True)),
                ('descrition', models.TextField(blank=True, max_length=200, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]