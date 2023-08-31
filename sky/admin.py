from django.contrib import admin
from . models import News, Subscribers, Category

# Register your models here.
admin.site.register(Category)
class NewsAdmin(admin.ModelAdmin):
    list_display = ["title", "reporter", "category",  "date_posted"]
    prepopulated_fields = {"slug": ("category", "title",)}
    list_editable = ["category"]
    list_filter = ["category", "reporter"]

admin.site.register(News, NewsAdmin)
admin.site.register(Subscribers)