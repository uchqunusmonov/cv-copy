# Generated by Django 4.0.1 on 2022-03-31 17:57

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('text', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(upload_to='information/')),
                ('back_ground', models.ImageField(blank=True, null=True, upload_to='background/')),
                ('warehouse', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OurTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='OurTeam/')),
                ('first_name', models.CharField(blank=True, max_length=150, null=True)),
                ('last_name', models.CharField(blank=True, max_length=150, null=True)),
                ('position', models.CharField(blank=True, max_length=150, null=True)),
                ('instagram', models.URLField(blank=True, null=True)),
                ('facebook', models.URLField(blank=True, null=True)),
                ('telegram', models.URLField(blank=True, null=True)),
                ('responsibility', models.CharField(blank=True, max_length=250, null=True)),
                ('experience', models.CharField(blank=True, max_length=250, null=True)),
                ('email', models.EmailField(blank=True, max_length=250, null=True)),
                ('phone', models.PositiveBigIntegerField(blank=True, null=True)),
                ('fax', models.PositiveBigIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sphere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, null=True)),
                ('text', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
