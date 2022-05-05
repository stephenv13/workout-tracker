from django.shortcuts import render,get_object_or_404,redirect

# Create your views here.

# This returns the homepage HTML template
def home(request):
    return render(request,'home.html',{})

# This returns the account login HTML template
def account_login(request):
    return render(request,'login.html',{})

# This returns the workouts HTML template
def workouts(request):
    return render(request,'workouts.html',{})
