from django.shortcuts import render
from rest_framework import viewsets

from myapp.models import Post
from myapp.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
