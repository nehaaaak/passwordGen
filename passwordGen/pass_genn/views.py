from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import random

# Create your views here.

def home(request):  
    return render(request, 'home.html')

def passGen(request):
    char= list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        char.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('digits'):
        char.extend(list('0123456789'))
    if request.GET.get('symbols'):
        char.extend(list('@$#'))

    length= int(request.GET.get('length', 10))
    password= ""
    for x in range(length):
        password += random.choice(char)
    return render(request, 'pass.html', {'password':password})