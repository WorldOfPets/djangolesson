from rest_framework import serializers

from .models import *

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['titel', 'content', 'date_joined', 'is_publised', 'category']
    
    def validate(self, attrs):
        if len(attrs['titel']) < 4:
            raise serializers.ValidationError("Слишко короткое название статьи!")

        return super().validate(attrs)


class NewsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsCategory
        fields = ['id', 'name']