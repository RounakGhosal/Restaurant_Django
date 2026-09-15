from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_header = "Restaurant Admin"
admin.site.site_title = "Restaurant Admin Portal"
admin.site.index_title = "Welcome to Restaurant Admin Portal"

urlpatterns = [

    path('', views.home, name='home'),

    path('about/', views.about, name='about'),

    path('services/', views.services, name='services'),

    path('dine-in/', views.dine_in, name='dine_in'),

    path('delivery/', views.delivery, name='delivery'),

    path('contact/', views.contact, name='contact'),

    path('search/', views.search, name='search'),
]