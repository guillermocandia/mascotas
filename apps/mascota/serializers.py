from rest_framework import serializers

from .models import Mascota


class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = '__all__'


class MascotaVotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = ('pk',)
