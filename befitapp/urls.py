from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from . import views
urlpatterns = [
    path('', views.home,name='home'),
    path('Login|Register', views.loginreg,name='loginreg'),
    path('Gainweight', views.gainw,name='gainw'),
    path('Looseweight', views.loosew,name='loosew'),
    path('Fitness Calculators', views.fitc,name='fitc'),
    path('Nutrition Table', views.nutrit,name='nutrit'),
    path('Yoga', views.yoga,name='yoga'),
    path('Cardio', views.cardio,name='cardio'),
    path('HIIT', views.hiit,name='hiit'),
    path('Heavy Weight Training', views.heavyw,name='heavyw'),
    path('Aerobics', views.aero,name='aero'),
    path('Register', views.register,name='register'),
    path('Login', views.loginu,name='login'),
    path('Logout', views.logout,name='logout'),
    path('Calo', views.calo,name='calo'),
    path('BMI', views.bmi1,name='bmi'),
    path('Bodyfat', views.bodyf1,name='bodyf'),
    path('profile', views.profile,name='profile'),
    path('Add', views.addexer,name='addexer'), 
    path('Article', views.article1,name='article1'), 
    path('Calo1', views.calo1,name='calo1'), 
    path('Calo2', views.calo2,name='calo2'),
    path('Recommendedmeals', views.reca,name='reca'),
    path('Baddmeal', views.baddmeal,name='baddmeal'),
    path('Laddmeal', views.laddmeal,name='laddmeal'),
    path('Eaddmeal', views.eaddmeal,name='eaddmeal'),
    path('Daddmeal', views.daddmeal,name='daddmeal'),
]