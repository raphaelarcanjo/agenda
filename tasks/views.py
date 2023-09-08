from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Task, UserTask
from .forms import TaskForm, RegistrationForm
from datetime import datetime


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

    if request.POST == 'POST':
        if form.is_valid():
            task = form.save()
            user = request.user
            bridge = UserTask(user=user.id, task=task)
            bridge.save()
            messages.success(request, "Tarefa criada com sucesso!")
            return redirect('list')
        else:
            messages.error(request, "Erro ao criar a tarefa!")

    return render(request, 'create.html', {'form': form})


@login_required
def update(request, id):
    task = Task.objects.get(id=id)
    form = TaskForm(request.POST or None, instance=task)

    if request.POST == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Tarefa atualizada com sucesso!")
            return redirect('list')
        else:
            messages.error(request, "Erro ao atualizar a tarefa")

    return render(request, 'update.html', {'form': form, 'task': task})


@login_required
def delete(request, id):
    user = request.user
    usertask = UserTask.objects.get(user=user.id, task=id)
    task = Task.objects.get(id=id)

    if request.method == 'POST':
        usertask.delete()
        task.delete()
        messages.success(request, "Tarefa removida com sucesso!")
        return redirect('list')

    return render(request, 'confirm_delete.html', {'task': task})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Cadastro criado com sucesso!")
            return redirect('login')

        else:
            messages.error(request, "Cadastro criado com sucesso!")
    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})
