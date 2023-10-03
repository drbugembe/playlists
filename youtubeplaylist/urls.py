from django.contrib import admin
from django.urls import path
from youtubelists.views import index,compress_images

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('compress/', compress_images, name='compress_images'),
]
