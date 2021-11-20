from fitapp.forms import UserInfoForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from fitapp.models import UserModels
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

# ================================= FITTURE HOME PAGE FUNCTIONALITIES =====================================

def fitture(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def user_signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        userinfo = UserInfoForm(request.POST)
        userprofile = UserProfileForm(request.POST)
        if userinfo.is_valid() and userprofile.is_valid():
            user = userinfo.save()
            user.set_password(user.password)
            user.save()
            profile = userprofile.save(commit=False)

            profile.user = user
            profile.save()

            return render(request, 'login.html')

    else:
        userinfo = UserInfoForm()
        userprofile = UserProfileForm()
    return render(request, 'signup.html', {'form1':userinfo, 'form2':userprofile})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user and user.is_active:
            login(request, user)
            return HttpResponseRedirect(reverse('fitapp:user-account'))

        else:
                # If account is not active:
                return HttpResponse("Your account is not active.")

    else:
        pass
        #Nothing has been provided for username or password.
        return render(request, 'login.html', {})

# ================================= USER ACCOUNT HOME PAGE FUNCTIONALITIES =====================================

def home(request):
    return render(request, 'user_account.html')

def settings(request):
    return render(request, 'user-settings.html')

def us(request):
    return render(request, 'us.html')

def dashboard(request):
    return render(request, 'dashboard.html')


@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('landing-page'))

# def user_page(request, username):
#     user = UserModels.objects.all()
#     print(username)
#     # for acc in len(user):
#     #     if user[acc].user.username == username:
#     return render(request, 'user_home.html')
