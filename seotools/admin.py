from django.contrib import admin

from seo.admin import ModelInstanceSeoInline


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ModelInstanceSeoInline]