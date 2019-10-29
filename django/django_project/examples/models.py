from django.db import models
from django import forms
import django_tables2 as tables
from itertools import chain


# Create your models here.
class study(models.Model):
    study_id = models.IntegerField(primary_key=True)
    pmid = models.CharField(max_length=30)
    design = models.CharField(max_length=30)
    type_of_study = models.CharField(max_length=30)
    ascertainment = models.CharField(max_length=30)
    source = models.CharField(max_length=30)
    platform = models.CharField(max_length=30)
    the_domain = models.CharField(max_length=30)
    num_SNPs = models.IntegerField()
    num_polys = models.IntegerField()
    DX = models.CharField(max_length=30)
    Case_N = models.IntegerField()
    Case_perc_fem = models.FloatField()
    Case_age = models.FloatField()
    Control_N = models.IntegerField()
    Control_perc_fem = models.FloatField()
    Control_age = models.FloatField()
    num_families = models.IntegerField()
    num_affected = models.IntegerField()
    num_generations = models.IntegerField()
    mean_score = models.FloatField()
    SD_score = models.FloatField()
    measure_used = models.CharField(max_length=30)
    disorder = models.CharField(max_length=30)
    test = models.CharField(max_length=30)
    hyperlink = models.CharField(max_length=30)

    def __unicode__(self):
        self.study_id


class SNP_entry(models.Model):
    entry_id = models.IntegerField(primary_key=True)
    SNP_id = models.CharField(max_length=30)
    Meta_p_value = models.FloatField()
    SNP_chromosome_location = models.CharField(max_length=30)
    SNP_chromosome_band = models.CharField(max_length=30)
    SNP_position = models.IntegerField()
    SNP_version = models.CharField(max_length=30)
    odds_risk = models.FloatField()
    odds_risk_lci = models.FloatField()
    odds_risk_uci = models.FloatField()
    ethnicity_1000_pop = models.CharField(max_length=30)
    REF_allele = models.CharField(max_length=30)
    ALT_allele = models.CharField(max_length=30)
    EFF_score = models.FloatField()
    EFF_var = models.FloatField()
    mtc_pvalue = models.FloatField()
    SNP_risk = models.CharField(max_length=30)
    SNP_test = models.CharField(max_length=30)
    SNP_hyperlink = models.CharField(max_length=30)
    gene_name = models.CharField(max_length=30)
    gene_ensmbl_id = models.IntegerField()
    gene_chr = models.CharField(max_length=30)
    gene_band = models.CharField(max_length=30)
    gene_start = models.IntegerField()
    gene_end = models.IntegerField()
    gene_risk_status = models.CharField(max_length=30)
    gene_hyperlink = models.CharField(max_length=30)
    disorder = models.CharField(max_length=30)
    study_id = models.ForeignKey(study, on_delete=models.CASCADE)

    def __unicode__(self):
        self.enrty_id

class SimpleTable(tables.Table):
#study
    study_id = tables.Column(accessor="study_id.study_id")
    pmid = tables.Column(accessor="study_id.pmid")
    design = tables.Column(accessor="study_id.design")
    type_of_study = tables.Column(accessor="study_id.type_of_study")
    ascertainment = tables.Column(accessor="study_id.ascertainment")
    source = tables.Column(accessor="study_id.source")
    platform = tables.Column(accessor="study_id.platform")
    the_domain = tables.Column(accessor="study_id.the_domain")
    num_SNPs = tables.Column(accessor="study_id.num_SNPs")
    num_polys = tables.Column(accessor="study_id.num_polys")
    DX = tables.Column(accessor="study_id.DX")
    Case_N = tables.Column(accessor="study_id.Case_N")
    Case_perc_fem = tables.Column(accessor="study_id.Case_perc_fem")
    Case_age = tables.Column(accessor="study_id.Case_age")
    Control_N = tables.Column(accessor="study_id.Control_N")
    Control_perc_fem = tables.Column(accessor="study_id.Control_perc_fem")
    Control_age = tables.Column(accessor="study_id.Control_age")
    num_families = tables.Column(accessor="study_id.num_families")
    num_affected = tables.Column(accessor="study_id.num_affected")
    num_generations = tables.Column(accessor="study_id.num_generations")
    mean_score = tables.Column(accessor="study_id.mean_score")
    SD_score = tables.Column(accessor="study_id.SD_score")
    measure_used = tables.Column(accessor="study_id.measure_used")
    disorder = tables.Column(accessor="study_id.disorder")
    test = tables.Column(accessor="study_id.test")
    hyperlink = tables.Column(accessor="study_id.hyperlink")
	
#SNP
    entry_id = tables.Column()
    SNP_id = tables.Column()
    Meta_p_value = tables.Column()
    SNP_chromosome_location = tables.Column()
    SNP_chromosome_band = tables.Column()
    SNP_position = tables.Column()
    SNP_version = tables.Column()
    odds_risk = tables.Column()
    odds_risk_lci = tables.Column()
    odds_risk_uci = tables.Column()
    ethnicity_1000_pop = tables.Column()
    REF_allele = tables.Column()
    ALT_allele = tables.Column()
    EFF_score = tables.Column()
    EFF_var = tables.Column()
    mtc_pvalue = tables.Column()
    SNP_risk = tables.Column()
    SNP_test = tables.Column()
    SNP_hyperlink = tables.Column()
    
#Gene
    gene_name = tables.Column()
    gene_ensmbl_id = tables.Column()
    gene_chr = tables.Column()
    gene_band = tables.Column()
    gene_start = tables.Column()
    gene_end = tables.Column()
    gene_risk_status = tables.Column()
    gene_hyperlink = tables.Column()
	
#Disorder
    disorder = tables.Column()
	

	
