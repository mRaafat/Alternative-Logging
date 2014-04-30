from django.db.models import *
from django.forms import ModelForm, PasswordInput

# Create your models here.
class User(Model):
	email = CharField(max_length=100,primary_key=True)
	password = CharField(max_length=50)
	def categories(self):
		categoryPasswords = {}


	def __unicode__(self):
		return self.email

class UserForm(ModelForm):
	class Meta:
		model = User
		widgets = {
			'password' : PasswordInput(),
		}

	
class Category(Model):
	name = CharField(max_length = 40)
	user = ForeignKey('User')

	def allPath(self):
		picsURLs = {} #This dictionary will contain a key, representing number of pic and its URL

	def __unicode__(self):
		return self.name