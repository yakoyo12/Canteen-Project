from django.shortcuts import render
from django.http import HttpResponse
from .models import Canteen

def home(request):
    canteen = Canteen.objects.all()
    return render(request, 'home.html', {'canteen': canteen})
