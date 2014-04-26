from django.db.models import *

# Create your models here.
class User(Model):
	email = CharField(max_length=100,primary_key=True)
	password = CharField(max_length=50)
	def categories(self):
		categoryPasswords = {}


	def __unicode__(self):
		return self.email

	
class Category(Model):
	name = CharField(max_length = 40)
	user = ForeignKey('User')

	def allPath(self):
		picsURLs = {} #This dictionary will contain a key, representing number of pic and its URL

	def __unicode__(self):
		return self.name