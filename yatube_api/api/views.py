from rest_framework import viewsets

from api.serializers import PostSerializer
from posts.models import Comment, Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class GroupViewSet(viewsets.ModelViewSet):
    pass


class CommentViewSet(viewsets.ModelViewSet):
    pass


class FollowViewSet(viewsets.ModelViewSet):
    pass