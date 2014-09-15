from django.db import models

class Version(models.Model):
	name = models.CharField(max_length=200)
	characters = models.OneToManyField(Character, verbose_name="list of characters")

class Player(models.Model):
	name = models.CharField(max_length=200)
	date_created = models.DateTimeField('date joined')

class Character(models.Model):
	name = models.CharField(max_length=200)
	version = models.OneToManyField(Version, verbose_name="version of smash")

class Tournament(models.Model):
	players = models.OneToManyField(Player, verbose_name="participants")
		
