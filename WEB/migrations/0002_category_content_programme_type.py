# Generated by Django 3.2.9 on 2022-02-26 11:59

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WEB', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Certificate', 'Certificate'), ('Diploma', 'Certificate'), ('Short Course', 'Short Course')], max_length=45, unique=True)),
            ],
            options={
                'verbose_name': 'Programme Category',
                'verbose_name_plural': 'Programme Category',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('NEWS', 'NEWS'), ('EVENT', 'EVENT'), ('REPORT', 'REPORT'), ('NEWS LETTER', 'NEWS LETTER'), ('DOWNLOADS', 'DOWNLOADS')], max_length=45, unique=True)),
            ],
            options={
                'verbose_name': 'Content Type',
                'verbose_name_plural': 'Content Type',
            },
        ),
        migrations.CreateModel(
            name='Programme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, unique=True, verbose_name='')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WEB.category')),
            ],
            options={
                'verbose_name': 'Programme Category',
                'verbose_name_plural': 'Programme Category',
            },
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, unique=True)),
                ('date', models.DateField(null=True)),
                ('image', models.ImageField(upload_to='', verbose_name='Content Image')),
                ('uploaded_date', models.DateField(auto_now_add=True)),
                ('place', models.CharField(max_length=500, null=True)),
                ('body', ckeditor.fields.RichTextField()),
                ('is_active', models.BooleanField(default=True)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WEB.type')),
            ],
            options={
                'verbose_name': 'Programme Category',
                'verbose_name_plural': 'Programme Category',
            },
        ),
    ]
