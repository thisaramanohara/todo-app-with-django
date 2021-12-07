from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem

# Create your views here.


def addTodo(request):
    # create a new item and save it and redirect the browser to /todo
    c = request.POST['content']
    new_item = TodoItem(content=c)
    # OR ---> new_item = TodoItem(content = request.POST['content'])

    new_item.save()
    return HttpResponseRedirect('/todo/')


def deleteTodo(request, todo_id):
    item_to_delete = TodoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/')


def todoView(request):
    all_todo_items = TodoItem.objects.all()
    return render(request, 'todo.html', {'all_items': all_todo_items})
