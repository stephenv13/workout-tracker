from django.contrib import admin
from django.urls import path,include
from workout_app import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.account_login,name='login'),
    path('workouts/',views.WorkoutListView.as_view(),name='workouts'),
    path('workouts/add_workout/',views.AddWorkoutView.as_view(),name='add_workout'),
    path('workouts/<int:pk>/',views.WorkoutDetailView.as_view(),name='workout_detail'),
    path('workouts/<int:pk>/add_exercise/',views.add_exercise,name='add_exercise'),
    path('workouts/<int:pk>/<int:exercise>/edit_exercise/',views.EditExerciseView.as_view(),name='edit_exercise'),


]