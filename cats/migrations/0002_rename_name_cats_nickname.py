# Generated by Django 3.2.9 on 2023-07-10 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cats',
            old_name='name',
            new_name='nickname',
        ),
    ]
