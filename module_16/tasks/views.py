from django.shortcuts import render, redirect
from tasks.forms import TaskForm

# Create your views here.
def add_task(request):
    if request.method == 'POST':
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('add_task')
        else:
            return render(request, 'tasks/add_task.html', {
                'form': task_form
            })
        
    return render(request, 'tasks/add_task.html', {
        'form': TaskForm()
    })


def show_tasks(request):
    return render(request, 'tasks/show_tasks.html')