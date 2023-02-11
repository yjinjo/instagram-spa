from django.shortcuts import render
from rest_framework.permissions import AllowAny

from .models import Post
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer


# ViewSet은 CRUD가 다 들어간 API를 만들어줍니다.
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()  # DB의 전체에 대해서 쿼리를 날립니다.
    serializer_class = PostSerializer
    permission_classes = [AllowAny]  # FIXME: 인증 적용
