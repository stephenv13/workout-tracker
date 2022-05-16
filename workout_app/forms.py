from django import forms
from workout_app.models import Workout,Exercise

#  use 'attrs' to set HTML attributes accordingly
class WorkoutForm(forms.ModelForm):

    class Meta():
        model = Workout
        fields = ('workout_title','description','author')

        widgets ={
            'workout_title':forms.TextInput(attrs={'class':'textinputclass','placeholder':'Enter Title...'}),
            'description':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent','placeholder':'Enter Description...'}),
            'author':forms.TextInput(attrs={'class':'textinputclass','placeholder':"Enter Author's Name..."}),

        }

class ExerciseForm(forms.ModelForm):

    class Meta():
        model = Exercise
        fields = ('name','number_of_sets','number_of_reps','weight')

        widgets = {
            'name':forms.TextInput(attrs={'class':'textinputclass','placeholder':"Enter Exercsie Name..."}),
            'number_of_sets':forms.NumberInput(attrs={'class':'numberinputclass','placeholder':"Enter Number of Sets..."}),
            'number_of_reps':forms.NumberInput(attrs={'class':'numberinputclass','placeholder':"Enter Number of Reps..."}),
            'weight':forms.NumberInput(attrs={'class':'numberinputclass','placeholder':"Enter Total Weight..."})
        }