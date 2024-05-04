from django import forms
from categories.models import Categories

class CategoryFrom(forms.ModelForm):
    class Meta():
        fields = '__all__'
        model = Categories

        labels = {
            'name': 'Category'
        }