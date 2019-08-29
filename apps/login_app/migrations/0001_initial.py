# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-08-29 19:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('mainCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='login_app.Categories')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('pw_hash', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('credits', models.IntegerField(default=3)),
                ('desc', models.TextField(default='', max_length=255)),
                ('image_base', models.TextField(default='', null=True)),
                ('location', models.TextField(default='', max_length=255)),
                ('skills_to_learn', models.ManyToManyField(related_name='students', to='login_app.SubCategories')),
                ('skills_to_teach', models.ManyToManyField(related_name='teachers', to='login_app.SubCategories')),
            ],
        ),
    ]
