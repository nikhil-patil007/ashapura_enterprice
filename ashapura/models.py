from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField( max_length=255,null=True,blank=True)
    username = models.CharField( max_length=255,null=True,blank=True)
    password = models.CharField( max_length=255,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

# class Vehicledetails(models.Model):
#     customer_name = models.CharField( max_length=255,null=True,blank=True)
#     account_no = models.CharField( max_length=255,null=True,blank=True)
#     center = models.CharField( max_length=255,null=True,blank=True)
#     executive = models.CharField( max_length=255,null=True,blank=True)
#     segment = models.CharField( max_length=255,null=True,blank=True)
#     product_name = models.CharField( max_length=255,null=True,blank=True)
#     new_vehicle_number = models.CharField( max_length=255,null=True,blank=True)
#     engine_number = models.CharField( max_length=255,null=True,blank=True)
#     chasis_number = models.CharField( max_length=255,null=True,blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
    
#     class Meta:
#         db_table = "AshaPura_Vehicle_details"
    
#     def __str__(self):
#         return self.customer_name