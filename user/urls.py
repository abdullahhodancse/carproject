from django.contrib import admin
from django.urls import path
from . import views
from .views import ProfileView,buy_car
#from car.views import buy_car

urlpatterns = [
   
    path('reg/',views.singup ,name='singup'),
   
    path('login/',views.UserLogInView.as_view(),name='user_login'),
   # path('profile/',views.profile,name='profile'),
    path('password/',views.password,name='password'),
    path('logout/',views.logout,name='logout'),
    path('update/',views.edit_profile,name='update'),
    path('profile/', ProfileView.as_view(), name='profile'),  
    # path('buy/<int:id>/', buy_car, name='buy_car'),
    path('user/buy/<int:car_id>/', views.buy_car, name='buy_car'),
    

    
    
  
   
]
