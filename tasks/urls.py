from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_list, name='list-list'),
    path('list/add/', views.list_create, name='list-add'),
    path('list/<int:list_id>/', views.task_list, name='task-list'),
    path('task/add/', views.task_create, name='task-add'),
    path('task/<int:pk>/', views.task_detail, name='task-detail'),
    path('task/<int:pk>/edit/', views.task_update, name='task-edit'),
    path('task/<int:pk>/delete/', views.task_delete, name='task-delete'),
]