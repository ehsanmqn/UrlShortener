# Generated by Django 2.2.4 on 2020-03-18 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UrlShortener_urls', '0010_auto_20200318_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='uuid',
            field=models.CharField(db_index=True, default='', editable=False, max_length=10, unique=True),
        ),
    ]
