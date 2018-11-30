from django.contrib import admin
#导入需要管理的数据库表
from .models import Banner,Category,Tag,Tui,Article,Link
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    #文章列表中显示想要显示的字段
    list_display=('id','category','title','tui','user','views','created_time')
    #满5条数据自动分页
    list_per_page=5
    #后台数据列表排序方式
    ordering=('-created_time',)
    #设置哪些字段可以点击进入编辑界面
    list_display_links=('id','title')

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display=('id','text_info','img','link_url','is_active')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('id','name','index')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id','name')

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display=('id','name','linkurl')
