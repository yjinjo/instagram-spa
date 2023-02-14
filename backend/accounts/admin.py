from django.contrib import admin
from .models import User


# User에 대한 admin을 추가
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
