# Generated by Django 4.1 on 2023-12-27 13:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_rename_create_date_post_created_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 27, 13, 10, 14, 72496, tzinfo=datetime.timezone.utc)),
        ),
    ]
