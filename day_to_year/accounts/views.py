from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model, authenticate, login, logout
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

User = get_user_model()


# Create your views here.
def login_view(request):
    if request.method =='POST':
        form = AuthenticationForm(request = request, data= request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request = request, username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect('main')
            else:
                return redirect('login')
            
        


    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form':form})


    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect("login")

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES) #
        if form.is_valid(): #
            print("ddddd")
            user = form.save() #
            login(request, user) #
        return redirect("login")
    else:
        form = RegisterForm()
        return render(request, 'signup.html', {'form': form})

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('main')
        else:
            messages.error(request, 'please correct the error below')
    
    else:
        form = PasswordChangeForm(request.user)
    
    return render(request, 'change_password.html', {'form':form})

def myaccount(request) :
    return render(request, 'account_main.html')

def profile(request) :
    return render(request, 'account_profile.html')

def mypost(request) :
    return render(request, 'account_mypost.html')

def like(request) :
    return render(request, 'account_like.html')

def myinfo(request) :
    return render(request, 'account_myinfo.html')