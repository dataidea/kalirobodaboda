from django.shortcuts import render
from django.shortcuts import redirect
from .forms import UserForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db.models import Q
from .models import User
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError  

# Create your views here.
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashbord')
        else:
            context = {'error': 'Invalid username or password'}
            return render(request=request, template_name='accounts/signin.html', context=context)
    else:
        return render(request=request, template_name='accounts/signin.html', context={})

def validate_signup(username, password, confirm_password):
    error_messages = []

    if password != confirm_password:
        error_messages.append('Password does not match')

    try:
        UnicodeUsernameValidator()(username)
    except ValidationError as e:
        error_messages.append(e.messages)

    try:
        validate_password(password)
    except ValidationError as e:
        error_messages.append(e.messages)

    return error_messages

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # validate username and password
        error_messages = validate_signup(username, password, confirm_password)

        if error_messages:
            context = {'error': error_messages}
            return render(request=request, template_name='accounts/signup.html', context=context)
        
        password = make_password(password)
        user = User.objects.create(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
        user.save()
        context = {}
        return render(request=request, template_name='kaliroboda/dashbord.html', context=context)
    
    else:
        context = {}
        return render(request=request, template_name='accounts/signup.html', context=context)

def signout(request):
    logout(request)
    return redirect('home')

def profile(request):
    return render(request=request, template_name='accounts/profile.html', context={})

def settings(request):
    return render(request=request, template_name='accounts/settings.html', context={})

def forgotPassword(request):
    return render(request=request, template_name='accounts/forgot_password.html', context={})

def userTable(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request=request, template_name='accounts/user_table.html',context=context)

def userSearch(request):
    query = request.GET.get('query')
    if query:
        results = User.objects.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(email__icontains=query) | Q(username__icontains=query)
        )
        context = {'users': results, 'query': query}
    else:
        context = {'users': [], 'query': query}
    return render(request=request, template_name='accounts/user_table.html', context=context)