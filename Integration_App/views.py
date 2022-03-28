from django.shortcuts import render

# Create your views here.
from Integration_App.models import Student

def get_all_detail(request):
    student = Student.objects.all()
    return render(request,'student.html',{'student':student})
