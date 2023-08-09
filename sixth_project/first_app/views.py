from django.shortcuts import render, redirect
from . import models
from first_app.forms import StudentForm

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            
    else:
        form = StudentForm()
        
    # std = StudentForm
    student = models.StudentModel.objects.all()
    
    return render ( request, 'home.html', {'data': student, 'form': form})

def delete_student(request, roll):
        std=models.StudentModel.objects.get(pk=roll).delete()
        context={
            "message":f"Deleted Successfully",
            }
        return redirect('homepage')
    