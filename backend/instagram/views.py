from datetime import timedelta
from time import timezone

from django.db.models import Q
from django.shortcuts import render
from rest_framework.permissions import AllowAny
from .models import Post
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer


# ViewSet은 CRUD가 다 들어간 API를 만들어줍니다.
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()  # DB의 전체에 대해서 쿼리를 날립니다.
    serializer_class = PostSerializer
    # permission_classes = [AllowAny]  # FIXME: 인증 적용

    def get_queryset(self):
        timesince = timezone.now() - timedelta(days=3)
        qs = super().get_queryset()
        qs = qs.filter(
            Q(author=self.request.user)
            | Q(author__in=self.request.user.following_set.all())
        )
        qs = qs.filter(created_at__gte=timesince)

        return qs
