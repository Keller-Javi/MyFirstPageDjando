from django.urls import path
from . import views

urlpatterns = [
    path('', views.sesion, name="sesion"),
    path('home/', views.index, name="home"),
#    path('hello/<str:username>', views.hello),
    path('about/', views.about, name="about"),
    path('projects/', views.projects, name="projects"),
    path('create_project/', views.create_project, name="create_project"),
    path('projects/<int:id>', views.detail_project, name="detail_project"),
    path('delete_projects/<int:id>', views.delete_project, name="delete_project"),
    path('tasks/', views.tasks, name="tasks"),
    path('create_tasks/', views.create_task, name="create_tasks"),
    path('delete_tasks/<int:id>', views.delete_task, name="delete_task"),
    path('done_tasks/<int:id>', views.done_task, name="done_task"),
]
