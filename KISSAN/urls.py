from django.urls import path
from KISSAN import views

urlpatterns = [
    path('home1/', views.index, name='home1'),
    path('', views.home, name="index"),
    path('home/', views.analyse, name="home"),
    path('prediction/', views.Predict, name="prediction"),
]