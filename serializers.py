from rest_framework import serializers
from whitebox.models import Character, MeleeWeapon
from django.contrib.auth.models import User

class MeleeWeaponSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeleeWeapon
        fields = ['id', 'name', 'damage', 'weight', 'cost_gp']

class CharacterSerializer(serializers.ModelSerializer):
    character_role = serializers.CharField(source='get_role')
    username = serializers.CharField(source='get_username')
    melee_weapons = MeleeWeaponSerializer(many=True)

    class Meta:
        model = Character
        fields = ['id', 'name', 'strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma', 'gold', 'silver', 'copper', 'user', 'finalized', 'c_role', 'character_role', 'username', 'melee_weapons']


