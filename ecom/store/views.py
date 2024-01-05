from django.shortcuts import render

def home(requsest):
    return render(requsest, 'home.html', {})