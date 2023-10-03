from django.urls import path
from youtubelists.views import index,compress_images

urlpatterns = [
    path('', index, name='index'),
    path('compress/', compress_images, name='compress_images'),
    # Add other URL patterns if needed
]
