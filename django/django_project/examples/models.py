from django.db import models
from django import forms
import django_tables2 as tables
from itertools import chain


# Create your models here.



class study(models.Model):
    enum_design = (
        ('GWA', 'GWA'),
        ('FBAT', 'FBAT'),
        ('Quantitative', 'Quantitative'),
    )
    enum_disorder_t = (
        ('reading', 'reading'),
        ('speech', 'speech'),
        ('learning', 'learning'),
    )
    enum_population = (
        ('African', 'African'),
        ('Ad Mixed American', 'Ad Mixed American'),
        ('East Asian', 'East Asian'),
        ('European', 'European'),
        ('South Asian', 'South Asian'),
        ('All', 'All'),
    )
    enum_type_of_stud = (
        ('GWAS', 'GWAS'),
        ('Chromosome #', 'Chromosome #'),
        ('Other', 'Other'),
        ('cSNP', 'cSNP'),
        ('Pooled', 'Pooled'),
        ('Candidate Gene', 'Candidate Gene'),
    )
    enum_diagnosis = (
        ('C', 'C'),
        ('F', 'F'),
        ('B', 'B'),
        ('L', 'L'),
    )
    enum_source_type = (
        ('CL', 'CL'),
        ('PO', 'PO'),
        ('CO', 'CO'),
    )
    enum_test_type = (
        ('Allele codominant', 'Allele codominant'),
        ('Dominant', 'Dominant'),
        ('Recessive', 'Recessive'),
        ('Over-dominant', 'Over-dominant'),
        ('Additive', 'Additive'),
    )


    study_id = models.IntegerField(primary_key=True)
    pmid = models.CharField(max_length=30, blank=True)
    design = models.CharField(max_length=30, choices=enum_design, blank=True)
    type_of_study = models.CharField(max_length=30, choices=enum_type_of_stud, blank=True)
    ethnic_Population = models.CharField(max_length=30, choices=enum_population, blank=True)
    source = models.CharField(max_length=30, choices=enum_source_type, blank=True)
    platform = models.CharField(max_length=30, blank=True)
    the_domain = models.CharField(max_length=30, choices=enum_disorder_t, blank=True)
    num_SNPs = models.IntegerField(blank=True, null=True)
    num_polys = models.IntegerField(blank=True, null=True)
    DX = models.CharField(max_length=30, choices=enum_diagnosis, blank=True)
    Case_N = models.IntegerField(blank=True, null=True)
    Case_perc_fem = models.FloatField(blank=True, null=True)
    Case_age = models.FloatField(blank=True, null=True)
    Control_N = models.IntegerField(blank=True, null=True)
    Control_perc_fem = models.FloatField(blank=True, null=True)
    Control_age = models.FloatField(blank=True, null=True)
    num_families = models.IntegerField(blank=True, null=True)
    num_affected = models.IntegerField(blank=True, null=True)
    num_generations = models.IntegerField(blank=True, null=True)
    mean_score = models.FloatField(blank=True, null=True)
    SD_score = models.FloatField(blank=True, null=True)
    measure_used = models.CharField(max_length=30, blank=True)
    disorder = models.CharField(max_length=30, blank=True)
    test = models.CharField(max_length=30, choices=enum_test_type, blank=True)
    hyperlink = models.CharField(max_length=30, blank=True)

    def __unicode__(self):
        self.study_id


class SNP_entry(models.Model):

    enum_ethnicity = (
        ('CHB', 'CHB'),
        ('JPT', 'JPT'),
        ('CHS', 'CHS'),
        ('CDX', 'CDX'),
        ('KHV', 'KHV'),
        ('CEU', 'CEU'),
        ('TSI', 'TSI'),
        ('FIN', 'FIN'),
        ('GBR', 'GBR'),
        ('IBS', 'IBS'),
        ('YRI', 'YRI'),
        ('LWK', 'LWK'),
        ('GWD', 'GWD'),
        ('MSL', 'MSL'),
        ('ESN', 'ESN'),
        ('ASW', 'ASW'),
        ('ACB', 'ACB'),
        ('MXL', 'MXL'),
        ('PUR', 'PUR'),
        ('CLM', 'CLM'),
        ('PEL', 'PEL'),
        ('GIH', 'GIH'),
        ('PJL', 'PJL'),
        ('BEB', 'BEB'),
        ('STU', 'STU'),
        ('ITU', 'ITU'),

    )


    entry_id = models.IntegerField(primary_key=True)
    Author = models.CharField(max_length=30, blank=True)
    Year = models.CharField(max_length=30, blank=True)
    SNP_id = models.CharField(max_length=30, blank=True)
    Meta_p_value = models.FloatField(blank=True, null=True)
    SNP_chromosome_location = models.CharField(max_length=30, blank=True)
    SNP_chromosome_band = models.CharField(max_length=30, blank=True)
    SNP_position = models.IntegerField(blank=True, null=True)
    SNP_version = models.CharField(max_length=30, blank=True)
    odds_risk = models.FloatField(blank=True, null=True)
    odds_risk_lci = models.FloatField(blank=True, null=True)
    odds_risk_uci = models.FloatField(blank=True, null=True)
    ethnicity_1000_pop = models.CharField(max_length=30, choices=enum_ethnicity, blank=True, null=True)
    REF_allele = models.CharField(max_length=30, blank=True)
    ALT_allele = models.CharField(max_length=30, blank=True)
    EFF_score = models.FloatField(blank=True, null=True)
    EFF_var = models.FloatField(blank=True, null=True)
    mtc_pvalue = models.FloatField(blank=True, null=True)
    SNP_risk = models.CharField(max_length=30, blank=True)
    SNP_test = models.CharField(max_length=30, blank=True)
    SNP_hyperlink = models.CharField(max_length=30, blank=True)
    gene_name = models.CharField(max_length=30, blank=True)
    gene_ensmbl_id = models.CharField(max_length=30, blank=True, null=True)
    gene_chr = models.CharField(max_length=30, blank=True)
    gene_band = models.CharField(max_length=30, blank=True)
    gene_start = models.IntegerField(blank=True, null=True)
    gene_end = models.IntegerField(blank=True, null=True)
    gene_risk_status = models.CharField(max_length=30, blank=True)
    gene_hyperlink = models.CharField(max_length=30, blank=True)
    disorder = models.CharField(max_length=30, blank=True)
    study_id = models.ForeignKey(study, on_delete=models.CASCADE)

    def __unicode__(self):
        self.enrty_id

class SimpleTable(tables.Table):
#study
    study_id = tables.Column(accessor="study_id.study_id")
    pmid = tables.Column(accessor="study_id.pmid")
    design = tables.Column(accessor="study_id.design")
    type_of_study = tables.Column(accessor="study_id.type_of_study")
    ethnic_Population = tables.Column(accessor="study_id.ethnic_Population")
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
	

	
