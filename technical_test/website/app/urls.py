from django.contrib import admin
from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('registration/', views.reg, name='Home-Page'),
    path('registration/reg/' or 'reg/', views.reg_verification, name="reg_verification"),
    path('registration/reg/verify/' or '/reg/verify/' or 'verify/', views.verify, name="verify"),
    path('/reg/verify/', views.verify, name="verify2"),
    path('verify/', views.verify, name="verify3"),
    path('login_validation/', views.login_validation, name='login_validation'),
    path('registration/reg/verify/login_validation/', views.login_validation, name='login_validation2'),
    path('login_validation/contact_us/', views.contact_us, name='contact_us'),
    path('registration/reg/verify/contact_us/', views.contact_us, name='contact_us2'),
    path('contact_us/', views.contact_us, name='contact_us3'),
    path('registration/reg/verify/contact_us/query/', views.query, name='query'),
    path('contact_us/query/', views.query, name='query'),

]