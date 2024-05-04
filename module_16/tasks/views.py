from django.shortcuts import render, redirect
from tasks.forms import TaskForm
from tasks.models import Task

# Create your views here.
def add_task(request):
    if request.method == 'POST':
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('show_tasks')
        else:
            return render(request, 'tasks/add_task.html', {
                'form': task_form
            })
        
    return render(request, 'tasks/add_task.html', {
        'form': TaskForm()
    })

def edit_task(request, id):
    task = Task.objects.get(pk=id)
    task_form = TaskForm(instance=task)
    if request.method == 'POST':
        task_form = TaskForm(request.POST, instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect('show_tasks')
        else:
            return render(request, 'tasks/add_task.html', {
                'form': task_form
            })
    return render(request, 'tasks/add_task.html', {
        'form': task_form
    })

def delet_task(request, id):
    task = Task.objects.get(pk=id)
    task.delete()
    return redirect('show_tasks')

def show_tasks(request):
    all_tasks = Task.objects.all()
    return render(request, 'tasks/show_tasks.html', {
        "tasks": all_tasks
    })