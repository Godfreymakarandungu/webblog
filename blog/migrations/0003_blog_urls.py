# Generated by Django 2.2.3 on 2019-07-29 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190717_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='urls',
            field=models.TextField(default='www.makarablog.duckdns.org'),
        ),
    ]
