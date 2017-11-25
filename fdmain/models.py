from django.db import models
from django.utils import timezone
from datetime import date

class fd_cususer(models.Model):
	contactnumber = models.CharField(max_length=70, null=True)
	cusname = models.CharField(max_length=100, null=True)
	mealtype = models.CharField(max_length=60, null=True)
	tiffintype = models.CharField(max_length=60, null=True)
	cuslocation = models.CharField(max_length=160, null=True)
	tiffincount = models.CharField(max_length=40, null=True)
	addressdetails = models.CharField(max_length=600, null=True)
	orderdate = models.DateTimeField(default=timezone.now, null=True)
	
	def __str__(self):
		return self.id
	def __str__(self):
		return self.contactnumber
	def __str__(self):
		return self.cusname
	def __str__(self):
		return self.mealtype
	def __str__(self):
		return self.ordertype
	def __str__(self):
		return self.tiffintype
	def __str__(self):
		return self.cuslocation
	def __str__(self):
		return self.tiffincount
	def __str__(self):
		return self.addressdetails
	"""def __str__(self):
		return self.orderdate"""