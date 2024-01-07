"""
URL configuration for book_ticket project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Empty URL for the home view
    path('movies/', views.movie_list, name='movie_list'),
    path('theaters/', views.theater_list, name='theater_list'),
    path('screenings/', views.screening_list, name='screening_list'),
    path('book-tickets/', views.book_tickets, name='book_tickets'),
    path('confirm-booking/', views.confirm_booking, name='confirm_booking'),
    path('all-tickets/', views.all_tickets, name='all_tickets'),
    path('accounts/', include('django.contrib.auth.urls')),
]


