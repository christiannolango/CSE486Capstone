from django.shortcuts import render
from django.http import HttpResponse
from examples.models import study
from examples.models import SimpleTable
from examples.models import SNP_entry
from django.template.response import TemplateResponse
from itertools import chain
import simplejson as json
# Create your views here.
def home(request):
	return render(request, 'pages/home.html')
	
def get_GENE(request):
	if request.method == 'GET':
		studyId = request.GET['text_box']
		data1 = study.objects.all()
		data2 = SNP_entry.objects.all()
		data1 = study.objects.filter(study_id=studyId)
		studyDetails = data1[0].study_id
		data2 = SNP_entry.objects.filter(study_id = studyDetails)
		#data3 = chain(data1, data2)
		table = SimpleTable(data2, template_name='django_tables2/bootstrap-responsive.html')
		return render(request, 'pages/database.html', {'table': table})
		
def get_entryId(request):
	if request.method == 'GET':
		entryId = request.GET['text_box']
		data = SNP_entry.objects.all()
		data = SNP_entry.objects.filter(entry_id=entryId)
		table = SimpleTable(data, template_name='django_tables2/bootstrap-responsive.html')
		return render(request, 'pages/database.html', {'table': table})
	
def index(request):
	return render(request, 'pages/index.html')

def results(request):
	return render(request, 'pages/results.html')

def methods(request):
	return render(request, 'pages/methods.html')

def about(request):
	return render(request, 'pages/about.html')

def contacts(request):
	return render(request, 'pages/contact.html')

def input(request):
	return render(request, 'pages/input.html')

def gene(request):
	return render(request, 'pages/gene.html')

def search(request):
	return render(request, 'pages/search.html')

def database(request):
	data = study.objects.all()
	table = SimpleTable(data, template_name='django_tables2/bootstrap-responsive.html')
	return render(request, 'pages/database.html', {'table': table})
	#return TemplateResponse(request, 'pages/disorders.html',{"data": data})

