# Generated by Django 2.2.4 on 2020-03-18 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UrlShortener_urls', '0007_url_shorten_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='shorten_url',
            field=models.CharField(default='', max_length=10, unique=True),
        ),
    ]
