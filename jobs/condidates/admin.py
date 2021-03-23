from django.contrib import admin
from .models import Condidate,CondidateJobMapping
from import_export.admin import ImportExportModelAdmin
from import_export import resources

class CondidateResource(resources.ModelResource):
    class Meta:
        model = Condidate

class CondidateAdmin(ImportExportModelAdmin):
    list_display = ('name','mobile','age','gender','city','will_relocate','is_engaged',)
    list_filter = ('gender','city','will_relocate')
    resource_class = CondidateResource


class ReviewCondidateAdmin(admin.ModelAdmin):
    list_display = ('name','mobile','age','gender','city','will_relocate','jobs','status',)
    list_filter = ('jobs',)
    list_display_links = None


admin.site.register(Condidate,CondidateAdmin)
admin.site.register(CondidateJobMapping,ReviewCondidateAdmin)
