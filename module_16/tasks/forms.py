from django import forms
from tasks.models import Task


class TaskForm(forms.ModelForm):
    class Meta():
        fields = '__all__'
        model = Task


        labels = {
            'is_completed': 'Completed'
        }

        widgets = {
            'assign_date': forms.DateInput(attrs={
                'type': 'date'
            })
        }
        