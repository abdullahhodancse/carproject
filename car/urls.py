from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
   
   path('add/',views. AddPostCar.as_view(),name='addcars'),
   path('details/<int:id>',views. DetailsCarView.as_view(),name='details_car'),
   #path('buy/<int:id>/', views.buy_car, name='buy_car')
  
]
