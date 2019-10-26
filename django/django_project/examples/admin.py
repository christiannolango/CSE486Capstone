from django.contrib import admin
from examples.models import study
from examples.models import SNP_entry

# Register your models here.

admin.site.register(study)
admin.site.register(SNP_entry)

