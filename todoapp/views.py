from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm, UpdateTaskForm
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    # Filter todos for the logged-in user
    todos = Task.objects.filter(user=request.user)
    count_todos = todos.count()

    completed_todo = todos.filter(complete=True)
    count_completed_todo = completed_todo.count()
    uncompleted = count_todos - count_completed_todo

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            # Associate the task with the current user
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('todoapp:todos-list')
    
    else:
        form = TaskForm()
    
    context = {
        'todos': todos,
        'form': form,
        'count_completed_todo': count_completed_todo,
        'uncompleted': uncompleted,
    }

    return render(request, 'todoapp/index.html', context)

def update(request, pk):
    todo = Task.objects.get(Task, pk=pk, user= request.user)
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
    task = Task.objects.get(Task, pk=pk, user= request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'todoapp/delete_task.html')


def toggle_todo(request, pk):
    todo = get_object_or_404(Task, pk=pk, user= request.user)
    todo.complete = not todo.complete
    todo.save()
    return redirect('todoapp:todos-list')  # Correct redirect