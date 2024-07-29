# Generated by Django 4.1.8 on 2024-07-18 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=255)),
                ('amount', models.PositiveBigIntegerField()),
                ('description', models.CharField(max_length=255)),
                ('discount', models.CharField(max_length=100)),
                ('photo', models.ImageField(blank=True, upload_to='')),
            ],
        ),
    ]
