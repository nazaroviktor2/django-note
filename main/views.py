from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


# Create your views here.
def index(request):
    tasks = Task.objects.order_by('-id')

    return render(request, "main/index.html",{'title':'гланая страница',
    'tasks':tasks})

def about(request):
    return render(request, "main/about.html")

def add(request):
    erorr = ''
    if request.method=="POST":
        form = Task( title= request.POST['name'], task = request.POST['textarea'] )
       
        form.save()
        return redirect('/')
       
    form = TaskForm()
    context = {
        'form':form,
        'title':'Добавить задачу',
        'error':erorr

    }
    return render(request, "main/add.html",context)
