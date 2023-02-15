import re

from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()


class SignupSerializer(serializers.ModelSerializer):
    # write_only 옵션으로 DB에서 절대 읽어오는 것이 아닌 쓰기 전용으로 적용합니다.
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        # User.objects.create 를 통해서 user를 하나 생성합니다.
        user = User.objects.create(username=validated_data["username"])

        # set_password를 통해서 password에 해당하는 부분을 암호화해서 setting 합니다.
        user.set_password(validated_data["password"])
        user.save()
        return user

    class Meta:
        model = User
        fields = ["pk", "username", "password"]


class SuggestionUserSerializer(serializers.ModelSerializer):
    avatar_url = serializers.SerializerMethodField("avatar_url_field")

    def avatar_url_field(self, author):
        if re.match(r"^https?://", author.avatar_url):
            return author.avatar_url

        if "request" in self.context:
            scheme = self.context["request"].scheme  # 'http' or 'https
            host = self.context["request"].get_host()
            return scheme + "://" + host + author.avatar_url

    class Meta:
        model = User
        fields = ["username", "name", "avatar_url"]
