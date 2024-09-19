"""
URL configuration for django_signals project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from users.views import create_user_view_q1,create_user_view_q2,create_user_view_q3
from shapes.views import rectangle_info


urlpatterns = [
    path('admin/', admin.site.urls),
    path('create-user1/',create_user_view_q1),
    path('create-user2/',create_user_view_q2),
    path('create-user3/',create_user_view_q3),
    path('rectangle', rectangle_info, name='rectangle_info'),

]
