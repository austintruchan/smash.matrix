from django.contrib import admin
from smashtournamnet.models import Version
from smashtournamnet.models import Player
from smashtournamnet.models import Character
from smashtournamnet.models import Tournament

admin.site.register(Version)
admin.site.register(Character)
admin.site.register(Player)
admin.site.register(Tournament)
# Register your models here.
