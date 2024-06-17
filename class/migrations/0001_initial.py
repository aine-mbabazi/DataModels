# Generated by Django 5.0.6 on 2024-06-17 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=20)),
                ('class_id', models.PositiveSmallIntegerField()),
                ('course', models.CharField(max_length=20)),
                ('teacher', models.CharField(max_length=20)),
                ('enrollment', models.PositiveSmallIntegerField()),
                ('room_number', models.PositiveSmallIntegerField()),
                ('class_time', models.CharField(max_length=20)),
                ('meeting_days', models.CharField(max_length=40)),
                ('academic_year', models.PositiveSmallIntegerField()),
                ('class_capacity', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
