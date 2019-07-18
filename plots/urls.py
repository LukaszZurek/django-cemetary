from django.urls import path

from . import views

urlpatterns = [
	path('', views.CemetaryListView.as_view(), name='cemetary_list'),
	path('cemetary/add', views.CemetaryCreateView.as_view(), name='cemetary_add'),
	path('cemetary/<int:pk>/detail', views.CemetaryDetailView.as_view(), name='cemetary_detail'),
	path('person/add', views.DeadPersonCreateView.as_view(), name='deadperson_add'),
	path('person/on_cemetary/<int:cemetary_pk>', views.DeadPersonListView.as_view(), name='deadperson_list'),
	path('person/on_cemetary/<int:pk>/detail', views.DeadPersonDetailView.as_view(), name='deadperson_detail'),
	path('person/<int:pk>/edit', views.DeadPersonEditView.as_view(), name='deadperson_edit'),
	path('person/<int:pk>/delete', views.DeadPersonDeleteView.as_view(), name='deadperson_delete'),

]