from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm, UpdateTaskForm

def index(request):
    todos = Task.objects.all()
    count_todos = todos.count()

    completed_todo = Task.objects.filter(complete=True)
    count_completed_todo = completed_todo.count()
    uncompleted = count_todos - count_completed_todo

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/')
    
    else:
        form = TaskForm()
    context= {
        'todos': todos,
        'form': form,
        'count_completed_todo': count_completed_todo,
        'uncompleted': uncompleted,
    }

    return render(request, 'todoapp/index.html', context)



def update(request, pk):
    todo = Task.objects.get(id=pk)
    if request.method == "POST":
        form = UpdateTaskForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UpdateTaskForm(instance=todo)
    context= {
        'form': form
    }
    return render(request, 'todoapp/update_task.html', context)


def delete(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'todoapp/delete_task.html')