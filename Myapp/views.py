from django.shortcuts import render
from django.http import HttpResponse

def atal(request):
	return render(request,'demo.html')

def kakaria(request):
	return render(request,'demo1.html')

def sidi(request):
	return render(request,'demo3.html')

def ahbd(request):
	return render(request,'demo4.html')

def home(request):
	return render(request,'demo5.html')

def contactus(request):
	return render(request,'demo2.html')

def aboutus(request):
	return render(request,'demo6.html')



# Create your views here.
