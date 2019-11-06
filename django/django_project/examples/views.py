from django.shortcuts import render
from django.http import HttpResponse
from examples.models import study
from examples.models import SimpleTable
from examples.models import SNP_entry
from django.template.response import TemplateResponse
from itertools import chain
import simplejson as json
import xlsxwriter
import subprocess
import os
# Create your views here.
def home(request):
	return render(request, 'pages/home.html')
	
def get_GENE(request):
	if request.method == 'GET':
		geneName = request.GET['text_box']
		studyData = study.objects.all()
		SNPData = SNP_entry.objects.all()
		filterGene = SNP_entry.objects.filter(gene_name=geneName)
		
		#WRITE TO EXCEL FILE
		if os.path.exists('geneData.xlsx'): os.remove('geneData.xlsx')
		workbook = xlsxwriter.Workbook('geneData.xlsx')
		worksheet1 = workbook.add_worksheet('studyData')
		worksheet2 = workbook.add_worksheet('SNP_entryData')
		row=0
		
		#write headers
		worksheet1.write(row,0,"studyId")
		worksheet1.write(row,1,"Pmid")
		worksheet1.write(row,2,"design")
		worksheet1.write(row,3,"type of study")
		
		worksheet2.write(row, 0, "entryId")
		row=1
		#write data
		for g in filterGene: 
			col=0
			worksheet1.write(row,col,g.study_id.study_id)
			worksheet1.write(row,col+1,g.study_id.pmid)
			worksheet1.write(row,col+2,g.study_id.design)
			worksheet1.write(row,col+3,g.study_id.type_of_study)
			worksheet2.write(row, col, g.entry_id)
			row+=1
		workbook.close()
		
		table = SimpleTable(filterGene, template_name='django_tables2/bootstrap-responsive.html')
		return render(request, 'pages/database.html', {'table': table})
		
		
def get_SNP(request):
	if request.method == 'GET':
		SNPname = request.GET['text_box']
		studyData = study.objects.all()
		SNPData = SNP_entry.objects.all()
		filterSNP = SNP_entry.objects.filter(SNP_id=SNPname)
		table = SimpleTable(filterSNP, template_name='django_tables2/bootstrap-responsive.html')
		return render(request, 'pages/database.html', {'table': table})
		
def get_Disorder(request):
	if request.method == 'GET':
		disorder_num = request.GET['dropdown']
		studyData = study.objects.all()
		SNPData = SNP_entry.objects.all()
		filterDisorder = SNP_entry.objects.filter(disorder=disorder_num)
		table = SimpleTable(filterDisorder, template_name='django_tables2/bootstrap-responsive.html')
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

	
#Trigger Rscript
def gene(request):

	retcode = subprocess.call("Rscript --vanilla examples/easyR.r", shell=True)
	return render(request, 'pages/gene.html')

def search(request):
	return render(request, 'pages/search.html')

def database(request):
	data = study.objects.all()
	table = SimpleTable(data, template_name='django_tables2/bootstrap-responsive.html')
	return render(request, 'pages/database.html', {'table': table})
	#return TemplateResponse(request, 'pages/disorders.html',{"data": data})

