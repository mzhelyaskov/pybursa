from django.contrib import admin
from students.models import Student
from django.db import models
from django.forms.extras.widgets import SelectDateWidget


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': (('name', 'surname'), 'birth_date')
        }),
        ('Contacts', {
            'fields': (('email', 'phone'),)
        }),
        ('Other information', {
            'fields': ('package', 'course', 'dossier')
        }),
    )
    list_display = ['name', 'surname', 'birth_date', 'email', 'phone',
                    'package']
    ordering = ['name', 'surname', 'birth_date', 'email', 'phone',
                'package']
    search_fields = ['name', 'surname', 'birth_date', 'email', 'phone',
                     'package']
    list_filter = ['birth_date', 'package']
    date_hierarchy = 'birth_date'
    filter_horizontal = ['course']
    if len(Student.PACKAGE_VIEW) < 5:
        radio_fields = {"package": admin.HORIZONTAL}
    formfield_overrides = {
        models.DateField: {'widget': SelectDateWidget}
    }
    list_max_show_all = 100
    list_per_page = 3