from django.shortcuts import render,redirect
from .models import student

def displayindex(request):
    data = student.objects.all()
    context = {"data" : data}
    return render(request, "index.html", context)

def insertdata(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')

        query = student(name=name, email=email, number=number,)
        query.save()
        return redirect("/")
    return render(request, "index.html")


def index(request):
    data = student.objects.all()
    context = {data : data}
    return render(request,"index.html", context)

def deleteData(request, id):
    d = student.objects.get(id=id)
    d.delete()
    return redirect('/')
    return render(request, "index.html")


def updateData(request, id):
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')


        edit = student.objects.get(id=id)
        edit.name = name
        edit.email = email
        edit.number = number
        edit.save()
        return redirect("/")
    d = student.objects.get(id=id)
    context = {"d" : d}
    return render(request, "edit.html", context)
