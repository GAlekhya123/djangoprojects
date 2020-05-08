from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import StudentForm
from .models import Student
from django.contrib import messages

def hello(request):
    return HttpResponse('My app 2')


def register(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        form.save()
        messages.success(request,request.POST['stuName']+"" +'record stored Successfully')
        messages.info(request,"Now you can add record")
        return redirect(register)
    form = StudentForm()
    return render(request,'myApp2/register.html',{'form':form})


def display(request):
    data = Student.objects.all()
    # import pdb; pdb.set_trace()
    return render(request,'myApp2/displayStudent.html',{'data':data})
def edit(request,id):
    data = Student.objects.get(id=id)
    if request.method=='POST':
        form = StudentForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('/myapp2/details')
    form = StudentForm(instance=data)
    return render(request,'myApp2/edit.html',{'form':form,'data':data})

def delete(request,id):
    ob = Student.objects.get(id=id)
    if request.method == 'POST':
        ob.delete()
        return redirect('/myapp2/display')
    return render(request,'myApp2/msg.html',{'info':ob})
