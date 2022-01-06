from rest_framework import serializers
from whitebox.models import Character, MeleeWeapon, RangedWeapon
from django.contrib.auth.models import User

class MeleeWeaponSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeleeWeapon
        fields = ['id', 'name', 'damage', 'weight', 'cost_gp']
        
class RangedWeaponSerializer(serializers.ModelSerializer):
    class Meta:
        model = RangedWeapon
        fields = ['id', 'name', 'damage', 'rof', 'w_range', 'weight', 'cost_gp']

class CharacterSerializer(serializers.ModelSerializer):
    character_role = serializers.CharField(source='get_role')
    username = serializers.CharField(source='get_username')
    melee_weapons = MeleeWeaponSerializer(many=True)
    ranged_weapons = RangedWeaponSerializer(many=True)

    class Meta:
        model = Character
        fields = ['id', 'name', 'strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma', 'gold', 'silver', 'copper', 'user', 'finalized', 'c_role', 'character_role', 'username', 'melee_weapons', 'ranged_weapons']


