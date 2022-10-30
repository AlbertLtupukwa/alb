from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
urlpatterns = [
   path('', views.home, name='home'),
   path('about/', views.about, name='about'),
   path('services/', views.services, name='services'),
   path('gallery/', views.gallery, name='gallery'),
   # path('http:/www.facebook.com/alberto.velez.1656854'),
]

urlpatterns += staticfiles_urlpatterns()