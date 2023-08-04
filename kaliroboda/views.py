import csv
from accounts.models import Member
from django.shortcuts import render
from django.http import HttpResponse
from companyinfo.models import Leader
from companyinfo.models import Service
from companyinfo.models import CompanyInfo
from companyinfo.models import FrequentlyAskedQuestion


def fetchCompanyInfo():
    try:
        company_info = CompanyInfo.objects.values()[0]
        print({'company_info': company_info})
    except Exception as e:
        company_info = {}
    return company_info


def getStats(request):
    try:
        members = Member.objects.all()
        districts = []
        stages = []
        for member in members:
            if member.district.lower() not in districts:
                districts.append(member.district.lower())
            if member.stage.lower() not in stages:
                stages.append(member.stage.lower())

        context = {
            'total_members': members.count(),
            'total_districts': len(districts),
            'total_stages': len(stages),
        }
    except Exception as e:
        context = {'error': e,
                   'message': 'Sorry, a problem occured while fetching members from the database. Please refresh this page, if the problem persists, contact the admin for help.'}
        template_name = 'kaliroboda/error.html'
        return render(request=request, template_name=template_name, context=context)
    return context

# handle home page request


def home(request):
    services = Service.objects.all()
    company_info = fetchCompanyInfo()
    leaders = Leader.objects.all()
    context = {'title': 'Home',
               'company_info': company_info, 'services': services, 'leaders': leaders}
    template_name = 'kaliroboda/home.html'
    return render(request=request, template_name=template_name, context=context)

# handle dashbord request


def dashbord(request):
    context = getStats(request=request)
    company_info = fetchCompanyInfo()

    if context:
        context['company_info'] = company_info
        template_name = 'kaliroboda/dashbord.html'
    else:
        # in case the fetch was not successful
        context = {'error': 'Error 502',
                   'message': 'Company info could not be fetched right now, please refresh or contact technician'}
        template_name = 'kaliroboda/error.html'
    return render(request=request, template_name=template_name, context=context)


def faqs(request):
    company_info = fetchCompanyInfo()
    faqs = FrequentlyAskedQuestion.objects.all()
    context = {'faqs': faqs, 'company_info': company_info}
    template_name = 'kaliroboda/faqs.html'
    return render(request=request, template_name=template_name, context=context)


def pageNotFound(request, exception):
    company_info = fetchCompanyInfo()
    context = {'company_info': company_info}
    template_name = 'kaliroboda/404.html'
    return render(request=request, template_name=template_name, context=context)


def serverError(request):
    company_info = fetchCompanyInfo()
    context = {'company_info': company_info}
    template_name = 'kaliroboda/500.html'
    return render(request=request, template_name=template_name, context=context)


def export_csv(request):
    table = request.GET.get('table')
    company_info = fetchCompanyInfo()
    response = HttpResponse(content_type='text/csv')

    if table == 'members':
        response['Content-Disposition'] = 'attachment; filename="member_table.csv"'
        writer = csv.writer(response)
        writer.writerow(['Card Id', 'FirstName', 'LastName', 'Title', 'Status', 'District',
                         'Village', 'Stage', 'PhoneNumber'])
        for member in Member.objects.all().values_list('card_id', 'first_name', 'last_name', 'title', 'status', 'district', 'village', 'stage', 'phone_number'):
            writer.writerow(member)

    else:
        context = {'company_info': company_info}
        template_name = 'kaliroboda/export.html'
        return render(request=request, template_name=template_name, context=context)

    return response
