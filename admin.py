from django.contrib import admin

from .models import Character, MeleeWeapon, RangedWeapon

admin.site.register(Character)
admin.site.register(MeleeWeapon)
admin.site.register(RangedWeapon)
