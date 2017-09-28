from django.contrib import admin

from df_goods.models import *
# Register your models here.
class GoodsInfoInline(admin.TabularInline):
    model = GoodsInfo
    extra = 4
class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['id','ttitle','isDelete']
    list_filter = ['ttitle']
    search_fields = ['ttitle']
    list_per_page = 10

    inlines = [GoodsInfoInline]

class GoodsInfoAdmin(admin.ModelAdmin):
	list_display = ['id','gtitle','gpic','gprice','isDelete', 'gunit', 'gclick', 'gjianjie', 'gkucun', 'gcontent', 'gtype']


admin.site.register(TypeInfo,TypeInfoAdmin)
admin.site.register(GoodsInfo,GoodsInfoAdmin)
