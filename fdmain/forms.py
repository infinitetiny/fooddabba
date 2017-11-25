from django import forms
from django.db.models import Model
from fdmain.models import fd_cususer
from django.forms import ModelForm

class NameForm(ModelForm):
	class Meta:
		model = fd_cususer
		fields = ['id', 'contactnumber', 'cusname', 'mealtype', 'tiffintype', 'cuslocation', 'tiffincount', 'addressdetails']