# Generated by Django 3.2.9 on 2023-07-08 21:09

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(2, '>= 2 characters for breedtype')])),
            ],
        ),
        migrations.CreateModel(
            name='Cats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(2, 'Name must be >= 2 characters')])),
                ('weight', models.PositiveIntegerField()),
                ('food', models.CharField(max_length=300)),
                ('breed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cats.breed')),
            ],
        ),
    ]