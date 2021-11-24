from django.urls import path
from phc import views

urlpatterns = [
    path('phcindex/',views.indexshow),
    path('datashow_page/', views.datashow_page),
    path('inquiry_page/', views.inquiry_page),
    path('inquiry/', views.inquiry),
    path('message_trace/', views.message_trace),
    path('trace/', views.trace),

]