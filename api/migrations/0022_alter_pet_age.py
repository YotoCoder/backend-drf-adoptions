# Generated by Django 4.1.1 on 2022-10-06 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_alter_pet_age_alter_pet_size_alter_pet_type_pet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='age',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('999', '999')], max_length=3),
        ),
    ]
