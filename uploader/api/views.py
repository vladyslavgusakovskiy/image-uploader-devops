from rest_framework.generics import CreateAPIView
from django.http import HttpResponse
from .models import ImageUpload
from .serializers import ImageUploadSerializer
from django.utils import timezone

startup_time = timezone.now()

class ImageUploadView(CreateAPIView):
    queryset = ImageUpload.objects.all()
    serializer_class = ImageUploadSerializer

# Health Check View
def health(request):
    return HttpResponse("Health OK", content_type="text/plain")

# Readiness Check View
def ready(request):
    # Calculate elapsed time since startup
    elapsed_time = timezone.now() - startup_time
    if elapsed_time.total_seconds() < 30:
        # Return HTTP 500 for the first 30 seconds after startup
        return HttpResponse("Service not ready", status=500, content_type="text/plain")
    else:
        # After 30 seconds, return HTTP 200
        return HttpResponse("Readiness OK", content_type="text/plain")
