# Generated by Django 3.2.5 on 2022-05-06 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='weight',
            field=models.CharField(default=0, max_length=3),
            preserve_default=False,
        ),
    ]
