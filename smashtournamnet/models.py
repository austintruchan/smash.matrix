from django.db import models

class Version(models.Model):
	name = models.CharField(max_length=200)
	
	def __str__(self):
		return self.name

class Player(models.Model):
	name = models.CharField(max_length=200)
	date_created = models.DateTimeField()

	def __str__(self):
		return self.name

class Character(models.Model):
	name = models.CharField(max_length=200)
	version = models.ForeignKey(Version) 

	def __str__(self):
		return self.name

class Tournament(models.Model):
	players = models.ManyToManyField(Player)
		
