# Generated by Django 2.2.4 on 2020-03-18 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UrlShortener_urls', '0009_remove_url_shorten_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='uuid',
            field=models.UUIDField(db_index=True, default='', editable=False, unique=True),
        ),
    ]
