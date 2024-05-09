from django.contrib import admin
from url_shortner import models
# Register your models here.

class UrlAdmin(admin.ModelAdmin):
    list_display = ["id","uuid","created_at"]
    list_display_links = ["uuid"]
    list_filter = ["id","url","uuid"]
    search_fields = ["url","uuid"]

admin.site.register(models.Urls,UrlAdmin)