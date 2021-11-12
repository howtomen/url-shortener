'''
Shortener Forms urlshortener/forms.py
'''
from django import forms
from .models import Shortener

class ShortenerForm(form.ModelForm):
	long_url = forms.URLFIELD(widget = forms.URLInput(
		attrs={"class": "form-control form-control-lg", "placeholder": "Your URL to shorten"}))

	class Meta:
		model = Shortener

		fields = ('long_url',)
