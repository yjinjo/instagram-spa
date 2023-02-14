from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import permissions
from rest_framework.generics import CreateAPIView, ListAPIView
from .serializers import SignupSerializer, SuggestionUserSerializer


class SignUpView(CreateAPIView):
    # User 모델이 바뀔 수 있기 때문에 바로 User 모델을 쓰는 것보다 get_user_model을 호출합니다.
    model = get_user_model()
    serializer_class = SignupSerializer

    permission_classes = [
        permissions.AllowAny,  # 회원 가입시에는 누구나 접속할 수 있어야 합니다.
    ]


class SuggestionListAPIView(ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = SuggestionUserSerializer
