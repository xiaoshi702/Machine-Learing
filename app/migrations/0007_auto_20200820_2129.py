# Generated by Django 2.2.14 on 2020-08-20 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20200820_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article_list',
            name='add_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
