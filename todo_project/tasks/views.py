from django.shortcuts import render
from .models import Task
# Create your views here.

def task_list(request):
    tasks = Task.objects.all()
    context = {'tasks':tasks}
    return render(request, 'tasks/task_list.html', context)

# create view for detail
def task_detail(request, pk):
    task = Task.objects.get(id=pk)
    context = {'task':task}
    return render(request, 'tasks/task_detail.html', context)


