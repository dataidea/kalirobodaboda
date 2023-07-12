from django.shortcuts import render
from accounts.models import User
from accounts.models import Member
from locations.models import District
from locations.models import Stage

def home(request):
    return render(request, 'kaliroboda/home.html')

def dashbord(request):
    users = User.objects.all()
    members = Member.objects.all()
    districts = District.objects.all()
    stages = Stage.objects.all()
    
    context = {
        'sample_users': users[:5],
        'total_users': users.count(),
        'sample_members': members[:5],
        'total_members': members.count(),
        'sample_districts': districts,
        'total_districts': districts.count(),
        'sample_stages': stages,
        'total_stages': stages.count(),
    }

    return render(request=request, template_name='kaliroboda/dashbord.html', context=context)

def charts(request):
    return render(request=request, template_name='kaliroboda/charts.html', context={})

def pageNotFound(request, exception):
    return render(request=request, template_name='kaliroboda/404.html', context={})

def serverError(request):
    return render(request=request, template_name='kaliroboda/500.html', context={})
