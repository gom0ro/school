from django.urls import path
from . import views
from django.shortcuts import render
urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact_view, name='contact'),
    path('success/', views.contact_success, name='success'),
    path('', views.index, name='index'),
    path('news/<int:pk>/', views.news_detail, name='news_detail'),   
    path('club/<int:pk>/', views.club_detail, name='club_detail'), # если хочешь отдельный html
]

def uyirmeler(request):
    return render(request, 'uyirmeler.html')
