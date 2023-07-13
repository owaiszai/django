from courses.models import Course
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError



def home(request):
    
    courses = Course.objects.all()
    
    try:
       query= request.GET['query']
       courses = Course.objects.filter(name__icontains=query)
    except MultiValueDictKeyError:
         query = False
       
     
   
             
    
    return render(request,template_name="courses/home.html",context={"courses":courses})
    
    
    
