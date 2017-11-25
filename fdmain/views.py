from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import TemplateView
from fdmain.forms import NameForm
from .models import fd_cususer
from django.contrib import messages
from datetime import datetime

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'fdmain/index.html', context=None)

def createord(request):
	model = fd_cususer
	
	if request.method == 'POST':
        # create a form instance and populate it with data from the request:
		form = NameForm(request.POST)
		print('anil')
        # check whether it's valid:
		if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
			#pid = fd_cususer.id
			#pname = fd_cususer.name
			print('anil123')
			pid = fd_cususer.id
			pcontactnumber = fd_cususer.contactnumber
			pcusname = fd_cususer.cusname
			pmealtype = fd_cususer.mealtype
			ptiffintype = fd_cususer.tiffintype
			pcuslocation = fd_cususer.cuslocation
			ptiffincount = fd_cususer.tiffincount
			paddressdetails = fd_cususer.addressdetails
			form.save()
			messages.success(request, 'Order Placed Successfully')
			return render(request, 'fdmain/index.html', {'form': form})
			#return redirect(self.get_success_url())
    # if a GET (or any other method) we'll create a blank form
	else:
		form = NameForm()
		#return redirect(self.get_success_url())
		return render(request, 'fdmain/index.html', {'form': form})