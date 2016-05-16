from django.contrib import admin

# Register your models here.

from .models import ContactUs 
from .forms import ContactUsform

#class to customize 

class ContactUsadmin(admin.ModelAdmin):
	#what display in admin 
	list_display = ["__unicode__", "full_name", "email", "message", "timestamp"] 
	#how display the form in admin 
	form = ContactUsform

admin.site.register(ContactUs, ContactUsadmin)