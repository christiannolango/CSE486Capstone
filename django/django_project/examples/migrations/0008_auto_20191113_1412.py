# Generated by Django 2.1.7 on 2019-11-13 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examples', '0007_auto_20191103_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snp_entry',
            name='ALT_allele',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='snp_entry',
            name='EFF_score',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='snp_entry',
            name='EFF_var',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='snp_entry',
            name='Meta_p_value',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='snp_entry',
            name='REF_allele',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='snp_entry',
            name='SNP_chromosome_band',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='snp_entry',
            name='SNP_chromosome_location',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='snp_entry',
            name='SNP_hyperlink',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='snp_entry',
            name='SNP_id',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='snp_entry',
            name='SNP_position',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='snp_entry',
            name='SNP_risk',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='snp_entry',
            name='SNP_test',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='snp_entry',
            name='SNP_version',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='snp_entry',
            name='disorder',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='snp_entry',
            name='ethnicity_1000_pop',
            field=models.CharField(blank=True, choices=[('CHB', 'CHB'), ('JPT', 'JPT'), ('CHS', 'CHS'), ('CDX', 'CDX'), ('KHV', 'KHV'), ('CEU', 'CEU'), ('TSI', 'TSI'), ('FIN', 'FIN'), ('GBR', 'GBR'), ('IBS', 'IBS'), ('YRI', 'YRI'), ('LWK', 'LWK'), ('GWD', 'GWD'), ('MSL', 'MSL'), ('ESN', 'ESN'), ('ASW', 'ASW'), ('ACB', 'ACB'), ('MXL', 'MXL'), ('PUR', 'PUR'), ('CLM', 'CLM'), ('PEL', 'PEL'), ('GIH', 'GIH'), ('PJL', 'PJL'), ('BEB', 'BEB'), ('STU', 'STU'), ('ITU', 'ITU')], max_length=30),
        ),
        migrations.AlterField(
            model_name='snp_entry',
            name='gene_band',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='snp_entry',
            name='gene_chr',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='snp_entry',
            name='gene_end',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='snp_entry',
            name='gene_ensmbl_id',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='snp_entry',
            name='gene_hyperlink',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='snp_entry',
            name='gene_name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='snp_entry',
            name='gene_risk_status',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='snp_entry',
            name='gene_start',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='snp_entry',
            name='mtc_pvalue',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='snp_entry',
            name='odds_risk',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='snp_entry',
            name='odds_risk_lci',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='snp_entry',
            name='odds_risk_uci',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='study',
            name='Case_N',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='study',
            name='Case_age',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='study',
            name='Case_perc_fem',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='study',
            name='Control_N',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='study',
            name='Control_age',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='study',
            name='Control_perc_fem',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='study',
            name='DX',
            field=models.CharField(blank=True, choices=[('C', 'C'), ('F', 'F'), ('B', 'B'), ('L', 'L')], max_length=30),
        ),
        migrations.AlterField(
            model_name='study',
            name='SD_score',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='study',
            name='ascertainment',
            field=models.CharField(blank=True, choices=[('African', 'African'), ('Ad Mixed American', 'Ad Mixed American'), ('East Asian', 'East Asian'), ('European', 'European'), ('South Asian', 'South Asian'), ('All', 'All')], max_length=30),
        ),
        migrations.AlterField(
            model_name='study',
            name='design',
            field=models.CharField(blank=True, choices=[('GWA', 'GWA'), ('FBAT', 'FBAT'), ('Quantitative', 'Quantitative')], max_length=30),
        ),
        migrations.AlterField(
            model_name='study',
            name='disorder',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='study',
            name='hyperlink',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='study',
            name='mean_score',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='study',
            name='measure_used',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='study',
            name='num_SNPs',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='study',
            name='num_affected',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='study',
            name='num_families',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='study',
            name='num_generations',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='study',
            name='num_polys',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='study',
            name='platform',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='study',
            name='pmid',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='study',
            name='source',
            field=models.CharField(blank=True, choices=[('CL', 'CL'), ('PO', 'PO'), ('CO', 'CO')], max_length=30),
        ),
        migrations.AlterField(
            model_name='study',
            name='test',
            field=models.CharField(blank=True, choices=[('Allele codominant', 'Allele codominant'), ('Dominant', 'Dominant'), ('Recessive', 'Recessive'), ('Over-dominant', 'Over-dominant'), ('Additive', 'Additive')], max_length=30),
        ),
        migrations.AlterField(
            model_name='study',
            name='the_domain',
            field=models.CharField(blank=True, choices=[('reading', 'reading'), ('speech', 'speech'), ('learning', 'learning')], max_length=30),
        ),
        migrations.AlterField(
            model_name='study',
            name='type_of_study',
            field=models.CharField(blank=True, choices=[('GWAS', 'GWAS'), ('Chromosome #', 'Chromosome #'), ('Other', 'Other'), ('cSNP', 'cSNP'), ('Pooled', 'Pooled'), ('Candidate Gene', 'Candidate Gene')], max_length=30),
        ),
    ]
