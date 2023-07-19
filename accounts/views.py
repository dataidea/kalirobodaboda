from .models import User
from pathlib import Path
from .forms import SignUpForm
from django.db.models import Q
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate

# Create your views here.
BASE_DIR = Path(__file__).resolve().parent.parent

# Handle sign in request


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            template_name = 'kaliroboda/dashbord.html'
        else:
            # in case authentication failed
            context = {'error': 'Invalid username or password',
                       'message': 'Login failed, please go back and check password or username. If problem persists, contact admin for help.'}
            template_name = 'accounts/error.html'
    else:
        # incase of a get request
        context = {}
        template_name = 'accounts/signin.html'
    return render(request=request, template_name=template_name, context=context)

# handle signup


def signup(request):
    if request.method == 'POST':
        signup_form = SignUpForm(request.POST, request.FILES)
        if signup_form.is_valid():
            user = signup_form.save()
            login(request, user)
            context = {}
            template_name = 'kaliroboda/dashbord.html'
        else:
            # incase user creation fails
            context = {'error': "Cannot Create User",
                       'message': 'An error occured while creating user, please try again. If the problem persists, contact admin for assistance'}
            template_name = 'kaliroboda/error.html'
    else:
        # for get request
        signup_form = SignUpForm()
        context = {'signup_form': signup_form}
        template_name = 'accounts/signup.html'
    return render(request=request, template_name=template_name, context=context)

# handle signout


def signout(request):
    logout(request)
    context = {}
    template_name = 'kaliroboda/home.html'
    return render(request=request, template_name=template_name, context=context)

# handle profile request


def profile(request):
    # get id sent as query on url string
    user_id = request.GET.get('user_id')
    if user_id:
        try:
            # try finding the user
            user_profile = User.objects.get(id=user_id)
            context = {'user_profile': user_profile}
            template_name = 'accounts/profile.html'
        except User.DoesNotExist as e:
            # incase no user with the id is found
            context = {'error': 'No user info', 'message': e}
            template_name = 'kaliroboda/error.html'
    else:
        # if invalid user id has been provided on the url string
        context = {'error': 'Error catching requested user',
                   'message': 'The user id provided in the query seems invalid, contact admin for assistance'}
        template_name = 'kaliroboda/error.html'
    return render(request=request, template_name=template_name, context=context)

# handle settings request


def settings(request):
    try:
        user = User.objects.get(id=request.user.id)
        context = {'user': user}
        template_name = 'accounts/settings.html'
    except User.DoesNotExist as e:
        context = {'error': 'UserDoesNotExist',
                   'message': f'{e} Check if you are signed in.'}
        template_name = "kaliroboda/error.html"
    return render(request=request, template_name=template_name, context=context)

# handle forgot password request


def forgotPassword(request):
    context = {}
    template_name = 'accounts/forgot_password.html'
    return render(request=request, template_name=template_name, context=context)

# handle user table request


def userTable(request):
    users = User.objects.all().order_by('first_name')
    context = {'users': users}
    template_name = 'accounts/user_table.html'
    return render(request=request, template_name=template_name, context=context)

# handle user search


def userSearch(request):
    # get query from form submission url
    query = request.GET.get('query')
    if query:
        # find all users with the parameters containing the query
        results = User.objects.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(
                email__icontains=query) | Q(username__icontains=query)
        )
        context = {'users': results, 'query': query}
        template_name = 'accounts/user_table.html'
    else:
        # in case no query was provided
        context = {'users': [], 'query': query}
        template_name = 'accounts/user_table.html'
    return render(request=request, template_name=template_name, context=context)
