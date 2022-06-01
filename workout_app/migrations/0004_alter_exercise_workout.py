# Generated by Django 3.2.5 on 2022-05-15 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workout_app', '0003_alter_exercise_workout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='workout',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercises', to='workout_app.workout'),
        ),
    ]