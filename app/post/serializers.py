from rest_framework import serializers
from core.models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'created', 'title', 'body']
