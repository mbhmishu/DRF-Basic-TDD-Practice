from django.contrib import admin
from .models import Customer


# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('title','first_name','last_name','full_name','gender','created_by','edited_at','created_at','status')
    readonly_fields =('created_at','edited_at')
    def full_name(self,obj):
        return obj.first_name + ' ' + obj.last_name 
admin.site.register(Customer,CustomerAdmin)


    
