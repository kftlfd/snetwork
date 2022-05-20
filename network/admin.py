from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username")

class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "time")

class ReactionAdmin(admin.ModelAdmin):
    list_display = ("id", "post", "user", "type")

class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "post", "user", "time")

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Reaction, ReactionAdmin)
admin.site.register(Comment, CommentAdmin)
