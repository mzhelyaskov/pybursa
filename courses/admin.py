from django.contrib import admin
from courses.models import Course
from django.db import models
from django.forms.extras.widgets import SelectDateWidget


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Basic', {
            'classes': ('wide',),
            'fields': ('course_name', 'programming_len', 'description')
        }),
        ('Coaches', {
            'classes': ('wide',),
            'fields': ('teacher', 'assistant')
        }),
        ('Period', {
            'fields': (('start_date', 'end_date'),)
        }),
        ('Advanced options', {
            'fields': ('slug',)
        }),
    )
    list_display = ['course_name', 'slug', 'programming_len', 'description',
                    'start_date', 'end_date']
    ordering = ['course_name', 'slug', 'programming_len', 'description',
                'start_date', 'end_date']
    search_fields = ['course_name', 'slug', 'programming_len', 'description',
                     'start_date', 'end_date']
    list_filter = ['programming_len', 'start_date', 'end_date']
    date_hierarchy = 'start_date'

    prepopulated_fields = {"slug": ("course_name",), }
    formfield_overrides = {
        models.DateField: {'widget': SelectDateWidget}
    }
    save_as = True
    save_on_top = True