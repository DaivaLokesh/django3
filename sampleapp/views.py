from django.shortcuts import render
from .models import Student
# Create your views here.
def home(request):
    return render(request,'home.html')

def addstudent(request):
    if request.method=='POST':
        name=request.POST['name']
        course=request.POST['course']
        fees=request.POST['fees']
        student=Student(name=name,course=course,fees=fees)
        student.save()
        return render(request,'add_student.html',{'flag':True})
    return render(request,'add_student.html')