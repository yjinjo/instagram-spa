from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, ListAPIView, get_object_or_404
from rest_framework.response import Response
from .serializers import SignupSerializer, SuggestionUserSerializer


class SignUpView(CreateAPIView):
    # User 모델이 바뀔 수 있기 때문에 바로  User 모델을 쓰는 것보다 get_user_model을 호출합니다.
    model = get_user_model()
    serializer_class = SignupSerializer

    permission_classes = [
        permissions.AllowAny,  # 회원 가입시에는 누구나 접속할 수 있어야 합니다.
    ]


class SuggestionListAPIView(ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = SuggestionUserSerializer

    def get_queryset(self):
        qs = (
            super()
            .get_queryset()
            .exclude(pk=self.request.user.pk)
            .exclude(pk__in=self.request.user.following_set.all())
        )
        return qs


@api_view(["POST"])
def user_follow(request):
    username = request.data["username"]
    follow_user = get_object_or_404(get_user_model(), username=username, is_active=True)
    request.user.following_set.add(follow_user)
    follow_user.follower_set.add(request.user)
    return Response(status.HTTP_204_NO_CONTENT)


@api_view(["POST"])
def user_unfollow(request):
    username = request.data["username"]
    follow_user = get_object_or_404(get_user_model(), username=username, is_active=True)
    request.user.following_set.remove(follow_user)
    follow_user.follower_set.remove(request.user)
    return Response(status.HTTP_204_NO_CONTENT)
