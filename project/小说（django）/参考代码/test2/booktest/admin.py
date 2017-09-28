from django.contrib import admin
from booktest.models import *
# Register your models here.
class HeroInfoInline(admin.TabularInline):
    model = HeroInfo
    extra = 3
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id','btitle','bpub_date','bread','bcommet','isDelete']
    list_filter = ['btitle']
    search_fields = ['btitle']
    list_per_page = 10

    inlines = [HeroInfoInline]



class HeroInfoAdmin(admin.ModelAdmin):
	list_display = ['id','hname','hgender','hcontent','hbook']


admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)
