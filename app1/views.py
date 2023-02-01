
from multiprocessing import context
import re
from unicodedata import name
from django.shortcuts import redirect, render, HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def dashboard(request):
    medi_count =Medicine.objects.filter(userz=request.user).count()
    recipts_count= Bill.objects.filter(userz=request.user).count()
    empl_count = Employee.objects.filter(userz=request.user).count()
    suppl_count = Company.objects.filter(userz=request.user).count()

    context={'medi_count':medi_count,'recipts_count':recipts_count,'empl_count':empl_count,'suppl_count':suppl_count}
    return render(request, 'dashboard.html',context)



# |--------Companies--------|
@login_required
def suppliers(request):
    suppl = Company.objects.filter(userz=request.user)
    if request.method=='POST':
        userz = request.user
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        contact =request.POST.get('contact')
        address =request.POST.get('address')
        added_on =request.POST.get('added_on')
        suppliers=Company(name=name,desc=desc,address=address,added_on=added_on,contact=contact,userz=request.user)
        suppliers.save()
    context={'suppl':suppl}
    return render(request, 'supplier.html', context)
def com_delete(request, event_id):
    event = Company.objects.get(id=event_id)
    event.delete()
    return redirect('suppl')

# |--------MEdicine--------|
@login_required
def medicine(request):
    medi = Medicine.objects.filter(userz=request.user)
    if request.method=='POST':
        name= request.POST.get('name')
        company_id= request.POST.get('company_id')
        company=Company.objects.get(id=company_id)
        desc= request.POST.get('desc')
        sell_price= request.POST.get('sell_price')
        buy_price= request.POST.get('buy_price')
        in_stock= request.POST.get('in_stock')
        added_on= request.POST.get('added_on')
        shelf_no= request.POST.get('shelf_no')
        medicine= Medicine(name=name, desc=desc, userz=request.user, company_id=company, sell_price=sell_price, buy_price=buy_price, in_stock=in_stock,added_on=added_on,shelf_no=shelf_no )
        medicine.save()
    context = {'medi':medi,'company_id':Company.objects.filter(userz=request.user)}
    return render(request, 'medicine.html',context)

def mad_delete(request, event_id):
    event = Medicine.objects.get(id=event_id)
    event.delete()
    return redirect('medicines')
    # |--------Employees--------|
@login_required
def employee(request):
    empl = Employee.objects.filter(userz=request.user)
    if request.method=='POST':
        name=request.POST.get('name')
        contact=request.POST.get('contact')
        address=request.POST.get('address')
        salary=request.POST.get('salary')
        joining_date=request.POST.get('joining_date')
        employee=Employee(name=name,contact=contact,address=address,salary=salary,joining_date=joining_date,userz=request.user)
        employee.save()
    context={'empl':empl}
    return render(request,'employees.html',context)

@login_required
def recipt(request):
    recipts= Bill.objects.filter(userz=request.user)
    if request.method=='POST':
        medicine_id = request.POST.get('medicine_id')
        medicine = Medicine.objects.get(id=medicine_id)
        qty =request.POST.get('qty')
        added_on=request.POST.get('added_on')
        recipt = Bill(medicine_id=medicine,qty=qty,added_on=added_on,userz=request.user)
        recipt.save()
    context={'medicine_id':Medicine.objects.filter(userz=request.user), 'recipts':recipts}
    return render(request,'bill.html', context)

# !------ Auth Views ------!

def signup(request):
    if request.method=='POST':
            username= request.POST['username']
            email= request.POST['email']
            password= request.POST['password']

            myuser = User.objects.create_user(username,email,password)
            myuser.save()
            return redirect('signin')
    return render(request,'sign-up.html')

def signin(request):
    if request.method=="POST":
            username= request.POST['username']
            password= request.POST['password']

            user=authenticate(username=username,password=password)
       
            if user is not None:
                login(request,user)
                messages.success(request,"Successfully Logged In")
                return redirect('dashboard')
            else:
                messages.error(request, "invalid Credentials Please try again!")
                return redirect('signin')

    return render(request,'sign-in.html')

def handlelogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('signin')
    
def search(request):
    query = request.GET['query']
    allsearch = Medicine.objects.filter(name__icontains=query)
    context={'allsearch':allsearch}
    return render(request,'',context)

