from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .forms import CreateNewProject, CreateNewTask

from django.http import HttpResponse
from .models import Project, Task, User
from django.shortcuts import get_object_or_404, redirect, render # Si no existe el objecto buscado
# nos mustra una pagina de error 404

# Create your views here.
@csrf_exempt
def sesion(request):
    username = request.POST.get('username')
    pas = request.POST.get('password')
    band = request.POST.get('crear_cuenta')

    if band == '0':
        try:
            this_user = User.objects.get(username=username)

            if this_user.password == pas:
                return render(request, 'index.html', {'username': username})
            else:
                print('Contraseña incorrecta')
        except:
            print('Usuario no existe')
            messages.success(request, 'Usuario no existe')      

    elif band == '1':
        User(username=username, password=pas).save()
        return render(request, 'index.html', {'username': username})

    return render(request, "sesion.html")

def index(request, username=None):
    return render(request, "index.html", {'username': username})

def about(request):
    return render(request, "about.html")

def projects(request):
    projects = Project.objects.all()
    return render(request, "projects/projects.html", {'projects': projects})

def tasks(request):
    tasks = Task.objects.all()
    return render(request, "tasks.html", {'tasks': tasks})

def create_task(request):
    if request.method == 'GET':
        return render(request, "create_task.html", {
        'form': CreateNewTask()
    })
    else:
        Task.objects.create(title=request.POST.get('title'),
            description=request.POST.get('description'), project_id=request.POST.get('project_id'))
        return redirect('tasks')

def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', 
            {'form': CreateNewProject()})
    else:
        Project.objects.create(name=request.POST.get('name'))
        return redirect('projects')

def detail_project(request, id):
    project = Project.objects.get(id=id)
    tasks = list(Task.objects.filter(project_id=id))
    return render(request, 'projects/project_detail.html', {'project_name': project.name, 'tasks': tasks})

def delete_task(request, id):
    task = Task.objects.get(id=id)
    print(id, task.title)
    task.delete()

    return redirect('tasks')

def done_task(request, id):
    task = Task.objects.get(id=id)
    task.Done()
    task.save()

    return redirect('tasks')

def delete_project(request, id):
    project = Project.objects.get(id=id)
    project.delete()

    return redirect('projects')
