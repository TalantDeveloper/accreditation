from django.contrib import admin

from station.models import Title, Station


class TitleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_per_page = 20


class StationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_titles')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'id')
    list_per_page = 20


admin.site.register(Title, TitleAdmin)
admin.site.register(Station, StationAdmin)
