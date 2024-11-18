from django.shortcuts import render ,HttpResponse ,redirect
from django.contrib import messages
import bcrypt
from .models import User ,Pie 
from . import models
# Create your views here.
def home(request):


    return render(request,'index.html')


def regAcc(request):
    if request.method=="POST":
        errors=User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key,value in errors.items():
                messages.error(request,value)

            return redirect('/')

        else:
            models.addUser(request.POST)
            return redirect('/')

def confirmlogin(request):
    if request.method=="POST":
        email=User.objects.filter(email=request.POST['email']).first()

        if email:
            if bcrypt.checkpw(request.POST['password'].encode(),email.password.encode()):
                request.session['fname']=email.first_name
                request.session['id']=int(email.id)

                return redirect('/success')
            else:

                messages.error(request, "Invalid email or password")
                return redirect('/')

    return redirect('/')


def suclogin(request):
    context={
        "pies":models.getallpies_byID(request.session['id']),

    }

    return render(request,'dashboard.html',context)

def logout(request):
    request.session.flush()
    return redirect('/')


def addnewpie(request):
    if request.method=="POST":
        errors=Pie.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key,value in errors.items():
                messages.error(request,value)

            return redirect('/addnewpie')

        else:
            models.addpie(request.POST)
            return redirect('/success')
        


def editpieview(request,id):
    context={
        'pie':Pie.objects.get(id=id)
    }


    return render(request,'editpiepage.html',context)


def editpie(request):
    pid=request.POST
    models.editpie(pid)
    
    return redirect('/success')


def deletepie(request,id):
    models.deletepie(id)
    
    return redirect('/success')


def allpies(request):

    context={
        'pies':Pie.objects.all()
    }


    return render(request,'allpies.html',context)