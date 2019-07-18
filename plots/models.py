from django.db import models
from django.core.validators import MaxValueValidator
from django.urls import reverse

""" 
klasy najwyższego poziomu NIE WIDZĄ klas, które są do nich przyczepione

"""

class Cemetary(models.Model): #najszersza klasa, do której będą podporządkowane inne obiekty - na początek
	cemetary_name = models.CharField(max_length=30, default='cmentarz')
	cemetary_horizontical = models.IntegerField(default=25,
		validators=[MaxValueValidator(100, 'Cmentarz jest za duży')])

	cemetary_vertical = models.IntegerField(default=25,
		validators=[MaxValueValidator(100, 'Cmentarz jest za duży')])

	def get_absolute_url(self):
		return reverse('cemetary_list')

	def __str__(self):
		return f"{self.cemetary_name}"

	@property #property = coś jak pole, tyle że niedostępne dla użytkownika, zwracające jakąś wartość (w tym przypadku maks. liczbę miejsc na cmentarzu)
	def allplaces(self):
		return self.cemetary_horizontical * self.cemetary_vertical
	

class Place(models.Model):
	horizontal = models.IntegerField()
	vertical = models.IntegerField()
	cemetary = models.ForeignKey(
		Cemetary,
		on_delete = models.CASCADE,
		related_name = 'places',
	)

	def __str__(self):
		return f"H{self.horizontal} x V{self.vertical}"

class DeadPerson(models.Model):
	name = models.CharField(max_length=30)
	second_name = models.CharField(max_length=30, null=True)
	surname = models.CharField(max_length=30)
	birth_date = models.DateField('birth date')
	death_date = models.DateField('death date')

	place = models.OneToOneField( #one-to-one relationship = jeden rekord z jednej tabeli odpowiada jednemu rekordowi z innej tabeli
		Place,
		on_delete=models.CASCADE,
		primary_key=True,
	)

	def get_absolute_url(self):
		return reverse('deadperson_list')

	def __str__(self):
		return f"{self.surname} {self.name}" #f-string!!!