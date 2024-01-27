from django.contrib.auth.hashers import make_password,check_password
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import pandas as pd

def loginPage(request):
    if 'userId' in request.session:
        return redirect('userpage')
    return render(request, 'adminpages/Login.html')

def userPage(request):
    if 'userId' in request.session:
        userList = User.objects.exclude(id=request.session['userId'])
        context = {
            "currentPage": "user",
            "userdata" : userList 
        }
        return render(request, 'adminpages/userPage.html',context)
    return redirect('loginpage')

def userformPage(request):
    if 'userId' in request.session:
        context = {
            "currentPage": "user",
        }
        return render(request, 'adminpages/userform.html',context)
    return redirect('loginpage')

def vehiclePage(request):
    if 'userId' in request.session:
        vehicleList = Vehicledetails.objects.all() 
        context = {
            "currentPage": "vehicle",
            "vehiclesdata" : vehicleList 
        }
        return render(request, 'adminpages/vehiclePage.html',context)
    return redirect('loginpage')

def vehicleformPage(request):
    if 'userId' in request.session:
        context = {
            "currentPage": "vehicle",
        }
        return render(request, 'adminpages/vehicleform.html',context)
    return redirect('loginpage')
    
def loginUser(request):
    try: 
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        checkUser = User.objects.filter(username=username,)

        if checkUser.exists():
            user_data = checkUser.first()
        else:
            messages.error(request,"User not exists")
            return redirect('loginpage')

        if check_password(password, user_data.password):
            request.session['userId'] = user_data.id
            request.session['userName'] = user_data.name
            return redirect('userpage')
        elif  password ==  user_data.password:
            user_data.password = make_password(password)
            user_data.save()
            request.session['userId'] = user_data.id
            request.session['userName'] = user_data.name
            return redirect('userpage')
        else:
            messages.error(request,"password doesn't match")
            return redirect('loginpage')
    except:
        messages.error(request, f"something is wrong.")
        return('loginpage')

def userDelete(request,uId):
    if 'userId' in request.session:
        try:
            checkUser = User.objects.get(id=uId)
            checkUser.delete()
            messages.success(request, f"User deleted.")
            return redirect('userpage')
        except:
            messages.error(request, f"something is wrong.")
            return redirect('userpage')
    return('loginpage')


def addUserFunctionality(request):
    if 'userId' in request.session:
        fullname = request.POST.get('fullname','')
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        userList = User.objects.filter(username=username)
        if userList.exists():
            messages.error(request, f"User Already exists.")
            return redirect("userformpage")
        userList = User.objects.create(
            name = fullname, 
            username = username,         
            password = make_password(password),         
        )
        messages.success(request, f"User added successfully.")
        return redirect("userpage")
    return('loginpage')


def importFileFunction(request):
    csv_file = request.FILES.get('csv_file','')
    
    df = pd.read_excel(csv_file)
    
    for index, row in df.iterrows():
        account_no = row['ACCOUNT NO']
        customer_name = row['CUSTOMER NAME']
        center = row['CENTRE']
        executive = row['EXECUTIVE']
        segment = row['SEGMENT']
        product_name = row['PRODUCT NAME']
        new_vehicle_number = row['NEW VEHICLE NUMBER']
        engine_number = row['ENGINE NUMBER']
        chasis_num = row['CHASIS NUMBER']
        
        oldvalue = Vehicledetails.objects.filter(
            new_vehicle_number = new_vehicle_number,
            engine_number = engine_number,
            chasis_number = chasis_num
        )
        
        if not oldvalue.exists():
            newData = Vehicledetails.objects.create(
                customer_name = customer_name,
                account_no = account_no,
                center = center,
                executive = executive,
                segment = segment,
                product_name = product_name,
                new_vehicle_number = new_vehicle_number,
                engine_number = engine_number,
                chasis_number = chasis_num
            )    
    messages.success(request, f"Data Imported successfully.")
    return redirect('vehicleformpage')
        

def logout(request):
    try:
        del request.session['userId']
        return redirect("loginpage")
    except:
        return redirect("loginpage")