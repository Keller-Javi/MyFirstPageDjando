from django import forms
from .models import Project

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Title of task", max_length=200, required=True, widget=forms.TextInput(attrs={'class': 'input'}))
    description = forms.CharField(label="Description of task", required=False, widget=forms.Textarea(attrs={'class': 'input'}))

    projects_name = [[x+1, y.name] for x,y in enumerate(list(Project.objects.all()))] # [[1, projects1], [2, projects2], ..., [id, project]]

    project_id = forms.ChoiceField(label="Select a proyect:" ,widget=forms.RadioSelect, choices=projects_name, required=True) # al seleccionar un proyecto nos devuelve la id de ese

class CreateNewProject(forms.Form):
    name = forms.CharField(label="Project name", max_length=200, required=True, widget=forms.TextInput(attrs={'class': 'input'}))