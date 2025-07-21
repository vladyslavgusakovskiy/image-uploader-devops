from django.db import models

class ImageUpload(models.Model):
    image = models.ImageField(upload_to='uploads/')
    upload_time = models.DateTimeField(auto_now_add=True)
    original_filename = models.CharField(max_length=255, blank=True)
    content_type = models.CharField(max_length=100, blank=True)
    size = models.PositiveIntegerField(blank=True, null=True)
