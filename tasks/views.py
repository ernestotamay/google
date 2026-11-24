from django.shortcuts import render, redirect, get_object_or_404
from .models import List, Task
from .forms import ListForm, TaskForm

# Listas
def list_list(request):
    lists = List.objects.all()
    return render(request, 'tasks/list_list.html', {'lists': lists})

def list_create(request):
    form = ListForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list-list')
    return render(request, 'tasks/task_form.html', {'form': form})

# Tareas
def task_list(request, list_id):
    lista = get_object_or_404(List, id=list_id)
    tasks = lista.tasks.all()
    return render(request, 'tasks/task_list.html', {'lista': lista, 'tasks': tasks})

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'tasks/task_detail.html', {'task': task})

def task_create(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list-list')
    return render(request, 'tasks/task_form.html', {'form': form})

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('task-detail', pk=task.pk)
    return render(request, 'tasks/task_form.html', {'form': form})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('list-list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})