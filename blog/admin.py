from django.contrib import admin


from models import Post

from django.contrib.auth.models import User
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
