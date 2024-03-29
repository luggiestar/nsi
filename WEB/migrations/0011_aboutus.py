# Generated by Django 3.2.9 on 2022-05-13 07:34

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WEB', '0010_auto_20220510_1050'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('history', 'Our history'), ('function', 'Our history'), ('mission', 'Mission, Vision & Core Values')], max_length=40)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'about',
                'verbose_name_plural': 'about',
            },
        ),
    ]
