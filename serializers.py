from rest_framework import serializers
from whitebox.models import Character

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['id', 'strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma', 'gold', 'silver', 'copper', 'user', 'finalized', 'c_role']
