from django import forms
from django.forms import ModelForm
from registration.models import *

class RegistrationForm(ModelForm):
    class Meta:
        model = Person

class SessionAdditionForm(ModelForm):
    class Meta:
        model = Session
