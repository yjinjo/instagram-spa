from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Post, Comment, Tag


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["photo_tag", "caption"]
    list_display_links = ["caption"]

    # list_display의 "photo_tag"에 대한 부분이고, post는 각각의 인스턴스입니다.
    def photo_tag(self, post):
        # mark_safe는 제한적으로 써야합니다. (임의로 안전하다고 개발자가 정한 것입니다.)
        return mark_safe(
            f"<img src={post.photo.url} style='width: 100px; height: 100px;' />"
        )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
