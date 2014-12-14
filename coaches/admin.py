from django.contrib import admin
from coaches.models import Coach
from django.db import models
from django.forms.extras.widgets import SelectDateWidget


@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Basic', {
            'fields': (('name', 'surname'), 'user', 'birth_date')
        }),
        ('Contacts', {
            'fields': (('email', 'phone'),)
        }),
        ('Job information', {
            'fields': (('role', 'dossier'),)
        }),
    )
    list_display = ['user', 'name', 'surname', 'birth_date', 'email', 'phone',
                    'role', 'dossier']
    ordering = ['user', 'name', 'surname', 'birth_date', 'email', 'phone',
                'role', 'dossier']
    search_fields = ['user', 'name', 'surname', 'birth_date', 'email', 'phone',
                     'role', 'dossier']
    list_filter = ['birth_date', 'role']
    date_hierarchy = 'birth_date'
    formfield_overrides = {
        models.DateField: {'widget': SelectDateWidget}
    }
    save_as = True
    save_on_top = True