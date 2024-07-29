from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def home(r):
    return render(r,'home.html')
def employlogin(r):
    if r.user.is_authenticated and not r.user.is_staff:
        return redirect('dashboard')
    message=" "
    if r.method =='POST':
        username=r.POST.get('emailid')
        password=r.POST.get('password')
        print(username,password)
        user=authenticate(r,username=username,password=password)
        print(user)
        if user is not None:
            print(user)
            login(r,user)
            return redirect('dashboard')
        else:
            message="Invalid Username or Password"

    return render(r,'index.html',{'message':message})
def empdash(r):
    if r.user.is_authenticated and not(r.user.is_staff):
        emp=r.user.employee
        return render(r,'dashboard.html',{'name':emp})
    else:
        return redirect('login')
    
def empregister(r):
    
        if r.method=='POST':
            form=empform(r.POST,r.FILES)
            if form.is_valid():
                emp=form.save(commit=False)
                emailid=form.cleaned_data['emailid']
                password=form.cleaned_data['password']
                user=User.objects.create_user(username=emailid,password=password)
                emp.user=user
                emp.save()
                return redirect('dashboard')
        else:
            form=empform()
            return render(r,'register.html',{'form':form})
   
def productview(r):
    forms=details.objects.all()
    print(forms)
    return render(r,'proview.html',{'form':forms})
    
@login_required(login_url='/login/')
def emplogout(r):
    logout(r)
    return redirect('login')


def productreg(r):
    if r.method=='POST':
        form=product(r.POST,r.FILES)
        if form.is_valid():
            print(form)
            form.save()
            return redirect('dashboard')
    else:
        form=product()
        return render(r,'proreg.html',{'form':form})
def productupdate(r,pk):
    Product=get_object_or_404(details,pk=pk)
    if r.method=='POST':
        form=product(r.POST,instance=Product)
        if form.is_valid():
            form.save()
            return redirect('proview')
    else:
        form=product(instance=Product)
        return render(r,'update.html',{'form':form})
def prodelete(r,pk):
    Product=get_object_or_404(details,pk=pk)
    if r.method=='POST':
        Product.delete()
        return redirect('proview')
    else:
        form=product(instance=Product)
        return render(r,'delete.html',{'form':form})

    
 


