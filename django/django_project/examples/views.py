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

		excel_data(workbook, worksheet1, worksheet2, filterGene)

		table = SimpleTable(filterGene, template_name='django_tables2/bootstrap-responsive.html')
		return render(request, 'pages/database.html', {'table': table})
		
		
def get_SNP(request):
	if request.method == 'GET':
		SNPname = request.GET['text_box']
		studyData = study.objects.all()
		SNPData = SNP_entry.objects.all()
		filterSNP = SNP_entry.objects.filter(SNP_id=SNPname)

		# WRITE TO EXCEL FILE
		if os.path.exists('SNPData.xlsx'): os.remove('SNPData.xlsx')
		workbook = xlsxwriter.Workbook('SNPData.xlsx')
		worksheet1 = workbook.add_worksheet('studyData')
		worksheet2 = workbook.add_worksheet('SNP_entryData')

		excel_data(workbook, worksheet1, worksheet2, filterSNP)

		table = SimpleTable(filterSNP, template_name='django_tables2/bootstrap-responsive.html')
		return render(request, 'pages/database.html', {'table': table})
		
def get_Disorder(request):
	if request.method == 'GET':
		disorder_num = request.GET['dropdown']
		studyData = study.objects.all()
		SNPData = SNP_entry.objects.all()
		filterDisorder = SNP_entry.objects.filter(disorder=disorder_num)

		# WRITE TO EXCEL FILE
		if os.path.exists('DisorderData.xlsx'): os.remove('DisorderData.xlsx')
		workbook = xlsxwriter.Workbook('DisorderData.xlsx')
		worksheet1 = workbook.add_worksheet('studyData')
		worksheet2 = workbook.add_worksheet('SNP_entryData')

		excel_data(workbook, worksheet1, worksheet2, filterDisorder)

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

	retcode = subprocess.call("Rscript --vanilla examples/metaAnalysis.Rmd", shell=True)
	return render(request, 'pages/gene.html')

def search(request):
	return render(request, 'pages/search.html')

def database(request):
	data = study.objects.all()
	table = SimpleTable(data, template_name='django_tables2/bootstrap-responsive.html')
	return render(request, 'pages/database.html', {'table': table})
	#return TemplateResponse(request, 'pages/disorders.html',{"data": data})

