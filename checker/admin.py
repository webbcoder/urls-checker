from django.contrib import admin
from .models import UrlsChecker, Link
# Register your models here.


class UrlsCheckerAdmin(admin.ModelAdmin):
    list_display = ('author', 'interval')
    fields = ('author', 'links')


class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')
    fields = ('title', 'url')


admin.site.register(UrlsChecker, UrlsCheckerAdmin)
admin.site.register(Link, LinkAdmin)

