# Generated by Django 2.1.7 on 2019-11-22 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examples', '0015_auto_20191115_1356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snp_entry',
            name='Author',
        ),
        migrations.RemoveField(
            model_name='snp_entry',
            name='Year',
        ),
        migrations.AddField(
            model_name='study',
            name='Author',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='study',
            name='Year',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='study',
            name='DX',
            field=models.CharField(blank=True, choices=[('C', 'C'), ('F', 'F'), ('B', 'B'), ('L', 'L')], max_length=30),
        ),
        migrations.AlterField(
            model_name='study',
            name='source',
            field=models.CharField(blank=True, choices=[('CL', 'CL'), ('PO', 'PO'), ('CO', 'CO')], max_length=30),
        ),
    ]
