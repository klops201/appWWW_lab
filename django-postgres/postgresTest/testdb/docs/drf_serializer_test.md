>>> from rest_framework.renderers import JSONRenderer
>>> from rest_framework.parsers import JSONParser
>>> from testdb.models import Osoba, Stanowisko
>>> from testdb.serializers import OsobaSerializer
>>> osoba = Osoba(imie='Adam', nazwisko='Kowalski', plec=Osoba.PLEC.Mężczyzna, stanowisk
o=kierowca)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'kierowca' is not defined
>>> stanowisko_kierowcy = Stanowisko.objects.get(nazwa='kierowca')
>>> osoba = Osoba(imie='Adam', nazwisko='Kowalski', plec=Osoba.PLEC.Mężczyzna, stanowisk
o=stanowisko_kierowcy)
>>> serializer = OsobaSerializer(osoba)
>>> serializer.data
{'imie': 'Adam', 'nazwisko': 'Kowalski', 'plec': 1, 'data_dodania': None, 'stanowisko': 
1}
>>> content = JSONRenderer().render(serializer.data)
>>> content
b'{"imie":"Adam","nazwisko":"Kowalski","plec":1,"data_dodania":null,"stanowisko":1}'
>>> import io
>>> stream = io.BytesIO(content)
>>> data = JSONParser().parse(stream)
>>> deserializer = OsobaSerializer(data=data)
>>> deserializer.is_valid()
True
>>> deserializer.errors
{}  
>>> deserializer.fields
{'imie': CharField(required=True), 'nazwisko': CharField(required=True), 'plec': ChoiceField(choic
es=[(1, 'Mężczyzna'), (2, 'Kobieta'), (3, 'Inne')], default=1), 'data_dodania': DateField(read_onl
y=True), 'stanowisko': PrimaryKeyRelatedField(queryset=<QuerySet [<Stanowisko: kierowca>, <Stanowi
sko: lekarz>, <Stanowisko: Programista>]>)}
>>> deserializer.validated_data
OrderedDict([('imie', 'Adam'), ('nazwisko', 'Kowalski'), ('plec', 1), ('stanowisko', <Stanowisko: 
kierowca>)])
>>> deserializer.save()
>>> deserializer.data
{'imie': 'Adam', 'nazwisko': 'Kowalski', 'plec': 1, 'data_dodania': '2023-10-30', 'stanowisko': 1}

----------------------------------------------------------------------------------------


>>> stanowisko1 = Stanowisko(nazwa='kucharz', opis='gotuje')              
>>> stanowisko1.save()
>>> serializer = StanowiskoModelSerializer(stanowisko1)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'StanowiskoModelSerializer' is not defined
>>> from testdb.serializers import StanowiskoModelSerializer             
>>> serializer = StanowiskoModelSerializer(stanowisko1)      
>>> serializer.data
{'nazwa': 'kucharz', 'opis': 'gotuje'}
>>> content = JSONRenderer().render(serializer.data)
>>> content
b'{"nazwa":"kucharz","opis":"gotuje"}'
>>> stream = io.BytesIO(content)
>>> data = JSONParser().parse(stream)
>>> deserializer = StanowiskoModelSerializer(data=data)
>>> deserializer.is_valid()
True
>>> deserializer.errors
{}
>>> deserializer.fields
{'nazwa': CharField(max_length=60), 'opis': CharField(allow_blank=True, allow_null=True, max_lengt
h=60, required=False)}
>>> deserializer.validated_data
OrderedDict([('nazwa', 'kucharz'), ('opis', 'gotuje')])
>>> deserializer.save()
<Stanowisko: kucharz>
>>> deserializer.data
{'nazwa': 'kucharz', 'opis': 'gotuje'}
