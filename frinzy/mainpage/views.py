from django.shortcuts import render
from .models import Courses

# Create your views here.


def test(request):
    course = Courses.objects.filter(popular = True)[::-1]
    t = len(course)
    return render(request,'resources/testtemp.html',{'course' : course})


def moretest(request,tin):
    n = len(Courses.objects.all())
    con = Courses.objects.all()[::-1]
    p = int(n/3)
    if tin ==1:

        course = con[:p+1]
    if tin ==2:
        course = con[p+1:p*2+1]

    if tin ==3:
        course = con[p*2+1:]    
    return render(request,'resources/test2.html',{'course' : course})    


def policy(request):
    return render(request,'resources/policy.html')

def terms(request):
    return render(request,'resources/terms.html')

def blog(request,i):
    course = Courses.objects.get(pk = i)

    return render(request,'resources/blog.html',{'course' : course})