from django.shortcuts import render, redirect
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
import logging

logger = logging.getLogger(__name__)
# models
from .models import *

# Create your views here.
    
# return the Json values
def getTheVehicleData(data):
    vehicalObject = {
        "account_no": data.account_no if data.account_no else '',
        "center": data.center if data.center else '',
        "chasis_number": data.chasis_number if data.chasis_number else '',
        "created_at": data.created_at if data.created_at else '',
        "customer_name": data.customer_name if data.customer_name else '',
        "engine_number": data.engine_number if data.engine_number else '',
        "executive": data.executive if data.executive else '',
        "id" : data.id,
        "new_vehicle_number": data.new_vehicle_number if data.new_vehicle_number else '',
        "product_name": data.product_name if data.product_name else '',
        "segment": data.segment if data.segment else '',
        # "updated_at": data.updated_at if data.updated_at else '',
    }
    return vehicalObject

@csrf_exempt
@api_view(['POST'])
def searchVehicle(request):
    try:
        data = request.data
        vehicle_number = data['search_key']
        dataList = []
        
        if not vehicle_number:
            return Response({"message": "Data searched","data": dataList},status=200)
        
        searchedData = Vehicledetails.objects.filter(new_vehicle_number__icontains=vehicle_number)
        
        for item in searchedData:
            v_details = getTheVehicleData(item)
            dataList.append(v_details)
        return Response({'message':"Data searched",'data': dataList},status=200)
    except KeyError as e:
        return Response({'message': "Invalid key in the request body."}, status=400)
    except Exception as e:
        logger.error(f"User Register Exception : {str(e)}")
        return Response({'message': str(e)}, status=500)
    
# Function for the 404 error 
def error_404(request, exception):
    return render(request, 'errors/err.html')

# Function for the 500 error 
def error_500(request, *args, **argv):
    return render(request,'errors/500.html')


# Return the Admin Page.
def index(request):
    return render(request,'adminpages/index.html')