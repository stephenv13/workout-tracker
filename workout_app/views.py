from msilib.schema import ListView
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponseRedirect
from workout_app.forms import WorkoutForm
from workout_app.models import Workout
from django.views.generic import (DetailView,CreateView,ListView)

# Create your views here.

# This returns the homepage HTML template
def home(request):
    return render(request,'home.html',{})

# This returns the account login HTML template
def account_login(request):
    return render(request,'login.html',{})

# # This returns the workouts HTML template
# def workouts(request):

#     return render(request,'workouts.html',{})

class AddWorkoutView(CreateView):
    redirect_field_name = 'add_workout.html'

    form_class = WorkoutForm

    model = Workout


class WorkoutDetailView(DetailView):
    model = Workout

class WorkoutListView(ListView):
    model = Workout

    

