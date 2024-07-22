# Generated by Django 5.0.6 on 2024-07-22 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class_period',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('class_room', models.CharField(max_length=20)),
                ('day_of_week', models.CharField(max_length=20)),
                ('teacher', models.CharField(max_length=20)),
                ('subject', models.CharField(max_length=20)),
                ('is_cancelled', models.BooleanField()),
            ],
        ),
    ]
