# Generated by Django 2.2.4 on 2020-03-19 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UrlShortener_urls', '0017_auto_20200319_0654'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='urlvisits',
            name='uuid',
        ),
    ]
