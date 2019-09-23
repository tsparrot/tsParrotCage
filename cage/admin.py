from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')  # 要展示的字段
    list_filter = ('status', 'created', 'publish', 'author',)  # 过滤标签
    search_fields = ('title', 'body')  # 搜索组件
    # raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish',)
