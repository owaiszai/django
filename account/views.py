from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse
from courses.form import InstrucForm
from courses.models import Course , Video
# Create your views here.


def index(request):
    return render(request, 'account/index.html')
    #return HttpResponse('Testing')


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'account/register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('adminpage')
            elif user is not None and user.is_customer:
                login(request, user)
                return redirect('customer')
            elif user is not None and user.is_employee:
                login(request, user)
                return redirect('employee')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'account/login.html', {'form': form, 'msg': msg})


def admin(request):
    return render(request,'account/admin.html')


def customer(request):
    return render(request,'courses/my_courses.html')


def employee(request):
    form = InstrucForm()
    msg = None
    context={
          "form":InstrucForm(), 'msg': msg    
             }
               
    if request.method == "POST":
           
        if form.is_valid():
           name = request.POST.get("name")
           slug = request.POST.get("slug")
           description = request.POST.get("description")
           price = request.POST.get("price")
           discount = request.POST.get("discount") 
           active = request.POST.get("active")
           if active == 'on':
              active = 'True'
           else:
              active = 'False'
           thumbnail = request.POST.get("thumbnail") 
           
           resource =request.POST.get("resource")
           length = request.POST.get("length")
    
           title  = request.POST.get("title")
           serial_number = request.POST.get("serial_number")
           video_id = request.POST.get("video_id")
           is_preview = request.POST.get("is_preview")
           if is_preview == 'on':
              is_preview = 'True'
           else:
              is_preview = 'False'
           
           article_object=Course.objects.create(name=name,slug=slug,description=description,price=price,discount=discount,active=active,thumbnail=thumbnail,resource=resource,length=length)
           context['object'] =article_object
           context['created']=True
           
        else:
            msg = 'error validating form'  
    return render(request,'account/employee.html',context=context)
    
    
def signout(request ):
    logout(request)
    return redirect("home")