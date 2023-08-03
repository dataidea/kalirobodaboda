from .models import Member
from django.db.models import Q
from django.shortcuts import render
from django.shortcuts import redirect
from companyinfo.models import CompanyInfo

# Create your views here.


def fetchCompanyInfo():
    try:
        company_info = CompanyInfo.objects.values()[0]
    except Exception as e:
        company_info = {}
    return company_info


def profile(request):
    # get id sent as query on url string
    company_info = fetchCompanyInfo()
    member_id = request.GET.get('member_id')
    if member_id:
        try:
            # try finding the member
            member_profile = Member.objects.get(id=member_id)
            context = {'company_info': company_info,
                       'member_profile': member_profile}
            template_name = 'accounts/profile.html'
        except Member.DoesNotExist as e:
            # incase no member with the id is found
            context = {'company_info': company_info,
                       'error': 'No member info', 'message': e}
            template_name = 'kaliroboda/error.html'
    else:
        # if invalid member id has been provided on the url string
        context = {'company_info': company_info, 'error': 'Error catching requested member',
                   'message': 'The member id provided in the query seems invalid, contact admin for assistance'}
        template_name = 'kaliroboda/error.html'
    return render(request=request, template_name=template_name, context=context)

# handle settings request


def memberTable(request):
    # members = Member.objects.all().order_by('first_name')
    # context = {'members': members}
    company_info = fetchCompanyInfo()
    context = {'company_info': company_info}
    template_name = 'accounts/member_table.html'
    return render(request=request, template_name=template_name, context=context)

# handle member search


def memberSearch(request):
    # get query from form submission url

    query = request.GET.get('query')
    if query:
        company_info = fetchCompanyInfo()
        # find all members with the parameters containing the query
        results = Member.objects.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(
                email__icontains=query) | Q(card_id__icontains=query)
        )
        context = {'company_info': company_info,
                   'members': results, 'query': query}
        template_name = 'accounts/member_table.html'
    else:
        # in case no query was provided
        context = {'company_info': company_info, 'members': [], 'query': query}
        template_name = 'accounts/member_table.html'
    return render(request=request, template_name=template_name, context=context)
