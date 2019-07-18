from django.forms import ModelForm
import datetime
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _ #co to kurwa jest

from plots.models import DeadPerson, Cemetary

class DeadPersonForm(ModelForm): #przerabiam mój model na reprezentację formularzową, to jest ZAJEBIŚCIE przydatne przy walidacji inputu użytkownika (bo zamiast wpierdalać logikę w templatkę, załątwiam to tutaj) 
	class Meta:
		model = DeadPerson
		fields = '__all__'

	def clean_death_date(self):
		death_date = self.cleaned_data['death_date']
		if death_date > datetime.date.today(): #spr. czy nieboszczyk nie umarł w... przyszłości
			raise ValidationError(_('Osoba pochowana w naszym cmentarzu nie może umrzeć w przyszłości'))
		return death_date #walidacja zakończona - konieczny jest return
		
	def clean_birth_date(self):
		birth_date = self.cleaned_data['birth_date']
		if birth_date > datetime.date.today(): #spr. czy nieboszczyk nie urodził się w... przyszłości
			raise ValidationError(_('Osoba pochowana w naszym cmentarzy jeszcze się nie urodziła'))
		return birth_date

class CemetaryForm(ModelForm):
	class Meta:
		model = Cemetary
		fields = '__all__'