from django.contrib import admin
from dossier.models import Dossier


@admin.register(Dossier)
class DossierAdmin(admin.ModelAdmin):
    filter_horizontal = ['unloved_courses']
    list_display = ['address', 'favorite_color']
    list_filter = ['favorite_color']
    search_fields = ['address', 'favorite_color']
    save_as = True
    save_on_top = True