from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import PostSerializer, CommentSerializer, RegisterSerializer
from blog.models import Post, Comment


class PostAPIViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class CommentAPIViewSet(ListModelMixin, CreateModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class RegisterAPIView(CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]