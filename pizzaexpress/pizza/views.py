from django.shortcuts import render
from .forms import PizzaForm, MultiplePizzaForm
from django.forms import formset_factory
from .models import Pizza

# Create your views here.
def home(request):
    return render(request, 'pizza/home.html')

def order(request):
    multiple_form = MultiplePizzaForm()
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST, request.FILES)
        print(request.FILES, 'came here')
        if filled_form.is_valid():
            created_pizza = filled_form.save()
            created_pizz_pk = created_pizza.id
            
            note = 'Thanks for ordering! Your %s pizza is on its way' %(filled_form.cleaned_data['size'])

            new_from = PizzaForm()

            return render(request, 'pizza/order.html', {
                'pizzaform': new_from,
                'note': note,
                'multiple_form': multiple_form,
                'created_pizza_pk': created_pizz_pk
            })
            

    else:
        form = PizzaForm() 
        return render(request, 'pizza/order.html', {
            'pizzaform': form,
            'multiple_form': multiple_form
            })

def pizzas(request):
    number_of_pizzas = 2
    filled_multiple_pizza_form = MultiplePizzaForm(request.GET)

    if filled_multiple_pizza_form.is_valid():
        number_of_pizzas = filled_multiple_pizza_form.cleaned_data['number']

    PizzaFormSet = formset_factory(PizzaForm, extra=number_of_pizzas)
    formset = PizzaFormSet()

    if request.method == "POST":
        filled_formset = PizzaFormSet(request.POST)
         
        if filled_formset.is_valid():
            for form in filled_formset:
                form.save()
                print(form.cleaned_data["topping1"])

            note = "Pizzas have been ordered"
        else:
            note = "Order is not created, please try again"

        return render(request, 'pizza/pizzas.html', {
            "formset": formset,
            "note": note,
        })
    else:
        return render(request, 'pizza/pizzas.html', {
            'formset': formset
        })



def edit_order(request, pk):
    pizza = Pizza.objects.get(pk=pk)
    form = PizzaForm(instance=pizza)
    note = "Current Order"
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST, instance=pizza)
        if filled_form.is_valid():
            filled_form.save()
            form = filled_form
            note = 'Order has been updated'

    
    return render(request, 'pizza/edit_order.html', {
        'pizzaform': form,
        'pizza': pizza,
        'note': note
    })