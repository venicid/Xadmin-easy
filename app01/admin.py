from django.contrib import admin
from .models import *


class BookConfig(admin.ModelAdmin):
    list_display = ['title','price']
    search_fields = ['title', 'price']
    list_filter = ['title','publish','authors']

    # 批量修改数据
    def patch_init(self,request,queryset):
        print(queryset)
        queryset.update(price=100)

    patch_init.short_description = "批量初始化"

    actions = [patch_init]


admin.site.register(Book,BookConfig)
admin.site.register(Author)
admin.site.register(Publish)
admin.site.register(AuthorDetail)