from django.db import models
import datetime
from django.utils import timezone


class Stanowisko(models.Model):

    nazwa = models.CharField(max_length=60, null=False, blank=False)
    opis = models.CharField(max_length=60, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Stanowiska"

    def __str__(self):
        return self.nazwa




class Osoba(models.Model):


    PLEC = models.IntegerChoices('Płeć', 'Mężczyzna Kobieta Inne')
    imie = models.CharField(max_length=60, null=False, blank=False)
    nazwisko = models.CharField(max_length=60, null=False, blank=False)
    plec = models.IntegerField(choices = PLEC.choices)
    stanowisko = models.ForeignKey(Stanowisko, null=True, blank=True, on_delete=models.SET_NULL)
    data_dodania = models.DateField(default=datetime.date.today)
    wlasciciel = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    class Meta:
        ordering = ['nazwisko']
        verbose_name_plural = "Osoby"

    def __str__(self):
        return f"{self.imie +' '+ self.nazwisko}"


