import datetime
from django.shortcuts import render, redirect

# Create your views here.
# from django.http import HttpResponse, HttpResponseNotFound
# from django.views.decorators.http import require_http_methods
from .forms import *
from .models import *

# def home(request):
# 	return render(request, 'index.html')
# @require_http_methods(["GET"])
def home(request):
	date = datetime.datetime.now()
	return render(request, 'index.html',{'date': date})
	# return HttpResponse("<h2>Hi, this is django App %s</h2>"%now)

def registration(request):
	if request == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			stu = Registration.objects.all()
			return render(request, 'index.html', {'form':stu})
		else:
			print("something wrong!")
			form = RegistrationForm()
			return render(request, 'index.html', {'form':form})
	else:
		print("working fine")
		return render(request, 'index.html')


####### DASHBOARD #########
def dashboard(request):
	return render(request, 'dashboard/dashboard.html')



def websitehome(request):
	return render(request, 'website/websitehome.html')

# def registration(request):
# 	if request == 'POST':
# 		form = RegistrationForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			userdetail = Registration.objects.all()
# 			return render(request, 'index.html', {'userdetail':userdetail})
# 		else:
# 			form = RegistrationForm()
# 			return render(request, "registration.html", {'form':form})