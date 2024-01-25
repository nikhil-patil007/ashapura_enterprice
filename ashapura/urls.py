from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('api/uploadtodbusingcsv',views.uploadTheCSV),
    path('api/searchingvehicledata',views.searchVehicle)
]