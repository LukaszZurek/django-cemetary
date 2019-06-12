from django.db import models
from django.core.validators import MaxValueValidator
from django.urls import reverse

class PlaceOnCemetary(models.Model):
	horizontal = models.IntegerField(
		validators=[MaxValueValidator(4, 'Miejsce wykracza poza mapę cmentarza'),]
	)
	vertical = models.IntegerField(
		validators=[MaxValueValidator(4, 'Miejsce wykracza poza mapę cmentarza'),]
	)#mam 25 miejsc na cmentarzu, bo wartości od zera liczone

	def __str__(self):
		return f"H{self.horizontal} x V{self.vertical}"


class DeadPerson(models.Model):
	name = models.CharField(max_length=30)
	second_name = models.CharField(max_length=30, null=True)
	surname = models.CharField(max_length=30)
	birth_date = models.DateField('birth date')
	death_date = models.DateField('death date')

	place = models.OneToOneField( #one-to-one relationship = jeden rekord z jednej tabeli odpowiada jednemu rekordowi z innej tabeli
		PlaceOnCemetary,
		on_delete=models.CASCADE,
		primary_key=True,
	)

	def get_absolute_url(self):
		return reverse('index')

	def __str__(self): #dzięki temu w QuerySet instancje będą identyfikowane po jednym z pól danych
		return f"{self.surname} {self.name}" #f-string!!!