from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', TaskList.as_view(), name = 'task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUptate.as_view(), name='task-update'),
    path('task-delete/<int:pk>', TaskDelete.as_view(), name='task-delete'),
]