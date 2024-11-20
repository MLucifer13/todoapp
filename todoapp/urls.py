from django.urls import path
from . import views

app_name = 'todoapp'

urlpatterns = [
    path('', views.index, name="todos-list"),
    path('update/<int:pk>/', views.update, name='todos-update'),
    path('delete/<int:pk>/', views.delete, name='todos-delete'),
    path('toggle/<int:pk>/', views.toggle_todo, name='todos-toggle'),
]
