from django.shortcuts import render,redirect
from myApp.models import Emp
from django.http import HttpResponse

# Create your views here.

def signUp(request):
	if request.method=="POST":
		empid=request.POST['empid']
		empName=request.POST['empName']
		empDesig=request.POST['empDesig']
		salary=request.POST['salary']

		obj=Emp(empid=empid,empName=empName,empDesig=empDesig,salary=salary)

		obj.save()
		return redirect('/showAll')
		#return HttpResponse('Done success')



		#here we will read data which is coming from user
	return render(request,"myApp/signup.html",{})

def showAll(request):
	data=Emp.objects.all()
	return render(request,"myApp/showAll.html",{'data':data})
