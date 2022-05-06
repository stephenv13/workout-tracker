from django.contrib import admin
from django.urls import path,include
from workout_app import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.account_login,name='login'),
    path('workouts/',views.workouts,name='workouts'),
    path('workouts/<int:pk>/',views.workout_detail,name='workout_detail')


]