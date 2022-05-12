from django.db import models
from django.urls import reverse
from django.shortcuts import get_object_or_404

# Create your models here.

class Workout(models.Model):

    workout_title = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    author = models.CharField(max_length=20)

    def get_absolute_url(self):
        return reverse('workout_detail',kwargs={'pk':self.pk})

    def __str__(self):
        return self.workout_title

class Exercise(models.Model):

    workout = models.ForeignKey('workout_app.workout',related_name = 'exercises',on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=20)
    number_of_sets = models.CharField(max_length=2)
    number_of_reps = models.CharField(max_length=2)
    weight = models.CharField(max_length=3)

    # return back to the workout detail page for the specified workout id
    def get_absolute_url(self):
        return reverse('workout_detail',kwargs={'pk':self.workout_id})
        

    def __str__(self) -> str:
        return self.name
