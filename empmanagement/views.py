from django.http import HttpResponse
from django.shortcuts import render
import datetime

def home(request):
    
    if request.method == 'POST':
        check = request.POST['check']
        print(check)
        
        
    date = datetime.datetime.now()
    isActive = True
    name = 'Root Pointers'
    list_of_skills = [
        'Artificial Intelligence',
        'Machine Learning',
        'Deep Learning',
        'Django'
    ]
    student = {
        'student_name': 'SHOZAB IMDAD',
        'institute': 'GCU Lahore',
        'city': 'Lahore',
    }
    
    data = {
        'date': date,
        'student':student,
        'name': name,
        'isActive': isActive,
        'list_of_skills': list_of_skills 
    }
    #return HttpResponse('<h1>Hello this is index page</h1>' + str(date))
    return render(request, "home.html", data)


def about(request):
    print('Test function is called from about!')
    #return HttpResponse('<h1>Hello this is about page</h1>')
    return render(request, 'about.html', {})


def services(request):
    print('Test function is called from services!')
    #return HttpResponse('<h1>Hello this is services page</h1>')
    return render(request, 'services.html', {})
