from rest_framework.viewsets import ModelViewSet

from blog.models import Post
from blog.serializers.post_serializer import PostSerializer

class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer

    queryset = Post.objects.all().order_by('id')