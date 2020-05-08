from django.contrib import admin
from django.urls import path
from firstApp import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path('hi/', views.hi, name="hi"),
    path("hello/<str:name>", views.hello, name="hello"),
    path("rollno/<int:id>", views.rollno, name='rollno'),
    path("message/", views.message, name="message"),
    path("register/", views.register, name="register"),
    path("details/", views.details, name="userdetails"),
    path("login/", views.login, name="login"),
    path("score", views.score, name='score'),
    path('home', views.home,name = 'home'),
    path('restaurant',views.restaurant,name="restaurant"),
]
