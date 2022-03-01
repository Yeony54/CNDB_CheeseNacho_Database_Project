from django.urls import path
from users import views
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # django 자체 로그인/로그아웃 기능(views.py X)
    path('signup/', views.signup, name='signup'),
    path('mypage/', views.mypage, name='mypage'),
]
