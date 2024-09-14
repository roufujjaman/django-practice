"""
URL configuration for CookieSessionProject project.

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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('set_cookie/<str:ckey>/<str:cval>/<int:days>', views.set_cookie, {'days': 7}, name='set_cookie'),
    path('get_cookie/', views.get_cookie, name='get_cookie'),
    path('del_cookie/<str:name>', views.delete_cookie, name='delete_cookie'),
    path('default/<str:name>/', views.default)
]
