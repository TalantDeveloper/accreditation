from django.contrib import admin

from student.models import Student, Group


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'title')
    list_display_links = ('id', 'full_name')
    search_fields = ('full_name', 'title')
    list_per_page = 20


class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_students')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'id')
    list_per_page = 20


admin.site.register(Student, StudentAdmin)
admin.site.register(Group, GroupAdmin)
