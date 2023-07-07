from django.shortcuts import render

def home(request):
    return render(request, 'kaliroboda/home.html')

def dashbord(request):
    return render(request=request, template_name='kaliroboda/dashbord.html')