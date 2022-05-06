from django.db import models

# Create your models here.

class Workout(models.Model):

    workout_title = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    author = models.CharField(max_length=20)

    def __str__(self):
        return self.workout_title

class Exercise(models.Model):

    workout = models.ForeignKey(Workout,on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=20)
    number_of_sets = models.CharField(max_length=2)
    number_of_reps = models.CharField(max_length=2)
    weight = models.CharField(max_length=3)

    def __str__(self) -> str:
        return self.name
