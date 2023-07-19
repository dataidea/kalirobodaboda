import csv
from accounts.models import User
from accounts.models import Member
from locations.models import Stage
from django.shortcuts import render
from locations.models import District


# fetch all users

def fetchAll():
    try:
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
    except Exception as e:
        context = {'error': e,
                   'message': 'Sorry, a problem occured while fetching users from the database. Please refresh this page, if the problem persists, contact the admin for help.'}
    return context

# handle home page request


def home(request):
    context = {}
    template_name = 'kaliroboda/home.html'
    return render(request=request, template_name=template_name, context=context)

# handle dashbord request


def dashbord(request):
    context = fetchAll()
    if context['sample_users']:
        # if context includes sample users (fetched users)
        template_name = 'kaliroboda/dashbord.html'
    else:
        # in case the fetch was not successful
        template_name = 'kaliroboda/error.html'
    return render(request=request, template_name=template_name, context=context)


def charts(request):
    context = fetchAll()
    if context['sample_users']:
        template_name = 'kaliroboda/charts.html'
    else:
        template_name = 'kaliroboda/error.html'
    return render(request=request, template_name=template_name, context=context)


def pageNotFound(request, exception):
    return render(request=request, template_name='kaliroboda/404.html', context={})


def serverError(request):
    return render(request=request, template_name='kaliroboda/500.html', context={})


def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="user_table.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'First Name', 'Last Name', 'Email', 'Phone', 'Gender', 'Date of Birth'])

    for prediction in Prediction.objects.all().values_list(
            'id', 'prediction', 'confidence', 'location', 'time', 'date', 'image'):
        writer.writerow(prediction)

    return response
