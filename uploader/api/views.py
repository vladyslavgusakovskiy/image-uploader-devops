from rest_framework.generics import CreateAPIView
from .models import ImageUpload
from .serializers import ImageUploadSerializer

class ImageUploadView(CreateAPIView):
    queryset = ImageUpload.objects.all()
    serializer_class = ImageUploadSerializer
