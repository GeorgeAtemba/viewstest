from rest_framework import serializers
from .models import MixMod

class SerViewset(serializers.ModelSerializer):
    class Meta:
        model = MixMod()
        fields = '__all__'
