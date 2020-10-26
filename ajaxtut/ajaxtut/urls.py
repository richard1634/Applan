"""ajaxtut URL Configuration

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

from django.contrib.auth.decorators import login_required
from django.contrib import admin
from django.urls import path
from crud_ajax import  views 
from graphs import views as views2

from django.conf.urls import url
#
from pages.views import home_view, contact_view, about_view
from django.contrib.auth import views as auth_views
from users.views import register_view, profile_view
from task.views import task_create_view,task_delete_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task_manager/', login_required(views.CrudView.as_view()), name='crud_ajax'),
    path('ajax/crud/create/',  views.CreateCrudUser.as_view(), name='crud_ajax_create'),
    path('ajax/crud/update/',  views.UpdateCrudUser.as_view(), name='crud_ajax_update'),
    path('ajax/crud/delete/',  views.DeleteCrudUser.as_view(), name='crud_ajax_delete'),
    path('ajax/crud/timer/',    views.TimeCrudUser.as_view(),  name='crud_ajax_time'),
    path('ajax/crud/pause/',    views.PauseCrudUser.as_view(),  name='crud_ajax_pause'),
    path('ajax/crud/calc/',    views.CalcCrudUser.as_view(),  name='crud_ajax_calc'),
    path('ajax/crud/reset_timers/',    views.ResetAllTimersCrudUser.as_view(),  name='crud_ajax_reset'),


    path('graphs/',    views2.graph_view,  name='show_graph'),

    path('', home_view, name = 'home'),
    path('contact/',contact_view, name = 'contact'),
    path('about/', about_view, name = 'about'),

    path('register/', register_view, name = 'register'),

    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'),name = 'logout'),
    path('profile/', profile_view,name = 'profile'),
 
    path('create/', task_create_view, name = 'create'),
    url(r'^delete-entry/(?P<id>\d+)/$', task_delete_view, name='delete'),
]
