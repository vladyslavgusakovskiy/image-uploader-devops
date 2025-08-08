from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import ImageUpload
from PIL import Image
import tempfile

class ImageUploadAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.upload_url = reverse('image-upload')

    def generate_test_image(self):
        image = Image.new('RGB', (100, 100), color='red')
        tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
        image.save(tmp_file, format='JPEG')
        tmp_file.seek(0)
        return tmp_file

    def test_successful_image_upload(self):
        image_file = self.generate_test_image()

        response = self.client.post(
            self.upload_url,
            {'image': image_file},
            format='multipart'
        )

        print("STATUS:", response.status_code)
        print("DATA:", response.data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ImageUpload.objects.count(), 1)
