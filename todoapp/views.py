
from urllib import request
from django.shortcuts import redirect, render
from .models import TodoItem
from django.shortcuts import get_object_or_404  

def home(request):
   if request.method == "POST":
        title = request.POST.get("task")
        if title:
            TodoItem.objects.create(title=title)

        return redirect("home")   # 👈 VERY IMPORTANT
   todos = TodoItem.objects.all()
   return render(request, "index.html", {"todos": todos})


def delete(request,pk):
    task=get_object_or_404(TodoItem,id=pk)
    task.delete()
    print(pk)
    return redirect('home')
def done(request,pk):
    task=get_object_or_404(TodoItem,id=pk)
    task.title="Done"
    task.save()
    return redirect('home')
def edit_task(request,pk):
    task=get_object_or_404(TodoItem,id=pk)
    if request.method=="POST":
        new_title=request.POST.get("task")
        task.title=new_title
        task.save()
        return redirect('home')
    return render (request,"edit.html",{"task":task})