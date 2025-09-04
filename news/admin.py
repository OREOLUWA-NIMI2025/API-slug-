from django.contrib import admin
from .models import News
class NewsAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "published_date", "content"]
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ["title", "content"]


admin.site.register(News, NewsAdmin)


#what is doing here is that, i want you to automatically generate slug
#so where am i getting what i want use in generating it?
#("title",) generate it from the title. as i am passing these the title, the slug is been generate.



