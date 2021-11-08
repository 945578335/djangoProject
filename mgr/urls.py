from django.urls import path
from mgr import views
urlpatterns = [
    path('',views.login),
    path('login/', views.uselogin),
    path('useregister/', views.useregister),
    path('register/', views.register),
]