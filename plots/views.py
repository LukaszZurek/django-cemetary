from django.urls import reverse, reverse_lazy
from django.views import generic

from plots.models import DeadPerson, Cemetary
from plots.forms import DeadPersonForm, CemetaryForm

# adminlukasz
# projekt91

class DeadPersonListView(generic.ListView):
	template_name = 'plots/deadperson_list.html'
	context_object_name = 'dead_person_list'

	def get_queryset(self):
		cemetary_pk = self.kwargs.get('cemetary_pk') #wyciągam z kwargów (zmiennych przesyłanych w urlu) wartość powiązaną z querysetem. W tym przypadku: primary key cmentarza
		return DeadPerson.objects.filter(place__cemetary__pk=cemetary_pk) #zwracam queryset posortowany wg pk cmentarza. Składnia z dwiema podłogami ('__') jest charakterystyczna dla ORM-u
		if not cemetary_pk:
			return DeadPerson.objects.all()

class DeadPersonCreateView(generic.CreateView):
	model = DeadPerson
	form_class = DeadPersonForm
	template_name_suffix = '_add'

"""ROZKMINA (17-07-2019)
jak zrobić, żeby tworzenie osoby było równoznaczne z tworzeniem dla niej miejsca/kwatery na cmentarzu?

Django Signals
"""
class DeadPersonDetailView(generic.DetailView):
	model = DeadPerson
	template_name = 'plots/deadperson_detail.html'

class DeadPersonEditView(generic.UpdateView):
	model = DeadPerson
	template_name_suffix = '_update'
	form_class = DeadPersonForm

class DeadPersonDeleteView(generic.DeleteView):
	model = DeadPerson
	template_name = 'plots/deadperson_confirm_delete.html'

	def get_success_url(self):
		return reverse_lazy('index')

class CemetaryCreateView(generic.CreateView):
	model = Cemetary
	form_class = CemetaryForm
	template_name = 'plots/cemetary_add.html'

class CemetaryListView(generic.ListView):
	template_name = 'plots/cemetary_list.html'
	context_object_name = 'cemetary_list'

	def get_queryset(self):
		return Cemetary.objects.order_by('cemetary_name')

class CemetaryDetailView(generic.DetailView):
	model = Cemetary
	template_name = 'plots/cemetary_detail.html'

"""ROZKMINA (17-07-2019)
wyciągnąć z querysetu liczbę miejsc (która na razie jest równa liczbie zajętych miejsc)
"""

#CemetaryDeleteView
#CemetaryEditView