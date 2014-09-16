from django.test import TestCase
from smashtournamnet.models import Version, Player, Character, Tournament

class VersionTestCase(TestCase):
	def setUp(self):
		Version.objects.create(name = "Melee")
		Version.objects.create(name = "Brawl")
	
	def test_version_name(self):
		melee = Version.objects.get(name = "Melee")
		brawl = Version.objects.get(name = "Brawl")
		self.assertEqual(melee.name, "Melee")
		self.assertEqual(brawl.name, "Brawl")

class PlayerTestCase(TestCase):
	def setUp(self):
		Player.objects.create(name="Austin")

	def test_player_name(self):
		austin = Player.objects.get(name = "Austin")
		self.assertEquals(austin.name, "Austin")

class CharacterTestCase(TestCase):
	def setUp(self):
		melee = Version.objects.create(name = "Melee")
		Character.objects.create(
			name = "Link",
			version = melee,
		)

	def test_version_foreign_key(self):
		link = Character.objects.get(name = "Link")
		melee = Version.objects.get(name = "Melee")
		self.assertEqual(melee, link.version)	

		
