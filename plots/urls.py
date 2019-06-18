from django.urls import path

from . import views

urlpatterns = [
	path('', views.DeadPersonIndexView.as_view(), name='index'),
	path('<int:pk>/detail', views.DeadPersonDetailView.as_view(), name='detail'), #rozkmin montowanie urli i przekazywanie obiektow
	path('add', views.DeadPersonCreateView.as_view(), name='add'),
	path('<int:pk>/edit', views.DeadPersonEditView.as_view(), name='edit'),
	path('<int:pk>/delete', views.DeadPersonDeleteView.as_view(), name='delete'),

]