from msilib.schema import ListView
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponseRedirect
from workout_app.forms import ExerciseForm, WorkoutForm
from workout_app.models import Exercise, Workout
from django.views.generic import (DetailView,CreateView,ListView,UpdateView)

# Create your views here.

class AddWorkoutView(CreateView):
    redirect_field_name = 'add_workout.html'

    form_class = WorkoutForm

    model = Workout


class WorkoutDetailView(DetailView):
    model = Workout



class WorkoutListView(ListView):
    model = Workout

'''
This CBV will allow the user to edit a workout
'''
class EditExerciseView(UpdateView):
    redirect_field_name = ''

    form_class = WorkoutForm

    model = Workout

'''
This CBV will allow the user to edit an exercise
'''
class EditExerciseView(UpdateView):
    redirect_field_name = 'workout_app/workout_detail.html'

    form_class = ExerciseForm

    model = Exercise

# This returns the homepage HTML template
def home(request):
    return render(request,'home.html',{})

# This returns the account login HTML template
def account_login(request):
    return render(request,'login.html',{})

'''
This function allows the user to add an exercise to the currently viewed workout.
'''
def add_exercise(request,pk):

    workout = get_object_or_404(Workout,pk=pk)

    if request.method == 'POST':
        form = ExerciseForm(request.POST)

        # if the form is valid, save the exercise to the workout. Othewise, return back to exercise form
        if form.is_valid():
            exercise = form.save(commit=False)
            exercise.workout = workout
            exercise.save()
            return redirect('workout_detail',pk=workout.pk)
    else:
        form = ExerciseForm()
    return render(request,'workout_app/exercise_form.html',{'form':form})

'''
This function allows the user to delete an exercise
'''
def remove_exercise(request,pk):

    exercise = get_object_or_404(Exercise,pk)
    workout_pk = exercise.workout.pk
    exercise.delete()

    return redirect('workout_detail',pk=workout_pk)

