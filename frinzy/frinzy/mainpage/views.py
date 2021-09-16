from django.shortcuts import render
from .models import Courses

# Create your views here.

dat = {"title" : "Crinzy","image":None,'content':'Crinzy provides Free Courses'}
def test(request):
    course = Courses.objects.filter(popular = True)[::-1]

    return render(request,'resources/testtemp.html',{'course' : course,"data":dat})


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
    return render(request,'resources/test2.html',{'course' : course,"data":dat})


def policy(request):
    return render(request,'resources/policy.html',{"data":dat})

def terms(request):
    return render(request,'resources/terms.html',{"data":dat})

def blog(request,i):
    course = Courses.objects.get(pk = i)
    dat = {"title" : course.title,"image": course.image.url,"content":course.description}

    return render(request,'resources/blog.html',{'course' : course,"data":dat})