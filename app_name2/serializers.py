from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        # 모델 설정
        model = Movie
        # 필드 설정
        fields = ('id', 'title', 'genre', 'year')
