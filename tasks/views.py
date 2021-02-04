from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

# Create your views here.


class TaskView():
    def list(request):
        tasks = Task.objects.all()
        return render(request, 'list.html', {'tasks': tasks})

    def create(request):
        form = TaskForm(request.POST or None)

        if form.is_valid():
            form.save()
            return redirect('list')

        return render(request, 'create.html', {'form': form})

    def update(request, id):
        task = Task.objects.get(id=id)
        form = TaskForm(request.POST or None, instance=task)

        if form.is_valid():
            form.save()
            return redirect('list')

        return render(request, 'update.html', {'form': form, 'task': task})

    def delete(request, id):
        task = Task.objects.get(id=id)

        if request.method == 'POST':
            task.delete()
            return redirect('list.html')

        return render(request, 'confirm_delete.html', {'task': task})

    def stylesheet(request, file):
        return render(request, 'assets/css/' + file + '.css', {}, content_type='text/css')

    def scripts(request, file):
        return render(request, 'assets/js/' + file + '.js', {}, content_type='application/javascript')
