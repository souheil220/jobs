from django.contrib import admin
from  .models import NewJob

class JobAdmin(admin.ModelAdmin):
    exclude = ('creator',)
    

    def get_queryset(self,request,*args,**kwargs):
        if request.user.is_superuser:
            return NewJob.objects.all()
        else:
            return NewJob.objects.filter(creator = request.user)

    def get_list_display(self,request,*args,**kwargs):
        if request.user.is_superuser:
            return ('position_name','creator',)
        else:
            return ('position_name',)

    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        obj.save()


admin.site.register(NewJob, JobAdmin)