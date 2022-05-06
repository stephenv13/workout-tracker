from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponseRedirect
from workout_app.forms import WorkoutForm
from workout_app.models import Workout

# Create your views here.

# This returns the homepage HTML template
def home(request):
    return render(request,'home.html',{})

# This returns the account login HTML template
def account_login(request):
    return render(request,'login.html',{})

# This returns the workouts HTML template
def workouts(request):

    workout = get_object_or_404(Workout)

    if request.method == 'POST':
        form = WorkoutForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('workout_detail',pk=workout.pk)
    else:
        form = WorkoutForm()

    return render(request,'workouts.html',{'form':form})

def workout_detail(request):
    return render(request,'workout_detail.html')
