from rest_framework import serializers
from .models import Files

class FileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Files
        fields = ('file', 'selectedOption', 'target')