from django import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('arabic_words.urls')),
    path('', include('pwa.urls')),
]
