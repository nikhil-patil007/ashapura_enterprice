from django.urls import path
from . import views

urlpatterns = [
    path('api/uploadtodbusingcsv',views.uploadTheCSV),
    path('api/searchingvehicledata',views.searchVehicle)
]