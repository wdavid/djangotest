from rest_framework import serializers
from .models import Persona

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        #fields = ['id', 'fullname', 'nickname', 'age', 'is_active']
        fields = '__all__'