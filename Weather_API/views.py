from django.shortcuts import render
from django.http import HttpResponse
import requests





def home(request):
    response = requests.get('http://api.weatherstack.com/current?access_key=7acd28610f38c96b91bea304b1f20af7&query=India').json()
    return render(request, 'index.html',{'response': response})

def home1(request):
    response = requests.get('http://api.weatherstack.com/current?access_key=7acd28610f38c96b91bea304b1f20af7&query=India').json()
    return render(request, 'index.html',{'response': response})
