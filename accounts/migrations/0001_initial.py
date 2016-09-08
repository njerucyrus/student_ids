# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-03 21:46
from __future__ import unicode_literals

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
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='IdApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regNo', models.CharField(max_length=32)),
                ('full_name', models.CharField(max_length=100)),
                ('passport', models.ImageField(upload_to='img/passports')),
                ('application_type', models.CharField(choices=[('F', 'First Time'), ('R', 'Replacement')], default='F', max_length=32)),
                ('paid', models.BooleanField(default=False)),
                ('date_applied', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phoneNumber', models.CharField(max_length=13)),
                ('regNo', models.CharField(max_length=32, unique=True, verbose_name='RegNo')),
                ('national_id', models.PositiveIntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Course')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Department')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.School'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='department',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.School'),
        ),
        migrations.AddField(
            model_name='course',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Department'),
        ),
    ]
