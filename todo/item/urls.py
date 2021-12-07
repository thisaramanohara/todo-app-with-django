from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('', views.todoView),
    path('addTodo/', views.addTodo),
    path('deleteTodo/<int:todo_id>/', views.deleteTodo)
]
