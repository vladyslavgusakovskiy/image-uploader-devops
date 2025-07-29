from django.urls import path
from .views import ImageUploadView, health, ready

urlpatterns = [
    path('upload/', ImageUploadView.as_view(), name='image-upload'),
    path('health', health, name="health"),
    path('ready', ready, name="ready"),
]
