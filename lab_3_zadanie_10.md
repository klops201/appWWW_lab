>>> from testdb.models import Osoba, Stanowisko
>>> osoby = Osoba.objects.all()
>>> print(osoby)
<QuerySet [<Osoba: kaśka akrobata>, <Osoba: marek chrust>, <Osoba: ewa kot>, <Osoba: jan
 kowalski>, <Osoba: jarek monitor>]>
>>> osoba3 = Osoba.objects.get(id=3)
>>> print(osoba3)
jarek monitor
>>> osoby_j = Osoba.objects.filter(imie__startswith = 'j')
>>> print(osoby_j)
<QuerySet [<Osoba: jan kowalski>, <Osoba: jarek monitor>]>
>>> nazwiska= Osoba.objects.values('stanowisko').distinct()
>>> print(nazwiska)
<QuerySet [{'stanowisko': 2}, {'stanowisko': 3}, {'stanowisko': 1}, {'stanowisko': 1}, {
'stanowisko': 1}]>
>>> stanowiskoSort = Stanowisko.objects.order_by('-nazwa')
>>> print(stanowiskoSort)
<QuerySet [<Stanowisko: Programista>, <Stanowisko: lekarz>, <Stanowisko: kierowca>]>

>>> osobaNew = Osoba(imie = 'andrzej', nazwisko = 'duda', plec = 1, stanowisko = 'kierowca')
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "C:\Users\bostr\PycharmProjects\laby_WWW\venv\lib\site-packages\django\db\models\base.py", line 543, in __init_
_
    _setattr(self, field.name, rel_obj)
  File "C:\Users\bostr\PycharmProjects\laby_WWW\venv\lib\site-packages\django\db\models\fields\related_descriptors.py"
, line 266, in __set__
    raise ValueError(
ValueError: Cannot assign "'kierowca'": "Osoba.stanowisko" must be a "Stanowisko" instance.
>>> stanowisko_kierowcy = Stanowisko.objects.get(nazwa='kierowca')
>>> osobaNew = Osoba(imie = 'andrzej', nazwisko = 'duda', plec = 1, stanowisko = stanowisko_kierowcy) 
>>> osobaNew.save()                                                                                  
>>> 
