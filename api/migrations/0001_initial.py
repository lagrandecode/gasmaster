# Generated by Django 4.2.1 on 2023-05-08 10:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=250)),
                ('discount', models.PositiveIntegerField()),
                ('selling_price', models.PositiveIntegerField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='productimages/')),
                ('kg', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('profile_pics', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('address', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
