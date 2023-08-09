from django import forms
from first_app.models import StudentModel

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        # fields = ['name', 'roll', 'father_name']
        fields = '__all__'
        labels = {
            'roll' : 'Student Roll',
            'name' : 'Student Name',
            'father_name' : 'Father Name',
        }
        
        # widgets ={
        #     'name' : forms.TextInput(attrs = {'class' :'btn-primary'}),
        # }
        