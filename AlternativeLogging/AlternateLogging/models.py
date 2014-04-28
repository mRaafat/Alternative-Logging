from django.db.models import *
 
# Create your models here.
 
class User(Model): 
    email = CharField(max_length=128,primary_key=True)
    password = CharField(max_length=64)
 
 #Function that return a category of password that corresponds to the user password
    def categories(self):
        return [cat for cat in [Category.objects.get(id=cid) for cid in self.password.split()]]
    
    def __unicode__(self):
        return self.email
 
 
class Category(Model):
    name = CharField(max_length = 64)
 
    def __unicode__(self):
        return self.name
        #Function to return a specific picture
    def get_pictures(self):
        return [pic for pic in Picture.objects.filter(category=self)]
        
 
class Picture(Model):
    category = ForeignKey('Category')
    url = CharField(max_length = 265)
    
    def __unicode__(self):
        return self.url
