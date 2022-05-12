from django.contrib import admin
from django.urls import path
from workout_app import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.account_login,name='login'),
    path('workouts/',views.WorkoutListView.as_view(),name='workouts'),
    path('workouts/add_workout/',views.AddWorkoutView.as_view(),name='add_workout'),
    path('workouts/<int:pk>/remove_workout/',views.remove_workout,name='remove_workout'),
    path('workouts/<int:pk>/',views.WorkoutDetailView.as_view(),name='workout_detail'),
    path('workouts/<int:pk>/add_exercise/',views.add_exercise,name='add_exercise'),
    path('workouts/<int:workout_id>/edit_exercise/<int:pk>/',views.EditExerciseView.as_view(),name='edit_exercise'),
    path('workouts/<int:workout_id>/edit_exercise/<int:pk>/remove/',views.remove_exercise,name='remove_exercise'),


]