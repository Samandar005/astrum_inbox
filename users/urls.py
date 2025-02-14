from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'users'

urlpatterns = [
    path('logout/', auth_views.LogoutView.as_view(
        next_page='users:login',
    ), name='logout'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.UserLoginView.as_view(), name='login'),
]