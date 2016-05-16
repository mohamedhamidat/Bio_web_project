from __future__ import unicode_literals

from django.db import models

# Create your models here.

class ContactUs(models.Model):
	"""docstring for ContactUs"""
	message= models.TextField(blank=False, null=True)
	email = models.EmailField()
	full_name = models.CharField(max_length=120, blank=False, null=True) #blank required or no
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __unicode__(self):
		return self.email 
		# instance retured in admin 
		# return the email (__str__ for python3)


