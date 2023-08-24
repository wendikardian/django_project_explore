from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    # create path to detail
    path('tasks/<int:pk>/', views.task_detail, name='task_detail'),
]