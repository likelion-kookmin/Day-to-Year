from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model, authenticate, login, logout
from .forms import *
from .models import User

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

def find_user(request):
    if request.method == "POST":
        phone_num = request.POST['phone_num']
        print("aa",phone_num)
        user_information = User.objects.filter(phone_num = phone_num)
        return render(request, 'finduserlist.html',{'user_information':user_information})
    else:
        return render(request,'finduser.html')

def myaccount(request) :
    return render(request, 'account_main.html')

def profile(request) :
    return render(request, 'account_profile.html')

def mypost(request) :
    return render(request, 'account_mypost.html')

def like(request) :
    return render(request, 'account_like.html')

def myinfo(request) :
    users = User.objects.all()
    return render(request, 'account_myinfo.html', {'users' : users})

def myinfo_update(request) :
    if request.method == 'POST' :
        user_change_form = CustomUserChangeForm(request.POST, instance = request.user)

        if user_change_form.is_valid() :
            user_change_form.save()
            messages.success(request, '회원정보가 수정되었습니다.')
            return render(request, 'myinfo.html')
        else :
            user_change_form = CustomUserChangeForm(instance = request.user)
            return render(request, 'myinfo_update.html', {'user_change_form' : user_change_form})