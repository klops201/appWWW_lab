from django.contrib import admin

from .models import Osoba, Stanowisko
admin.site.register(Stanowisko)

class OsobaAdmin(admin.ModelAdmin):
    readonly_fields = ['data_dodania',]

admin.site.register(Osoba, OsobaAdmin)


