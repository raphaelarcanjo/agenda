from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Task
from .forms import TaskForm
from datetime import datetime

# Create your views here.


@login_required
def list(request):
    tasks = Task.objects.all()
    dt = datetime.now()
    data = {
        'tasks': tasks,
        'date': dt.date(),
        'time': dt.time(),
    }

    return render(request, 'list.html', data)


@login_required
def create(request):
    form = TaskForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list')

    return render(request, 'create.html', {'form': form})


@login_required
def update(request, id):
    task = Task.objects.get(id=id)
    form = TaskForm(request.POST or None, instance=task)

    if form.is_valid():
        form.save()
        return redirect('list')

    return render(request, 'update.html', {'form': form, 'task': task})


@login_required
def delete(request, id):
    task = Task.objects.get(id=id)

    if request.method == 'POST':
        task.delete()
        return redirect('list')

    return render(request, 'confirm_delete.html', {'task': task})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})
