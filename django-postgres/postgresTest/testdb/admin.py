from django.contrib import admin

from .models import Osoba, Stanowisko
class OsobaAdmin(admin.ModelAdmin):
    readonly_fields = ['data_dodania']
    list_display = ['imie','nazwisko', 'plec', 'stanowisko']
    list_filter = ['stanowisko', 'data_dodania']

admin.site.register(Osoba, OsobaAdmin)


class StanowiskoAdmin(admin.ModelAdmin):
    list_filter = ('nazwa',)
    list_display = ['nazwa']



admin.site.register(Stanowisko, StanowiskoAdmin)


