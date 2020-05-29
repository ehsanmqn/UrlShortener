# Generated by Django 2.2.4 on 2020-03-17 19:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('url', models.TextField(blank=True, max_length=1000, null=True, verbose_name='url')),
                ('created', models.DateTimeField(db_index=True, editable=False)),
                ('title', models.CharField(blank=True, default='', max_length=100, verbose_name='title')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='urls', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'index_together': {('creator', 'uuid')},
            },
        ),
    ]