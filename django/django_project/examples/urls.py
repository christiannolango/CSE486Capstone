from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='pages-home'),
    path('index/', views.index, name='pages-about'),
    path('results/', views.results, name='pages-results'),
    path('methods/', views.methods, name='pages-methods'),
    path('about/', views.about, name='pages-about'),
    path('contacts/', views.contacts, name='pages-contacts'),
    path('input/', views.input, name='pages-input'),
    path('database/', views.database, name='pages-database'),
    path('gene/', views.gene, name = 'pages-gene'),
    path('search/', views.search, name = 'pages-search'),
	path('<str:pmId>', views.get_pmId),
]