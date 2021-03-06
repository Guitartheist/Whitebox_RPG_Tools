from django.db import models
from django.contrib.auth.models import User
import random

def roll_attribute():
    a = 0
    for x in range(3):
        a += random.randrange(1,6)
    return a

def roll_starting_cash():
    a = 0
    for x in range(3):
        a += random.randrange(1, 6) * 10
    return a
        
class MeleeWeapon(models.Model):
    name = models.CharField(max_length=40)
    damage = models.CharField(max_length=40)
    weight = models.IntegerField()
    cost_gp = models.IntegerField()

    def __str__(self):
        r = self.name + " / " + self.damage + " / " + str(self.weight) + " / " + str(self.cost_gp) + " gp "
        return r

# USAGE: To add melee weapons to a character,
# MeleeWeaponQuantity.objects.create(character=character, melee_weapon=melee_weapon, quantity =quantity)
class MeleeWeaponQuantity(models.Model):
    character = models.ForeignKey('Character', related_name = 'melee_weapon_quantity', on_delete = models.SET_NULL, null = True)
    melee_weapon = models.ForeignKey('MeleeWeapon', related_name = 'melee_weapon_quantity', on_delete = models.SET_NULL, null = True, blank = True)
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return str(self.character.name) + " " + str(self.character.id) + " / " + str(self.melee_weapon.name)
        
class RangedWeapon(models.Model):
    name = models.CharField(max_length=40)
    damage = models.CharField(max_length=40)
    weight = models.IntegerField()
    rof = models.FloatField()
    w_range = models.IntegerField()
    cost_gp = models.IntegerField()

    def __str__(self):
        r = self.name + " / " + self.damage + " / " + str(self.rof) + " / " + str(self.w_range) + " / "  + str(self.weight) + " / " +  str(self.cost_gp) + " gp "
        return r

# USAGE: To add ranged weapons to a character,
# RangedWeaponQuantity.objects.create(character=character, melee_weapon=melee_weapon, quantity =quantity)        
class RangedWeaponQuantity(models.Model):
    character = models.ForeignKey('Character', related_name = 'raned_weapon_quantity', on_delete = models.SET_NULL, null = True)
    ranged_weapon = models.ForeignKey('RangedWeapon', related_name = 'ranged_weapon_quantity', on_delete = models.SET_NULL, null = True, blank = True)
    quantity = models.IntegerField(default=1)

