from django.urls import path
from .views import index, update,delete

app_name = 'todoapp'

urlpatterns = [
    path('', index, name="todos-index"),
    path('update/<int:pk>/', update, name='todos-update'),
    path('delete/<int:pk>/', delete, name='todos-delete'),
]
