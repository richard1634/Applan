"""applan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

#
from pages.views import home_view, contact_view, about_view
from django.contrib.auth import views as auth_views
from users.views import register_view, profile_view
from task.views import task_detail_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name = 'home'),
    path('contact/',contact_view, name = 'contact'),
    path('about/', about_view, name = 'about'),

    path('register/', register_view, name = 'register'),

    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'),name = 'logout'),
    path('profile/', profile_view,name = 'profile'),
 
    path('task/', task_detail_view,name = 'task'),

]