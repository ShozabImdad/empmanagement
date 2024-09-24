from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Emp, Testimonial
from .forms import Feedback
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required(login_url = '/admin/login')
def emp_home(request):
    
    emps = Emp.objects.all()
    #return HttpResponse('Student Home Page')
    return render(request, "emp/home.html", {'emps':emps})

@login_required(login_url = '/admin/login')
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

def delete_emp(request, emp_id):
    emp = Emp.objects.get(pk = emp_id)
    emp.delete()
    return redirect('/emp/home')


def update_emp(request, emp_id):
    emp = Emp.objects.get(pk = emp_id)
    return render(request, 'emp/update-emp.html', {'emp': emp})

def do_updation_in_emp(request, emp_id):
    if request.method == "POST":
        
        #fetch the data
        emp_name = request.POST.get("emp_name")
        emp_id_temp = request.POST.get("emp_id")
        emp_phone = request.POST.get("emp_phone")
        emp_address = request.POST.get("emp_address")
        emp_working = request.POST.get("emp_working")
        emp_department = request.POST.get("emp_department")
        
        #create model object and set the data
        e = Emp()
        e.name = emp_name
        e.emp_id = emp_id_temp
        e.phone = emp_phone
        e.address = emp_address
        e.working = emp_working
        e.department = emp_department
        if e.working is None:
            e.working = False
        else:
            e.working = True
        
        #save the object
        e.save()
        
        
    return redirect('/emp/home')


def testimonials(request):
    test = Testimonial.objects.all()
    return render(request, "emp/testimonials.html", {'test': test})

def feedback(request):
    if request == 'POST':
        form = Feedback()
        if form.is_valid():
            form.save()
            print("data saved")
        else:
            return render(request, "emp/feedback.html", {'form': form})
    else:
        form = Feedback()
    return render(request, "emp/feedback.html", {'form': form})