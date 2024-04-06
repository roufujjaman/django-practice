from django import forms
from . import models

class StudentForm(forms.ModelForm):
    class Meta:
        model = models.Student
        exclude= ["address"]
        fields = "__all__"
        labels = {
            "name": "Full Name",
            "roll": "Student ID",
        }
        widgets = {
            "email": forms.EmailInput(
                attrs={
                    "class": "red"
                }
            )
        }
        help_text = {
            "name"
        }