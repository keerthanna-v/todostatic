from django.shortcuts import render,redirect
from todoapp.models import todomodel
from todoapp.forms import todoform
from django.views.generic import UpdateView
from django.urls import reverse_lazy

# Create your views here.
def home(request):
    return render(request,'todoapp/home.html')

def viewtodo(request):
    form=todomodel.objects.all()
    return render(request,'todoapp/viewtodo.html',{'form':form})

def deletetodo(request,id):
    deleteid=todomodel.objects.get(id=id)
    deleteid.delete()
    return redirect('/')

def addtodo(request):
    form=todoform()
    if request.method=='POST':
        form=todoform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'todoapp/todomodel_form.html',{'form':form})

class UpdateView(UpdateView):
    model=todomodel
    success_url=reverse_lazy('index')
    fields = ('title','details','time')