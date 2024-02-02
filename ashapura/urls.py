from django.urls import path
from . import views
from . import templatesview

urlpatterns = [
    # Templates Path
    path('loginpage/', templatesview.loginPage, name='loginpage'),
    path('login/user/', templatesview.loginUser, name='loginUser'),
    path('login/user/<str:uId>/delete/', templatesview.userDelete, name='userdelete'),
    
    path('', templatesview.userPage, name='userpage'),
    
    path('users/add/', templatesview.userformPage, name='userformpage'),
    path('users/created/', templatesview.addUserFunctionality, name='usercreatefunction'),
    
    path('vehicles/', templatesview.vehiclePage, name='vehiclepage'),
    path('vehicles/import/form/', templatesview.vehicleformPage, name='vehicleformpage'),
    path('vehicles/import/creates/', templatesview.importFileFunction, name='importcsvdata'),
    path('vehicles/<str:vId>/delete/', templatesview.deleteData, name='deleteData'),
    
    path('logout/', templatesview.logout, name='logout'),
    
    path('api/searchingvehicledata', views.searchVehicle),    
    path('api/login/User', views.loginUser),    
]