from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from posts.models import Post, Comment, Group, Follow
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from .serializers import PostSerializer, CommentSerializer, GroupSerializer, FollowSerializer
from .permissions import OnlyAuthorPermission
from rest_framework import filters


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [IsAuthenticated, OnlyAuthorPermission]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = None
    permission_classes = [IsAuthenticated, OnlyAuthorPermission]

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        new_queryset = post.comments.all()
        return new_queryset

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        serializer.save(author=self.request.user, post=post)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)
    http_method_names = ['get', 'post']

    # def get_queryset(self):
    #     return self.request.user.follower.all()
    #
    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)
