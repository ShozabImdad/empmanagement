from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Emp

# Create your views here.
def emp_home(request):
    
    emps = Emp.objects.all()
    #return HttpResponse('Student Home Page')
    return render(request, "emp/home.html", {'emps':emps})

def add_emp(request):
    if request.method == "POST":
        
        #fetch the data
        emp_name = request.POST.get("emp_name")
        emp_id = request.POST.get("emp_id")
        emp_phone = request.POST.get("emp_phone")
        emp_address = request.POST.get("emp_address")
        emp_working = request.POST.get("emp_working")
        emp_department = request.POST.get("emp_department")
        
        #create model object and set the data
        emp = Emp()
        emp.name = emp_name
        emp.emp_id = emp_id
        emp.phone = emp_phone
        emp.address = emp_address
        emp.working = emp_working
        emp.department = emp_department
        if emp.working is None:
            emp.working = False
        else:
            emp.working = True
        
        #save the object
        emp.save()
        
        #prepare message if you want
        print("Data is Coming")
        return redirect('/emp/home')
    return render(request, 'emp/add-emp.html', {})