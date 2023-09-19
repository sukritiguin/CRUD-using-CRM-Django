from django.urls import path

from . import views


urlpatterns = [
    path('', views.HomePage, name='home'),
    path('register/', views.RegisterPage, name='register'),
    path('login/', views.LoginPage, name='login'),
    path('logout/', views.LogoutPage, name='logout'),
    path('dashboard/', views.DashboardPage, name='dashboard'),
    path('create-record/', views.CreateRecordPage, name='create-record'),
    path('update-record/<int:pk>/', views.UpdateRecordPage, name='update-record'),
]