class Character(models.Model):
    FIGHTER = 0
    MAGE = 1
    THIEF = 2
    CLERIC = 3
    name = models.CharField(max_length=40, default = "Scrub")
    strength = models.IntegerField(default=3)
    dexterity = models.IntegerField(default=3)
    constitution = models.IntegerField(default=3)
    intelligence = models.IntegerField(default=3)
    wisdom = models.IntegerField(default=3)
    charisma = models.IntegerField(default=3)
    gold = models.IntegerField(default=30)
    silver = models.IntegerField(default=0)
    copper = models.IntegerField(default=0)
    c_role = models.IntegerField(null=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    finalized = models.BooleanField(default=False)
    melee_weapons = models.ManyToManyField('MeleeWeapon', through='MeleeWeaponQuantity', related_name='melee_weapons')
    ranged_weapons = models.ManyToManyField('RangedWeapon', through='RangedWeaponQuantity', related_name='ranged_weapons')

    def get_username(self):
        if (self.user):
            return self.user.username
        return ''

    def get_role(self):
        if (self.c_role is not None):
            if (self.c_role == 0):
                return "Fighter"
            if (self.c_role == 1):
                return "Mage"
            if (self.c_role == 2):
                return "Thief"
            if (self.c_role == 3):
                return "Cleric"
            else:
                return "Person"
        else:
            return "Person"
    def roll(self, name):
        self.name = name
        self.strength = roll_attribute()
        self.dexterity = roll_attribute()
        self.constitution = roll_attribute()
        self.intelligence = roll_attribute()
        self.wisdom = roll_attribute()
        self.charisma = roll_attribute()
        self.gold = roll_starting_cash()
        self.silver = 0
        self.copper = 0
        return self
        
    def __str__(self):
        r = self.name + ": STR " + str(self.strength) + " / "
        r += "DEX " + str(self.dexterity) + " / "
        r += "CON " + str(self.constitution) + " / "
        r += "INT " + str(self.intelligence) + " / "
        r += "WIS " + str(self.wisdom) + " / "
        r += "CHA " + str(self.charisma) + " / "
        r += "GOLD " + str(self.gold) + " / "
        r += "SILVER " + str(self.silver) + " / "
        r += "COPPER " + str(self.copper) + " / "
        if (self.user == None):
            r += "Created by anonymous"
        else:
            r += "Created by " + self.user.username
        if self.finalized:
            r += " / Character has been finalized."
        else:
            r += " / Character not yet finalized."
        return r
        
    def purchase_melee_weapon(self, melee_weapon):
        if (self.gold >= melee_weapon.cost_gp):
            self.gold -= melee_weapon.cost_gp
            melee_weapon_quantity = MeleeWeaponQuantity.objects.create(character=self, melee_weapon=melee_weapon, quantity = 1)
            self.save()
            
    def purchase_ranged_weapon(self, ranged_weapon):
        if (self.gold >= ranged_weapon.cost_gp):
            self.gold -= ranged_weapon.cost_gp
            ranged_weapon_quantity = RangedWeaponQuantity.objects.create(character=self, ranged_weapon=ranged_weapon, quantity = 1)
            self.save()
        
    # used to see if dumping points into core role stat is legal
    # if dump is legal, performs dump. Character will still need to be saved.
    # s d c i w c = strength dexterity constitution intelligence wisdom charisma
    # return 0 or an error message detailing why the dump is not legal
    def finalize(self, c_role, s, d, co, i, w, ch):

        if self.finalized:
            return "Character has already been finalized."

        dump_from = "Cannot dump ? so that it is below 9. "
        dump_to = "Cannot dump ? so that it is above 18."
        total_dump = s + d + co + i + w + ch
        r = ""
        if (self.strength - s < 9 and s > 0):
            r += dump_from.replace("?","strength")
        if (self.dexterity - d < 9 and d > 0):
            r += dump_from.replace("?","dexterity")
        if (self.constitution - co < 9 and co > 0):
            r += dump_from.replace("?","constitution")
        if (self.intelligence - i < 9 and i > 0) :
            r += dump_from.replace("?","intelligence")
        if (self.wisdom - w < 9 and w > 0):
            r += dump_from.replace("?","wisdom")
        if (self.charisma - ch < 9 and ch > 0):
            r += dump_from.replace("?","charisma")

        if (int(c_role) == self.FIGHTER):
            if total_dump + self.strength - s > 18:
                r += dump_to.replace("?", "strength")
            else:
                self.strength += total_dump - s
        elif (int(c_role) == self.MAGE):
            if total_dump + self.intelligence - i > 18:
                r += dump_to.replace("?", "intelligence")
            else:
                self.intelligence += total_dump - i
        elif (int(c_role) == self.THIEF):
            if total_dump + self.dexterity + d > 18:
                r += dump_to.replace("?", "dexterity")
            else:
                self.dexterity += total_dump - d
        elif (int(c_role) == self.CLERIC):
            if total_dump + self.wisdom + w > 18:
                r += dump_to.replace("?", "wisdom")
            else:
                self.wisdom += total_dump - w
        else:
            r += "Invalid character role " + c_role + " selected."

        if (len(r) == 0):
            self.strength -= s
            self.dexterity -= d
            self.constitution -= co
            self.intelligence -= i
            self.wisdom -= w
            self.charisma -= ch
            self.c_role = c_role
            self.finalized = True
            return 0
        else:
            return r
