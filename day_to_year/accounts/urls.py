from django.urls import path, include
from .views import *

urlpatterns = [
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('signup/', register_view, name="signup"),
    path('finduser/', find_user, name="find_user"),
    path('myaccount/', myaccount, name="myaccount")
] 