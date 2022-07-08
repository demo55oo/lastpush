from django.urls import path

from .import views

urlpatterns =[
     path('', views.verify_dns_view, name="home"),
]