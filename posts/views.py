from posts.models import Post
from posts.serializers.posts_serializers import Post_Serializer
from rest_framework import viewsets, permissions

# Create your views here.
class Post(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = Post_Serializer

