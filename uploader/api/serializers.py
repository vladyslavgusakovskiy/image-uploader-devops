from rest_framework import serializers
from .models import ImageUpload


class ImageUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageUpload
        fields = '__all__'
        read_only_fields = ['original_filename', 'content_type', 'size']

    def create(self, validated_data):
        image = validated_data.get('image')
        instance = ImageUpload(
            image=image,
            original_filename=image.name,
            content_type=image.content_type,
            size=image.size,
        )
        instance.save()
        return instance
