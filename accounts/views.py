from .models import User
from pathlib import Path
from django.db.models import Q
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from .forms import SignUpForm
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.password_validation import validate_password

# Create your views here.
BASE_DIR = Path(__file__).resolve().parent.parent


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
            template_name = 'accounts/signin.html'
            return render(request=request, template_name=template_name, context=context)
    else:
        template_name = 'accounts/signin.html'
        return render(request=request, template_name=template_name, context={})


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
        signup_form = SignUpForm(request.POST, request.FILES)
        if signup_form.is_valid():
            user = signup_form.save()
            login(request, user)
            return redirect('dashbord')
        else:
            context = {'error': "Cannot Create User",
                       'message': 'An error occured while creating user, please try again. If the problem persists, contact admin for assistance'}
            template_name = 'kaliroboda/error.html'
            return render(request=request, template_name=template_name, context=context)
    else:
        signup_form = SignUpForm()
        context = {'signup_form': signup_form}
        template_name = 'accounts/signup.html'
        return render(request=request, template_name=template_name, context=context)


# def signup(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         email = request.POST['email']
#         password = request.POST['password']
#         confirm_password = request.POST['confirm_password']
#         uploaded_display_picture = request.FILES.get('display_picture')
#         if uploaded_display_picture:
#             display_picture = uploaded_display_picture
#         else:
#             display_picture = User._meta.get_field(
#                 'display_picture').get_default()
#         # validate username and password
#         error_messages = validate_signup(username, password, confirm_password)

#         if error_messages:
#             context = {'error': error_messages}
#             template_name = 'accounts/signup.html'
#             return render(request=request, template_name=template_name, context=context)

#         password = make_password(password)
#         user = User.objects.create(username=username, first_name=first_name,
#                                    last_name=last_name, email=email, password=password, display_picture=display_picture)
#         user.save()
#         context = {}
#         template_name = 'kaliroboda/dashbord.html'
#         return render(request=request, template_name=template_name, context=context)

#     else:
#         context = {}
#         template_name = 'accounts/signup.html'
#         return render(request=request, template_name=template_name, context=context)


def signout(request):
    logout(request)
    return redirect('home')


def profile(request):
    template_name = 'accounts/profile.html'
    context = {}
    return render(request=request, template_name=template_name, context=context)


def settings(request):
    try:
        user = User.objects.get(id=request.user.id)
        context = {'user': user}
        template_name = 'accounts/settings.html'
        return render(request=request, template_name=template_name, context=context)
    except User.DoesNotExist as e:
        context = {'error': 'UserDoesNotExist',
                   'message': f'{e} Check if you are signed in.'}
        template_name = "kaliroboda/error.html"
        return render(request=request, template_name=template_name, context=context)


def forgotPassword(request):
    context = {}
    template_name = 'accounts/forgot_password.html'
    return render(request=request, template_name=template_name, context=context)


def userTable(request):
    users = User.objects.all()
    context = {'users': users}
    template_name = 'accounts/user_table.html'
    return render(request=request, template_name=template_name, context=context)


def userSearch(request):
    query = request.GET.get('query')
    if query:
        results = User.objects.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(
                email__icontains=query) | Q(username__icontains=query)
        )
        context = {'users': results, 'query': query}
        template_name = 'accounts/user_table.html'
    else:
        context = {'users': [], 'query': query}
        template_name = 'accounts/user_table.html'
    return render(request=request, template_name=template_name, context=context)
