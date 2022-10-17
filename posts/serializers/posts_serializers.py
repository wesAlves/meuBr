from dataclasses import field, fields
from rest_framework import serializers
from posts.models import Post

class Post_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'