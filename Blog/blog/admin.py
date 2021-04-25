from django.contrib import admin
from .models import Post, UserProfileInfo, Comment
# Register your models here.

admin.site.register(Post)
admin.site.register(UserProfileInfo)
admin.site.register(Comment)
