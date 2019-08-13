from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

# Create your views here.
    
def get_todo_list(request):
    results = Item.objects.all()
    return render(request, 'todo_list.html', {'Items': results})
    
def create_an_item(request):
    return render(request, "")