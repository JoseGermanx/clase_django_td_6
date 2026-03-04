
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import dashboard, home, custom_logout

urlpatterns = [
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', custom_logout, name='logout')
]