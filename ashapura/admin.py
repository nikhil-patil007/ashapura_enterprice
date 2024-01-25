from django.contrib import admin
from .models import *

# Register your models here.

admin.site.site_header = 'Ashapura Administration'
admin.site.site_title = 'Ashapura Admin'
admin.site.index_title = 'Welcome to Ashapura Enterprise Admin'

class vehicalDetailsAdmin(admin.ModelAdmin):
    # model = Categories
    list_per_page = 15 # No of records per page 
    list_display = ('id',"customer_name","account_no","center","executive","segment","product_name","new_vehicle_number","engine_number","chasis_number","created_at","updated_at")
    list_display_links = ('id',"customer_name","account_no","center","executive","segment","product_name","new_vehicle_number","engine_number","chasis_number","created_at","updated_at")
    ordering = ('-id'),
    list_filter = ('center'),
    search_fields = ('customer_name','center','product_name','new_vehicle_number')
    
admin.site.register(Vehicledetails,vehicalDetailsAdmin)