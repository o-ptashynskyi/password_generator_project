from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.

def home(request):
    return render(request, template_name='generator/home.html')

def about(request):
    return render(request, template_name='generator/about.html')


def password(request):

    length = int(request.GET.get('length', 12)) # получение длині пароля с формі ввода
    chars = 'abcdefghijklmnopqrstuvwxyz'
    chars_latin_lower = list('abcdefghijklmnopqrstuvwxyz')
    chars_latin_upper = list(chars.upper())
    numbers = list('0123456789')
    special = list('/\*-+!?<>$%^&')
    generated_password = ''
    if request.GET.get('uppercase'):
        chars_latin_lower.extend(chars_latin_upper)
    if request.GET.get('numbers'):
        chars_latin_lower.extend(numbers)
    if request.GET.get('special'):
        chars_latin_lower.extend(special)

    for x in range(length):
        generated_password += random.choice(chars_latin_lower)



    return render(request, template_name='generator/password.html', context={'password': generated_password})
