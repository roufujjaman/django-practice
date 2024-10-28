from django import forms
from .models import Pizza, Size

# PIZZA_SIZE_CHOICES = [
#     ("Small", "Small"),
#     ("Medium", "Medium"),
#     ("Large", "large")
# ]

# PIZZA_TOPPING_CHOICES = [
#     ("Pepperoni", "Pepperoni"),
#     ("Cheese", "Cheese"),
#     ("Olive", "Olive")
# ]

# class PizzaForm(forms.Form):
#     # topping = forms.MultipleChoiceField(choices=PIZZA_TOPPING_CHOICES, widget=forms.CheckboxSelectMultiple)
#     topping1 = forms.CharField(label="Topping 1", max_length=100)
#     topping2 = forms.CharField(label="Topping 2", max_length=100)
#     size = forms.ChoiceField(label="Size", choices=PIZZA_SIZE_CHOICES)



class PizzaForm(forms.ModelForm):

    class Meta:
        model = Pizza
        fields = ["topping1", "topping2", "size"]

        labels = {
            "topping1": "Topping 1",
            "topping2": "Topping 2"
        }


class MultiplePizzaForm(forms.Form):
    number = forms.IntegerField(min_value=2, max_value=6)