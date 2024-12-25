from django.shortcuts import render
from home.models import Task
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from home.models import Task


# Create your views here.
def home(request):
    context={'success':False,'name':'nikhitha'}
    if request.method=="POST":
        title=request.POST['title']
        desc=request.POST['desc']
        print(title,desc)
        ins=Task(tasktitle=title,taskdesc=desc)
        ins.save()
        context={'success':True}
    
    return render(request,'index.html',context)
def tasks(request):
    allTasks=Task.objects.all()
    #print(allTasks)
    #for item in allTasks:
        #print(item.tasktitle)
    context={'tasks':allTasks}
    return render(request,'tasks.html',context)

class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks')
    context_object_name = 'task'
    template_name = 'task_deletion.html'