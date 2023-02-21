from django.db import models

# Create your models here.
class Project(models.Model): # creamos una tabla llamada Project en la base de datos
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Task(models.Model): # esta es otra tabla
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)
            # indicamos que hay una relación entre las tablas
            # en el on_delete decimos que si se elimina el proyecto base se elimina las tareas
    
    def __str__(self):
        return self.title + ' (Project: ' + self.project.name + ')'
    
    def Done(self):
        self.done = True

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username