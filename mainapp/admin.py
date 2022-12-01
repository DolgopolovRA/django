from django.contrib import admin

from mainapp.models import News, Course, CourseTeacher, Lesson


admin.site.register(Course)
admin.site.register(CourseTeacher)


@admin.register(News)
class adminNews(admin.ModelAdmin):
    search_fields = ["title", "preambule", "body"]


@admin.register(Lesson)
class AdminLesson(admin.ModelAdmin):
    list_display = ["id", "num", "title", "deleted"]

    def get_course_name(self, obj):
        return obj.name

    get_course_name.short_description = ("Курс")

    ordering = ["-course__name", "-num"]
    list_per_page = 2
    list_filter = ["course", "created_at", "deleted"]
    actions = ["mark_deleted"]

    def mark_deleted(self, request, queryset):
        queryset.update(deleted=True)
    mark_deleted.short_description = ("Пометить удаленным")
