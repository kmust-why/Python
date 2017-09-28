# Register your models here.
from django.contrib import admin
from novel.models import *
# Register your models here.

class ChapterInfoAdmin(admin.ModelAdmin):
    list_display = ['chapterid','novelid','title','content']
    list_filter = ['title']
    search_fields = ['title']
    list_per_page = 10




class NovelInfoAdmin(admin.ModelAdmin):
	list_display = ['novelid','type','novelname']


admin.site.register(Novel,NovelInfoAdmin)
admin.site.register(Chapter,ChapterInfoAdmin)

