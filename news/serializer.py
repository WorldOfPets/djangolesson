from rest_framework import serializers
from .models import News

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('title', 'content', 'slug', 'category')
    
    def validate(self, attrs):
        print(self.request.user)
        if len(attrs['title']) < 3:
            raise serializers.ValidationError("So short name for title")
        return attrs
