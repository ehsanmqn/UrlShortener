# Generated by Django 2.2.4 on 2020-03-18 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UrlShortener_urls', '0008_auto_20200318_1624'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='url',
            name='shorten_url',
        ),
    ]