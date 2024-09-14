# Generated by Django 5.1.1 on 2024-09-13 03:44

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('status', models.CharField(choices=[('LAYOFFS', 'Layoffs'), ('HIRING FREEZE', 'Hiring Freeze'), ('HIRING', 'Hiring')], default='HIRING', max_length=13)),
                ('last_update', models.DateTimeField(default=django.utils.timezone.now)),
                ('application_link', models.URLField(blank=True)),
                ('notes', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
