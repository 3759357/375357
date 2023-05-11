from rest_framework import serializers
from .models import food

class foodSerializer(serializers.ModelSerializer):
    class Meta:
        model = food
        fields = ('title', 'text')