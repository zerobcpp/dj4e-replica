# Generated by Django 4.0.7 on 2024-03-26 05:04

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_names', models.CharField(max_length=500, validators=[django.core.validators.MinLengthValidator(2, 'name must be longer')])),
                ('transaction_id', models.CharField(default='0', max_length=150)),
                ('total_products', models.CharField(default='0', max_length=150)),
                ('total_amount', models.CharField(default='0', max_length=150)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='')),
            ],
        ),
    ]
