from django.shortcuts import render
from.models import products
# Create your views here.
from django.http import HttpResponse
def index(request):
    x=products.objects.all()
    return render(request,'index.html',{'x': x})
def about(request):
    return HttpResponse("<h1>About page</h1>")
