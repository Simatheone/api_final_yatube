from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from api.serializers import (
    CommentSerializer, FollowSerializer,
    GroupSerializer, PostSerializer
)
from api.permissions import IsAuthorOrReadOnly
from posts.models import Comment, Group, Follow, Post


class PostViewSet(viewsets.ModelViewSet):
    """Вьюсет для обработки CRUD запросов эндпоинта posts/... ."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ModelViewSet):
    """Вьюсет для обработки CRUD запросов эндпоинта groups/... ."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def create(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class CommentViewSet(viewsets.ModelViewSet):
    """
    Вьюсет для обработки CRUD запросов.
    Эндпоинты: 
    posts/<post_id>/comments/ и posts/<post_id>/comments/<comment_id>/
    """
    serializer_class = CommentSerializer
    # permission_classes = 

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        queryset = Comment.objects.filter(post_id=post_id)
        return queryset


class FollowViewSet(viewsets.ModelViewSet):
    """Вьюсет для обработки CRUD запросов follow/... ."""
    serializer_class = FollowSerializer
    # permission_classes = 
    pass