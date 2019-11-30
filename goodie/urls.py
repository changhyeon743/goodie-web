"""goodie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from parsed_data import views

urlpatterns = [
    path('',views.BaseView.as_view(template_name='parsed_data/home.html')),
    path('trending',views.BaseView.as_view(template_name='parsed_data/trending.html')),
    path('most_liked',views.BaseView.as_view(template_name='parsed_data/most_liked.html')),
    path('well_community',views.BaseView.as_view(template_name='parsed_data/well_community.html')),

    #path('trending',views.HomeView(template = 'parsed_data/trending.html').as_view()),

    path('admin/', admin.site.urls),
    path('api/', include('parsed_data.urls')),
]
