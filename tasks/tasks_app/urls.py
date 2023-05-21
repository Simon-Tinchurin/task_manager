from django.urls import path
from . import views

urlpatterns = [
    path('', views.log_in, name=''),
    path('register/', views.register, name='register'),
    path('log_out/', views.log_out, name='log_out'),
    path('tasks/', views.user_tasks, name='tasks'),
    path('delete/<int:task_id>/', views.delete_task, name='delete'),
    path('edit/<int:task_id>/', views.edit_task, name='edit'),
]
