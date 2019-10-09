from django.db import models
from django import forms
import django_tables2 as tables


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
    enrty_id = models.IntegerField(primary_key=True)
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
    class Meta:
        model = study
