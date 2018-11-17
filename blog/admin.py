from django.contrib import admin
# include/import model Post
from .models import Post

# register Post model with
admin.site.register(Post)
