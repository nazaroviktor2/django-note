from .models import Task
from django.forms import ModelForm, TextInput, Textarea


class TaskForm(ModelForm):
    class Meta:
        model = Task
        
        fields = ["title",'task']
        widjets = {"title":TextInput( attrs={
            'class':'form-control',
            'placeholder':'Ввидете название'
        }),
        'task':Textarea( attrs={
            'class':'form-control',
            'placeholder':'Ввидете описание'
        }),
       
        


        }