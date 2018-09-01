from django.shortcuts import HttpResponse
from stark.service import stark
from .models import *
from django.forms import ModelForm

class AuthorConfig(stark.ModelStark):
    list_display = ['nid','name', 'age']
    list_display_links = ['name']

class BookModelForm(ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

        labels = {
            "authors":"作者",
            "publishDate":"出版日期",
        }

class BookConfig(stark.ModelStark):
    list_display = ['__str__',]
    list_display_links = ['title']
    modelform_class = BookModelForm
    search_fields = ['title','price']
    list_filter = ['title','publish','authors']  # 一对多，多对多字段

    # 批量修改数据
    def patch_init(self,request,queryset):
        queryset.update(price=111)

    patch_init.short_description = "批量初始化"

    actions = [patch_init]


stark.site.register(Book,BookConfig)
stark.site.register(Publish)
stark.site.register(Author,AuthorConfig)
stark.site.register(AuthorDetail)