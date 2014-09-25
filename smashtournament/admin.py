from django.contrib import admin
from smashtournament.models import Version
from smashtournament.models import Player
from smashtournament.models import Character
from smashtournament.models import Tournament

admin.site.register(Version)
admin.site.register(Character)
admin.site.register(Player)
admin.site.register(Tournament)
# Register your models here.
