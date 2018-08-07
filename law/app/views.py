# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Lawyer ,Issues ,Customer
from django.contrib.auth.models import User
from .forms import Lawyer_register ,CreateUser
# Create your views here.
def CreateAdmin(request):
    if request.method=='POST':
        form=CreateUser(request.POST)
        form2=Lawyer_register(request.POST)
        if form.is_valid() and form2.is_valid():
            form_=form2.save(commit=False)
            user1=form.save()
            l=Lawyer(user=user1 ,city=form_.city)
            l.save()
            ai=request.POST.getlist('issues')
            for a in ai:
                l.issues.add(Issues.objects.get(id=a))
                l.save()
            return render(request ,'app/index.html')
        else:
            err='please insert correct data'
            return render(request ,'app/signuplawyer.html',{'err':err,'form':form ,'form2':form2})
    else:
        form=CreateUser()
        form2=Lawyer_register()
        return render(request ,'app/signuplawyer.html',{'form':form ,'form2':form2})


def CreateCustomer(request):
    if request.method=='POST':
        form=CreateUser(request.POST)
        if form.is_valid() :
            user1=form.save()
            c=Customer(user=user1)
            c.save()
            return render(request ,'app/index.html')
        else:
            return render(request ,'app/signupuser.html',{'form':form})
    else:
        form=CreateUser()
        return render(request ,'app/signupuser.html',{'form':form})



def home(request):
    query=request.GET.get('q')
    query2=request.GET.get('issues')
    if query and query2:
        lawyer=Lawyer.objects.filter(city__cityname__contains=query)
        i=Issues.objects.get(issuesname=query2)
        lawyer=lawyer.filter(issues=i)
        return render(request ,'app/index.html',{'lawyer':lawyer})
    else:
        return render(request ,'app/index.html')
