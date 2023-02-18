from django.shortcuts import HttpResponse, render


def fun(request):
    return render(request,"home.html",{'name':'student'})
def add(request):
    num1=int(request.POST['num1'])
    num2=int(request.POST['num2'])
    num3=num1+num2
    return render(request,"result.html",{"add":num3})