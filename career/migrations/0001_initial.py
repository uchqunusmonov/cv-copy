# Generated by Django 4.0.1 on 2022-04-02 14:27

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', ckeditor.fields.RichTextField(blank=True, max_length=500)),
                ('salary', models.PositiveIntegerField(default=0, help_text='enter the currency in dollars')),
                ('job_type', models.CharField(choices=[('online', 'online'), ('offline', 'offline')], max_length=10)),
                ('graph', models.CharField(choices=[('full time', 'full time'), ('part time', 'part time')], default='full time', max_length=10)),
                ('active_date', models.DateField(blank=True, null=True)),
                ('duties', models.CharField(blank=True, max_length=500)),
                ('requirements', models.CharField(blank=True, max_length=500)),
                ('pros', models.CharField(blank=True, max_length=500)),
                ('skills', models.CharField(blank=True, max_length=500)),
                ('active', models.BooleanField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Vacancy',
                'verbose_name_plural': 'Vacancies',
            },
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('file', models.FileField(help_text='Send your resume as a file', upload_to='')),
                ('created_date', models.DateField(auto_now_add=True)),
                ('vacancy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='career.vacancy')),
            ],
            options={
                'verbose_name': 'Resume',
                'verbose_name_plural': 'Resumes',
            },
        ),
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('background', models.ImageField(upload_to='Career/images/')),
                ('job_ads', models.TextField(verbose_name='Job advertisement title')),
                ('tel', models.CharField(max_length=100)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
