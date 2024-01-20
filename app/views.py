from django.shortcuts import render

# Create your views here.
from app.models import *
from django.http import HttpResponse
from app.forms import *

def create_student(request):
    ESFO=Studentform()
    d={'ESFO':ESFO}
    if request.method=='POST':
        SFDO=Studentform(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('Studentform done')
        else:
            return HttpResponse('Invalid')
    return render(request,'create_student.html',d)