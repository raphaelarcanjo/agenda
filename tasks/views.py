from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task, UserTask
from .forms import TaskForm, RegistrationForm
from datetime import datetime

# Create your views here.


@login_required
def list(request):
    user = request.user
    user_tasks = UserTask.objects.filter(user=user.id).values_list('task', flat=True)
    tasks = Task.objects.filter(id__in=user_tasks).all()
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
        task = form.save()
        user = request.user
        bridge = UserTask(user=user.id, task=task)
        bridge.save()
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
    user = request.user
    usertask = UserTask.objects.get(user=user.id, task=id)
    task = Task.objects.get(id=id)

    if request.method == 'POST':
        usertask.delete()
        task.delete()
        return redirect('list')

    return render(request, 'confirm_delete.html', {'task': task})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})
