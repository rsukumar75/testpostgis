from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import User
from .forms import Signup_form
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance
from django.contrib.gis.db.models import GeometryField
from django.forms.models import model_to_dict
import json

def signup(request):
	if request.method == 'POST':
		form = Signup_form(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.save()
			return HttpResponse("Thanks for signing up!")
	else:
		form = Signup_form()
	return render(request, 'lex/signup.html', {'form':form})

def recommendations(request,n):
	radius = 5
	current_user = User.objects.get(name=n)
	recommendations_list = User.objects.filter(location__dwithin=(current_user.location, Distance(km=radius)))
	latitude = []
	longitude = []
	names = []
	for u in recommendations_list:
		if(u.name!=n):
			latitude.append(u.location.y)
			longitude.append(u.location.x)
			names.append(u.name)
	context = {'latitude':latitude, 'longitude':longitude, 'names':names}
	return render(request, 'lex/recommendations.html', {"recommendations":json.dumps(context)})
# Create your views here.