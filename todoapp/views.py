from django.shortcuts import render, redirect, get_object_or_404
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
        if form.is_valid():  # Added parentheses here
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


def toggle_todo(request, pk):
    todo = get_object_or_404(Task, pk=pk)
    todo.complete = not todo.complete
    todo.save()
    return redirect('todoapp:todos-list')  # Correct redirect