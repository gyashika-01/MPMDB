# Generated by Django 5.1.1 on 2024-11-10 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='med_basic',
            old_name='Bioactive_Compound',
            new_name='Scientific_Name',
        ),
        migrations.RenameField(
            model_name='med_basic',
            old_name='States_of_India_Support_their_Growth',
            new_name='Worldwide_regions_Support_their_Growth',
        ),
        migrations.RemoveField(
            model_name='med_basic',
            name='Plant_Id',
        ),
        migrations.AlterField(
            model_name='med_basic',
            name='Plant_Name',
            field=models.TextField(),
        ),
    ]