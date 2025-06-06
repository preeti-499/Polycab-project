"""
URL configuration for polycab project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from polycabmanage import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.admin_login, name='login'),
    # path('user/',views.user_login, name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
    path('admindash',views.dashboard,name='admindash'),
    path('task',views.task,name='task'),
    path('admin.html', views.admin_dashboard, name='admin_dashboard'),
    path('user_dashboard', views.user_dashboard, name='user_dashboard'),
    path('add',views.add_user,name='add_user'),
    path('user/update/<int:user_id>/', views.update_user, name='update_user'),
    path('user/delete/<int:user_id>/', views.delete_user, name='delete_user'),
    path('addtask',views.addtask,name='addtask'),
    path('task/update/<int:pk>/', views.task_update, name='task_update'),
    path('task/delete/<int:pk>/', views.task_delete, name='task_delete'),
]

