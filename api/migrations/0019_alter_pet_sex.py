# Generated by Django 4.1.1 on 2022-10-06 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_alter_pet_sex_alter_pet_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='sex',
            field=models.CharField(choices=[('Macho', 'Macho'), ('Hembra', 'Hembra')], max_length=10),
        ),
    ]
