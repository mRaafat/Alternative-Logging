from django.contrib import admin
from AlternateLogging.models import*


# Register your models here.
class UserAdmin(admin.ModelAdmin):
	form = UserForm


admin.site.register(User,UserAdmin)



