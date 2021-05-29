from django.contrib.auth.forms import  UserCreationForm
from .models import User

class RegisterForm(UserCreationForm):
    class Mets:
        model = User
        fields = ['username', 'password1', 'password2', 'nickname', 'location', 'phone_num', 'profile_img']
        
