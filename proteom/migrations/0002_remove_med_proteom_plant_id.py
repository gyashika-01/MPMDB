# Generated by Django 5.1.1 on 2024-11-10 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proteom', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='med_proteom',
            name='Plant_Id',
        ),
    ]