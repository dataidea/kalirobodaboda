import csv
from accounts.models import Member
from locations.models import Stage
from django.shortcuts import render
from locations.models import District
from django.http import HttpResponse


def fetchAll(request):
    try:
        members = Member.objects.all()
        districts = District.objects.all()
        stages = Stage.objects.all()
        context = {
            'sample_members': members[:5],
            'total_members': members.count(),
            'sample_districts': districts,
            'total_districts': districts.count(),
            'sample_stages': stages,
            'total_stages': stages.count(),
        }
    except Exception as e:
        context = {'error': e,
                   'message': 'Sorry, a problem occured while fetching members from the database. Please refresh this page, if the problem persists, contact the admin for help.'}
        template_name = 'kaliroboda/error.html'
        return render(request=request, template_name=template_name, context=context)
    return context

# handle home page request


def home(request):
    context = {}
    template_name = 'kaliroboda/home.html'
    return render(request=request, template_name=template_name, context=context)

# handle dashbord request


def dashbord(request):
    context = fetchAll(request=request)
    if context['sample_members']:
        template_name = 'kaliroboda/dashbord.html'
    else:
        # in case the fetch was not successful
        template_name = 'kaliroboda/error.html'
    return render(request=request, template_name=template_name, context=context)


def faqs(request):
    context = {}
    template_name = 'kaliroboda/faqs.html'
    return render(request=request, template_name=template_name, context=context)


def pageNotFound(request, exception):
    context = {}
    template_name = 'kaliroboda/404.html'
    return render(request=request, template_name=template_name, context=context)


def serverError(request):
    context = {}
    template_name = 'kaliroboda/500.html'
    return render(request=request, template_name=template_name, context=context)


def export_csv(request):
    table = request.GET.get('table')
    response = HttpResponse(content_type='text/csv')

    if table == 'members':
        response['Content-Disposition'] = 'attachment; filename="member_table.csv"'
        writer = csv.writer(response)
        writer.writerow(['Card Id', 'FirstName', 'LastName', 'Title',
                         'Stage', 'Village', 'PhoneNumber'])
        for member in Member.objects.all().values_list('card_id', 'first_name', 'last_name', 'title',
                                                       'stage', 'village', 'phone_number'):
            writer.writerow(member)

    else:
        context = {}
        template_name = 'kaliroboda/export.html'
        return render(request=request, template_name=template_name, context=context)

    return response
