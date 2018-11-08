from django import forms
from django.contrib.gis import forms as geoforms
from mapwidgets.widgets import GooglePointFieldWidget, GoogleStaticOverlayMapWidget
from .models import User

class Signup_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','location']
        widgets = {
            'location': GooglePointFieldWidget()
        }