from django.shortcuts import render

# Create your views here.
def signin(request):
    return render(request=request, template_name='accounts/signin.html', context={})

def signup(request):
    return render(request=request, template_name='accounts/signup.html', context={})

def forgotPassword(request):
    return render(request=request, template_name='accounts/forgot_password.html', context={})

def memberTable(request):
    return render(request=request, template_name='accounts/member_table.html')