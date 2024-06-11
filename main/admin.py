from django.contrib import admin

from main.models import Exam, ResultTest, General


class ExamAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'group', 'station', 'result')
    list_display_links = ('id', 'student', 'group', 'station', 'result')
    search_fields = ('student', 'group', 'station', 'result')
    list_per_page = 20


class ResultTestAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'group', 'result')
    list_display_links = ('id', 'student', 'group', 'result')
    search_fields = ('student', 'group', 'result')
    list_per_page = 20


class GeneralAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'group', 'result_test', 'exam', 'result_sum')
    list_display_links = ('id', 'student', 'group', 'result_test', 'exam', 'result_sum')
    search_fields = ('student', 'group', 'result_test', 'exam', 'result_sum')
    list_per_page = 20


admin.site.register(Exam, ExamAdmin)
admin.site.register(ResultTest, ResultTestAdmin)
admin.site.register(General, GeneralAdmin)
