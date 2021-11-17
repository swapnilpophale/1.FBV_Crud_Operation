from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeModelForm
def homeview(request):
    form = EmployeeModelForm() #blank
    if request.method == 'POST':
        form = EmployeeModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('retrieve')
    return render(request, 'home.html', {'form':form})


def retrieveview(request):
    data = Employee.objects.all()
    return render(request, 'data.html', {'data':data})

def updateview(request, oid):
    data = Employee.objects.get(id= oid)
    form = EmployeeModelForm(instance=data)
    if request.method == 'POST':
        form = EmployeeModelForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
        return redirect('retrieve')
    return render(request, 'home.html', {'form': form})

def deleteview(request, id):
    data = Employee.objects.get(id= id)
    data.delete()
    return redirect('retrieve')

