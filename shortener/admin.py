from django.contrib import admin
from shortener.models import URL
# Register your models here.


class URLAdmin(admin.ModelAdmin):
    exclude = ['short_url', ]
    list_display = ('url', 'short_url')


admin.site.register(URL, URLAdmin)
