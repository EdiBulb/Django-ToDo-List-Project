from django.shortcuts import render, redirect
from .models import Task

def task_list(request):
    tasks = Task.objects.all()  # 모든 할 일 조회
    return render(request, 'todo/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)  # 할 일 추가
        return redirect('task_list')
    return render(request, 'todo/add_task.html')
