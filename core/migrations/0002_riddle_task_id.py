# Generated by Django 5.0.1 on 2024-01-28 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='riddle',
            name='task_id',
            field=models.CharField(blank=True, max_length=36),
        ),
    ]
