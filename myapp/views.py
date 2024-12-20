from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    students=student.objects.all()
    Games=Game.objects.all()

    return render(request,'index.html',{'students':students, 'Games':Games})