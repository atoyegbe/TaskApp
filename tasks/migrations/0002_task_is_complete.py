# Generated by Django 3.0.3 on 2020-07-09 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='is_complete',
            field=models.BooleanField(default=False),
        ),
    ]
