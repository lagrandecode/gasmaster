# Generated by Django 4.1.7 on 2023-04-27 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GasNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_image', models.ImageField(upload_to='')),
                ('news_desc', models.CharField(max_length=1000)),
                ('content', models.CharField(max_length=5000)),
                ('news_link', models.URLField()),
                ('created_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]