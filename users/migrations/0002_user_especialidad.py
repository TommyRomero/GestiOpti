# Generated by Django 2.2.17 on 2020-12-03 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='especialidad',
            field=models.TextField(default='', max_length=200),
        ),
    ]
