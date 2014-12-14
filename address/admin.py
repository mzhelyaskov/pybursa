from django.contrib import admin
from address.models import Address


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['index', 'country', 'district', 'region', 'street',
                    'house']
    ordering = ['index', 'country', 'district', 'region', 'street',
                'house']
    search_fields = ['index', 'country', 'district', 'region', 'street',
                     'house']
    list_filter = ['index', 'district', 'region']
    save_as = True
    save_on_top = True