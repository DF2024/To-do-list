from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Task

class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'task_list/task_list.html'


class TaskCreate(CreateView):
    model = Task
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('tasks')
    template_name = 'tareas/task_form.html'

class TaskUpdate(UpdateView):
    model = Task
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('tasks')
    template_name = 'tareas/task_form.html'

class TaskDelete(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
    template_name = 'tareas/task_confirm_delete.html'
