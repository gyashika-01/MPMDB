# Generated by Django 4.2.4 on 2023-10-05 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metabolites', '0003_rename_structure_of_metabolites_med_metabolites_structure_of_metabolites_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='med_metabolites',
            name='Structure_of_Metabolites_1',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='med_metabolites',
            name='Structure_of_Metabolites_2',
            field=models.URLField(),
        ),
    ]