from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .forms import *
from .models import User

User = get_user_model()


# Create your views here.
def login_view(request):
    error=""
    if request.user.is_authenticated:
        return redirect('main')
    else:
        if request.method =='POST':
            form = AuthenticationForm(request = request, data= request.POST)
            if form.is_valid():
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password")
                user = authenticate(request = request, username = username, password = password)
                print("user",user, type(user))
                if user is None:
                    print('ddd')
                    error = "오류입니다"
                else:

                    login(request, user)
                    return redirect('main')
            else:
                error = "가입하지 않은 아이디이거나, 잘못된 비밀번호입니다"

        form = AuthenticationForm()
        print("dsafdsf")
        return render(request, 'login.html', {'form': form, 'error' : error})
    



def logout_view(request):
    logout(request)
    return redirect("login")

def register_view(request):
    if request.user.is_authenticated:
        return redirect('main')

    else:
        if request.method == "POST":
            form = RegisterForm(request.POST, request.FILES) #
            if form.is_valid(): #
                print("ddddd")
                user = form.save() #git 
                login(request, user) #
            return redirect("login")
        else:
            form = RegisterForm()
            return render(request, 'signup.html', {'form': form})

def change_password(request):
    if not request.user.is_authenticated:
        return redirect('main')
    else:

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
    myposts = request.user.rentals.all().order_by('id')[:3]
    mylikes = request.user.like.all().order_by('id')[:3]
    return render(request, 'account_main.html',{'myposts':myposts, 'mylikes':mylikes})

def profile(request, user_id) :
    users = User.objects.get(id = user_id)
    return render(request, 'account_profile.html', {'users' : users})

def mypost(request) :
    myposts = request.user.rentals.all()
    return render(request, 'account_mypost.html',{'myposts':myposts})

def mylike(request) :
    mylikes = request.user.like.all()
    return render(request, 'account_like.html',{'mylikes':mylikes})

def myinfo(request) :
    users = User.objects.all()
    return render(request, 'account_myinfo.html', {'users' : users})

def myinfo_update(request) :
    if request.method == 'POST' :
        user_change_form = CustomUserChangeForm(request.POST, instance = request.user)
        print(request.user)
        #print(user_change_form)
        if user_change_form.is_valid() :
            user = user_change_form.save()
            messages.success(request, '회원정보가 수정되었습니다.')
            print("success")
            return redirect('myinfo')
        else :
            user_change_form = CustomUserChangeForm(instance = request.user)
            print("fail")
            return render(request, 'myinfo_update.html', {'user_change_form' : user_change_form})
    else :
        return render(request, 'myinfo_update.html')

def profile_update(request) :
    
    if request.method == 'POST' :
        user = request.user
        profile_change_form = ProfileChangeForm(request.POST, request.FILES, instance = request.user)

        if profile_change_form.is_valid() :
            user = profile_change_form.save()
            messages.success(request, '프로필이 수정되었습니다.')
            print("success")
            return redirect('profile', user.id)
        else :
            profile_change_form = ProfileChangeForm(instance = request.user)
            print("fail")
            return render(request, 'profile_update.html', {'profile_change_form' : profile_change_form})
    else :
        return render(request, 'profile_update.html')
        

