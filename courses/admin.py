from django.contrib import admin

from .models import Course, Lesson


class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 1


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "is_published")
    list_filter = ("is_published",)
    search_fields = ("title",)
    inlines = [LessonInline]


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("title", "course", "position")
    list_filter = ("course",)
    search_fields = ("title",)