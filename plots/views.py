from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from datetime import datetime
from django.urls import reverse, reverse_lazy
from django.views import generic

from plots.models import DeadPerson
from plots.forms import DeadPersonForm

# admin
# hello567

class DeadPersonIndexView(generic.ListView):
	template_name = 'plots/index.html'
	context_object_name = 'dead_person_list'

	def get_queryset(self):
		return DeadPerson.objects.order_by('surname')

class DeadPersonCreateView(generic.CreateView):
	model = DeadPerson
	form_class = DeadPersonForm
	template_name_suffix = '_add'

class DeadPersonDetailView(generic.DetailView):
	model = DeadPerson
	template_name = 'plots/detail.html'

class DeadPersonEditView(generic.UpdateView):
	model = DeadPerson
	template_name_suffix = '_update'
	form_class = DeadPersonForm

class DeadPersonDeleteView(generic.DeleteView):
	model = DeadPerson
	template_name = 'plots/deadperson_confirm_delete.html'

	def get_success_url(self):
		return reverse_lazy('index')

""" co dalej?
- dodawanie i usuwanie TYLKO z poziomu admina
- widok loginu 

"""