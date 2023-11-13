from rest_framework import serializers
from .models import Osoba, Stanowisko
from datetime import date

class OsobaSerializer(serializers.Serializer):

   # id = serializers.IntegerField(read_only=True)

    imie = serializers.CharField(required=True)

    nazwisko = serializers.CharField(required=True)

    plec = serializers.ChoiceField(choices=Osoba.PLEC.choices, default=Osoba.PLEC.choices[0][0])

    data_dodania = serializers.DateField(read_only=True)

    stanowisko = serializers.PrimaryKeyRelatedField(queryset=Stanowisko.objects.all())

    def create(self, validated_data):
        return Osoba.objects.create(**validated_data)



    def validate_imie(self, value):

        if not value.isalpha():
            raise serializers.ValidationError(
                "Nazwa osoby powinna składać się tylko z liter!",
            )
        return value


    # def validate_data_dodania(self, value):
    #     # if not (value <= date.today()):
    #     if not (value == date.today()):
    #         raise serializers.ValidationError(
    #             "data jest z przyszłości!",
    #         )
    #     return value



    def update(self, instance, validated_data):
        instance.imie = validated_data.get('imie', instance.imie)
        instance.nazwisko = validated_data.get('nazwisko', instance.nazwisko)
        instance.plec = validated_data.get('plec', instance.plec)
        instance.data_dodania = validated_data.get('data_dodania', instance.data_dodania)
        instance.stanowisko = validated_data.get('stanowisko', instance.stanowisko)
        instance.save()
        return instance






class StanowiskoSerializer(serializers.Serializer):

    nazwa = serializers.CharField(required=True)

    opis = serializers.CharField(required=True)

    def update(self, instance, validated_data):
        instance.nazwa = validated_data.get('nazwa', instance.nazwa)
        instance.opis = validated_data.get('opis', instance.opis)
        instance.save()
        return instance
