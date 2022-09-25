# Generated by Django 4.1.1 on 2022-09-25 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='sex',
            field=models.CharField(choices=[('1', 'Macho'), ('2', 'Hembra')], default='2', max_length=10),
        ),
        migrations.AlterField(
            model_name='pet',
            name='size',
            field=models.CharField(choices=[('1', 'Pequeño'), ('2', 'Mediano'), ('3', 'Grande')], default='2', max_length=10),
        ),
    ]