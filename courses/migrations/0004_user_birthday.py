# Generated by Django 3.1.1 on 2021-06-02 07:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_remove_user_birthday'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2001, 9, 26, 0, 0)),
            preserve_default=False,
        ),
    ]