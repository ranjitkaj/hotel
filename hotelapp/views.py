from django.shortcuts import render
from .models import *


def index(request):
    if request.method == 'POST':
        a = register()
        a.check_in = request.POST['check_in']
        a.check_out = request.POST['check_out']
        a.adults = request.POST['adults']
        a.childs = request.POST['childs']
        a.rooms = request.POST['rooms']

        a.save()
    return render(request, 'index.html')

def index(request):
    if request.method == 'POST':
        b = massege()
        b.name = request.POST['name']
        b.email = request.POST['email']
        b.number = request.POST['number']
        b.msg = request.POST['msg']
        b.save()
    return render(request, 'index.html')
    
    


    
# Create your views here.
