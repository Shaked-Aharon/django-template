# main/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
]
