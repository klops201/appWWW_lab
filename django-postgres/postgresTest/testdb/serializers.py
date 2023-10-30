from rest_framework import serializers
from .models import Osoba, Stanowisko

class OsobaSerializer(serializers.Serializer):

   # id = serializers.IntegerField(read_only=True)

    imie = serializers.CharField(required=True)

    nazwisko = serializers.CharField(required=True)

    plec = serializers.ChoiceField(choices=Osoba.PLEC.choices, default=Osoba.PLEC.choices[0][0])

    data_dodania = serializers.DateField(read_only=True)

    stanowisko = serializers.PrimaryKeyRelatedField(queryset=Stanowisko.objects.all())

    def create(self, validated_data):
        return Osoba.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.imie = validated_data.get('imie', instance.imie)
        instance.nazwisko = validated_data.get('nazwisko', instance.nazwisko)
        instance.plec = validated_data.get('plec', instance.plec)
        instance.data_dodania = validated_data.get('data_dodania', instance.data_dodania)
        instance.stanowisko = validated_data.get('stanowisko', instance.stanowisko)
        instance.save()
        return instance






class StanowiskoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stanowisko
        fields = ['nazwa', 'opis']
        #read_only_fields = ['id']
