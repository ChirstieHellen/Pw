from django import forms
from .models import Escola

class Escolasform(forms.ModelForm):
	class Meta:
		model =Escola
		fields = '__all__'

		