from django.contrib import admin
from in_progress.models import In_Progress

# Register your models here.
class In_ProgressAdmin(admin.ModelAdmin):
    pass

admin.site.register(In_Progress, In_ProgressAdmin)