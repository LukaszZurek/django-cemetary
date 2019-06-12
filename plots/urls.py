from django.urls import path

from . import views

urlpatterns = [
	path('', views.DeadPersonIndexView.as_view(), name='index'),
	path('<int:pk>/', views.DeadPersonDetailView.as_view(), name='detail'), #rozkmin montowanie urli i przekazywanie obiektow
	path('<int:pk>/edit', views.DeadPersonEditView.as_view(), name='edit'),

]