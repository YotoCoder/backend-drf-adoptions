# Generated by Django 4.1.1 on 2022-09-20 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelPetTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('img', models.ImageField(blank=True, null=True, upload_to='img/petstes/')),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=255)),
                ('img', models.ImageField(upload_to='img/pets/')),
                ('age', models.IntegerField(default=1)),
                ('sex', models.CharField(default='Macho', max_length=10)),
                ('size', models.CharField(default='Mediano', max_length=10)),
                ('city', models.CharField(default='Lima', max_length=66)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