def excel_data(workbook, worksheet1, worksheet2, filter):
	row = 0
	# write headers
	worksheet1.write(row, 0, "studyId")
	worksheet1.write(row, 1, "Pmid")
	worksheet1.write(row, 2, "design")
	worksheet1.write(row, 3, "type of study")
	worksheet1.write(row, 4, "ascertainment")
	worksheet1.write(row, 5, "source")
	worksheet1.write(row, 6, "platform")
	worksheet1.write(row, 7, "the_domain")
	worksheet1.write(row, 8, "num_SNPs")
	worksheet1.write(row, 9, "num_polys")
	worksheet1.write(row, 10, "DX")
	worksheet1.write(row, 11, "Case_N")
	worksheet1.write(row, 12, "Case_perc_fem")
	worksheet1.write(row, 13, "Case_age")
	worksheet1.write(row, 14, "Control_N")
	worksheet1.write(row, 15, "Control_perc_fem")
	worksheet1.write(row, 16, "Control_age")
	worksheet1.write(row, 17, "num_families")
	worksheet1.write(row, 18, "num_affected")
	worksheet1.write(row, 19, "num_generations")
	worksheet1.write(row, 20, "mean_score")
	worksheet1.write(row, 21, "SD_score")
	worksheet1.write(row, 22, "measure_used")
	worksheet1.write(row, 23, "disorder")
	worksheet1.write(row, 24, "test")
	worksheet1.write(row, 25, "hyperlink")

	worksheet2.write(row, 0, "entryId")
	worksheet2.write(row, 1, "SNP_id")
	worksheet2.write(row, 2, "Meta_p_value")
	worksheet2.write(row, 3, "SNP_chromosome_location")
	worksheet2.write(row, 4, "SNP_chromosome_band")
	worksheet2.write(row, 5, "SNP_position")
	worksheet2.write(row, 6, "SNP_version")
	worksheet2.write(row, 7, "odds_risk")
	worksheet2.write(row, 8, "odds_risk_lci")
	worksheet2.write(row, 9, "odds_risk_uci")
	worksheet2.write(row, 10, "ethnicity_1000_pop")
	worksheet2.write(row, 11, "REF_allele")
	worksheet2.write(row, 12, "ALT_allele")
	worksheet2.write(row, 13, "EFF_score")
	worksheet2.write(row, 14, "EFF_var")
	worksheet2.write(row, 15, "mtc_pvalue")
	worksheet2.write(row, 16, "SNP_risk")
	worksheet2.write(row, 17, "SNP_test")
	worksheet2.write(row, 18, "SNP_hyperlink")
	worksheet2.write(row, 19, "gene_name")
	worksheet2.write(row, 20, "gene_ensmbl_id")
	worksheet2.write(row, 21, "gene_chr")
	worksheet2.write(row, 22, "gene_band")
	worksheet2.write(row, 23, "gene_start")
	worksheet2.write(row, 24, "gene_end")
	worksheet2.write(row, 25, "gene_risk_status")
	worksheet2.write(row, 26, "gene_hyperlink")
	worksheet2.write(row, 27, "disorder")

	row = 1
	# write data
	for g in filter:
		col = 0
		worksheet1.write(row, col, g.study_id.study_id)
		worksheet1.write(row, col + 1, g.study_id.pmid)
		worksheet1.write(row, col + 2, g.study_id.design)
		worksheet1.write(row, col + 3, g.study_id.type_of_study)
		worksheet1.write(row, col + 4, g.study_id.ascertainment)
		worksheet1.write(row, col + 5, g.study_id.source)
		worksheet1.write(row, col + 6, g.study_id.platform)
		worksheet1.write(row, col + 7, g.study_id.the_domain)
		worksheet1.write(row, col + 8, g.study_id.num_SNPs)
		worksheet1.write(row, col + 9, g.study_id.num_polys)
		worksheet1.write(row, col + 10, g.study_id.DX)
		worksheet1.write(row, col + 11, g.study_id.Case_N)
		worksheet1.write(row, col + 12, g.study_id.Case_perc_fem)
		worksheet1.write(row, col + 13, g.study_id.Case_age)
		worksheet1.write(row, col + 14, g.study_id.Control_N)
		worksheet1.write(row, col + 15, g.study_id.Control_perc_fem)
		worksheet1.write(row, col + 16, g.study_id.Control_age)
		worksheet1.write(row, col + 17, g.study_id.num_families)
		worksheet1.write(row, col + 18, g.study_id.num_affected)
		worksheet1.write(row, col + 19, g.study_id.num_generations)
		worksheet1.write(row, col + 20, g.study_id.mean_score)
		worksheet1.write(row, col + 21, g.study_id.SD_score)
		worksheet1.write(row, col + 22, g.study_id.measure_used)
		worksheet1.write(row, col + 23, g.study_id.disorder)
		worksheet1.write(row, col + 24, g.study_id.test)
		worksheet1.write(row, col + 25, g.study_id.hyperlink)
		worksheet2.write(row, col, g.entry_id)
		worksheet2.write(row, col + 1, g.SNP_id)
		worksheet2.write(row, col + 2, g.Meta_p_value)
		worksheet2.write(row, col + 3, g.SNP_chromosome_location)
		worksheet2.write(row, col + 4, g.SNP_chromosome_band)
		worksheet2.write(row, col + 5, g.SNP_position)
		worksheet2.write(row, col + 6, g.SNP_version)
		worksheet2.write(row, col + 7, g.odds_risk)
		worksheet2.write(row, col + 8, g.odds_risk_lci)
		worksheet2.write(row, col + 9, g.odds_risk_uci)
		worksheet2.write(row, col + 10, g.ethnicity_1000_pop)
		worksheet2.write(row, col + 11, g.REF_allele)
		worksheet2.write(row, col + 12, g.ALT_allele)
		worksheet2.write(row, col + 13, g.EFF_score)
		worksheet2.write(row, col + 14, g.EFF_var)
		worksheet2.write(row, col + 15, g.mtc_pvalue)
		worksheet2.write(row, col + 16, g.SNP_risk)
		worksheet2.write(row, col + 17, g.SNP_test)
		worksheet2.write(row, col + 18, g.SNP_hyperlink)
		worksheet2.write(row, col + 19, g.gene_name)
		worksheet2.write(row, col + 20, g.gene_ensmbl_id)
		worksheet2.write(row, col + 21, g.gene_chr)
		worksheet2.write(row, col + 22, g.gene_band)
		worksheet2.write(row, col + 23, g.gene_start)
		worksheet2.write(row, col + 24, g.gene_end)
		worksheet2.write(row, col + 25, g.gene_risk_status)
		worksheet2.write(row, col + 26, g.gene_hyperlink)
		worksheet2.write(row, col + 27, g.disorder)
		row += 1
	workbook.close()

