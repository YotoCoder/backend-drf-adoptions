# Generated by Django 4.1.1 on 2022-10-13 02:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_alter_pet_size'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pet',
            options={'ordering': ['-created_at']},
        ),
    ]
