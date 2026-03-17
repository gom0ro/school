from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'app'

urlpatterns = [
    # Басты бет
    path('', views.index, name='index'),

    # Мектеп туралы
    path('about/', views.about, name='about'),

    # Жаңалықтар
    path('news/', views.news_list, name='news_list'),
    path('news/<slug:slug>/', views.news_detail, name='news_detail'),

    # Мұғалімдер
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('teachers/<slug:slug>/', views.teacher_detail, name='teacher_detail'),

    # Галерея
    path('gallery/', views.gallery, name='gallery'),
    path('gallery/<slug:slug>/', views.gallery_album, name='gallery_album'),

    # Құжаттар
    path('documents/', views.documents, name='documents'),

    # Байланыс
    path('contact/', views.contact, name='contact'),
    
    # Тәрбие жұмыстары (отдельные HTML страницы)
    path('tarbie/birtutas/', TemplateView.as_view(template_name='tarbie/birtutas.html'), name='tarbie_birtutas'),
    path('tarbie/zhospary/', TemplateView.as_view(template_name='tarbie/zhospary.html'), name='tarbie_zhospary'),
    path('tarbie/sharalar/', TemplateView.as_view(template_name='tarbie/sharalar.html'), name='tarbie_sharalar'),
    path('tarbie/ata-analar/', TemplateView.as_view(template_name='tarbie/ata_analar.html'), name='ata_analar'),
    path('tarbie/quqyq/', TemplateView.as_view(template_name='tarbie/quqyq.html'), name='quqyq'),
    path('tarbie/profilaktika/', TemplateView.as_view(template_name='tarbie/profilaktika.html'), name='profilaktika'),
    path('tarbie/synyp/', TemplateView.as_view(template_name='tarbie/synyp.html'), name='synyp'),
    path('tarbie/parlament/', TemplateView.as_view(template_name='tarbie/parlament.html'), name='parlament'),
    path('tarbie/adal-urpaq/', TemplateView.as_view(template_name='tarbie/adal_urpaq.html'), name='adal_urpaq'),
    path('tarbie/zhas-ulan/', TemplateView.as_view(template_name='tarbie/zhas_ulan.html'), name='zhas_ulan'),

    # Статикалық беттер
    path('page/<slug:slug>/', views.static_page, name='static_page'),

    # Үйірмелер
    path('club/<slug:slug>/', views.club_detail, name='club_detail'),
]
