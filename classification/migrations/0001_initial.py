# Generated by Django 4.2.4 on 2023-09-09 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='med_class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Plant_Id', models.IntegerField()),
                ('Plant_Name', models.TextField()),
                ('Scientific_Name', models.TextField()),
                ('Kingdom', models.TextField()),
                ('Division', models.TextField()),
                ('Class', models.TextField()),
                ('Order', models.TextField()),
                ('Family', models.TextField()),
                ('Genus', models.TextField()),
                ('Species', models.TextField()),
            ],
        ),
    ]