# Generated by Django 3.2.9 on 2022-02-27 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WEB', '0004_auto_20220227_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='documents', verbose_name='Content Image'),
        ),
    ]
