# Generated by Django 4.1.1 on 2022-09-18 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_pet_is_active_alter_pet_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelPetTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
    ]
