# Generated by Django 4.1.1 on 2022-10-06 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_pet_age_alter_pet_city_alter_pet_is_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='age',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)], default=1),
        ),
        migrations.AlterField(
            model_name='pet',
            name='city',
            field=models.CharField(default='Lima', max_length=66),
        ),
        migrations.AlterField(
            model_name='pet',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='pet',
            name='sex',
            field=models.CharField(choices=[('Macho', 'Macho'), ('Hembra', 'Hembra')], default=2, max_length=10),
        ),
        migrations.AlterField(
            model_name='pet',
            name='size',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3)], default=2),
        ),
        migrations.AlterField(
            model_name='pet',
            name='type_pet',
            field=models.CharField(choices=[('Perro', 'Perro'), ('Gato', 'Gato'), ('Otro', 'Otro')], default='Perro', max_length=10),
        ),
    ]