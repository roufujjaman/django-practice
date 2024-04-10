from django.shortcuts import render
from django import forms

class UserForm(forms.Form):
    name = forms.CharField(
        label="Full Name",
        initial="Your Name Here",
        widget=forms.TextInput()
    )
    
    email = forms.EmailField()
    
    birth_date = forms.DateField(
        label="Birth Date",
        widget=forms.DateInput(
            attrs={
                "type": "date"
                }
            )
    )

    join_year_choices = ["2020", "2021", "2022", "2023", "2024"]
    join_date = forms.DateField(
        label="Joining Date",
        widget=forms.SelectDateWidget(
            years=join_year_choices,
        )
    )

    weight = forms.DecimalField()

    location_choices = [("UT", "Uttara"), ("BN", "Banani"), ("DH", "Dhanmondi"), ("GL", "Gulshan")]
    location = forms.ChoiceField(
        choices=location_choices
    )

    prefered_days_choices = [("S", "Sunday"), ("M", "Monday"), ("T", "Tuesday"), ("W", "Wednesday"), ("R", "Thursday")]
    prefered_days = forms.MultipleChoiceField(
        choices=prefered_days_choices
    )

    comment = forms.CharField(
        widget=forms.Textarea(
            attrs={"rows": 5}
        )
    )

    agree = forms.BooleanField()



def home(request):
    return render(request, "project/layout.html")

def form(request):
    return render(request, "project/form.html", {
        "userForm": UserForm()
    })