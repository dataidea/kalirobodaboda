from django.shortcuts import render

def home(request):
    return render(request, 'kaliroboda/home.html')

def dashbord(request):
    return render(request=request, template_name='kaliroboda/dashbord.html')

def charts(request):
    return render(request=request, template_name='kaliroboda/charts.html', context={})

def pageNotFound(request, exception):
    return render(request=request, template_name='kaliroboda/404.html', context={})

def serverError(request):
    return render(request=request, template_name='kaliroboda/500.html', context={})
