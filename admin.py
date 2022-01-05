from django.contrib import admin

from .models import Character
from .models import MeleeWeapon

admin.site.register(Character)
admin.site.register(MeleeWeapon)
