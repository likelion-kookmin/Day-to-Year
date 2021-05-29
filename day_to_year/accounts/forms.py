from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'nickname', 'location', 'phone_num', 'profile_img']
        
