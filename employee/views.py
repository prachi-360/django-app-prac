from django.http import HttpResponse
from django.shortcuts import render
from .models import Employee
# from e_gift_gallery import employee
# from e_gift_gallery import employee


def addEmployee(request):
    emp = Employee(ename='abc',eage=25,eemail='abc@gmail.com',econtact='7896785674')
    emp.save
    return HttpResponse('Employee Added...')

def viewEmployee(request):
    employees = Employee.objects.all().values_list()
    print(employees)
    return render(request,'employee/view.html',{'employees':employees})

def deleteEmployee(request):
    emp = Employee.objects.get(id =1)
    emp.delete()
    return HttpResponse("Employee Deleted...")

def updateEmployee(request):
    emp = Employee.objects.get(id =2)
    emp.eage = 30
    emp.econtact = 1456789876
    emp.save()
    return HttpResponse("Employee Updated...")