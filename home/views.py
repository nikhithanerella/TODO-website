from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from home.models import Task
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.views.decorators.cache import never_cache
# Home view for adding tasks


def home(request):
    context = {'success': False, 'name': request.user.username}
    user = authenticate(request, username=email, password=password) 
    print(user) # 'username' is passed to authenticate
    if request.method=='POST':
        title = request.POST.get('title')  # Using .get() to avoid key errors
        desc = request.POST.get('desc') 
          # Ensure both title and description are provided
        ins = Task(tasktitle=title, taskdesc=desc,user=user)
        print(user)
        ins.save()
        context = {'success': True}
    return render(request, 'index.html', context)

# View for displaying all tasks
def tasks(request):
    #user = authenticate(request, username=email, password=password)  # 'username' is passed to authenticate
    print(user)
    #allTasks = Task.objects.all()
    allTasks = Task.objects.filter(user=user)
    print(User.username)
    print(allTasks)
    context = {'tasks': allTasks}
    return render(request, 'tasks.html', context)

def signup(request):
    context={'success':False}
    if request.method=="POST":
            global email,password,username,user
            username=request.POST.get('username')
            email=request.POST.get('email')
            password=request.POST.get('password')
            print(username,email,password)
            user=User.objects.create_user(username,email,password)
            user.save()
            print(user)
            if user is not None:  # Log the user in
               context = {"success": True}
               return redirect('login')
            else:
               context = {"success": False,'error':"User already exist"} 
    return render(request,'signup.html',context)
    
    
@never_cache       
def login(request):
    context = {"success": False}
    if request.method == "POST":
        global email,password,user
        email = request.POST.get('email')  # Get email from POST data
        password = request.POST.get('password')  # Get password from POST data
        # Find user by email (assuming you're using email for login)
        user = authenticate(request, username=email, password=password) 
        print(user) # 'username' is passed to authenticate
        if user is not None:  # Log the user in
            context = {"success": True}
            return redirect('home')  # Redirect to the home page upon successful login
        else:
            context = {"success": False, 'error': "Invalid username or password"}
    
    return render(request,'login.html',context)

def logouts(request):
     print("yes")
     if request.method=='POST':
         print("yes")
         logout(request)
         print("yes")
         return redirect('login')
     return render(request,'out.html')
# Task deletion view using Django's generic DeleteView
class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks')  # Redirect to tasks page after successful deletion
    context_object_name = 'task'
    template_name = 'task_deletion.html'