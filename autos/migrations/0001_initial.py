# Generated by Django 3.2.9 on 2023-07-04 02:31

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Make',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='enter a make', max_length=200, validators=[django.core.validators.MinLengthValidator(2, 'It must be >= 2 characters')])),
            ],
        ),
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(help_text='enter a nickname', max_length=200, validators=[django.core.validators.MinLengthValidator(2, 'It must be >= 2 characters')])),
                ('mileage', models.PositiveIntegerField()),
                ('comments', models.CharField(max_length=250)),
                ('make', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autos.make', verbose_name='fk-make')),
            ],
        ),
    ]
