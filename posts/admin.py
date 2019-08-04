from django.contrib import admin

# Register your models here.
from.models import Post

# アドミン管理サイトにPostの管理機能を追加
admin.site.register(Post)
