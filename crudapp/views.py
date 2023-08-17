from django.shortcuts import render,redirect, HttpResponse
from crudapp.models import *
from django.contrib import messages
from django.core.paginator import Paginator
import os
# Create your views here.
def data_add(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone_no = request.POST['phone_no']
        address = request.POST['address']
        image = request.FILES.get('image')
        # validation 
        error = False
        if first_name == "":
            error = True
            messages.error(request,'First name is required')
        elif last_name == "":
            error = True
            messages.error(request,'Last name is required')
        elif email == "":
            error = True
            messages.error(request,'Email is required')
        elif phone_no =="":
            error = True
            messages.error(request,'Phone is required')
        elif address == "":
            error = True
            messages.error(request,'Address is required')
        elif image == "":
            error = True
            messages.error(request,'Image is required')
        
        if error == False:
            queryset = Entry.objects.create(first_name = first_name, last_name = last_name, email = email, phone_no = phone_no, address = address, image = image)
            if queryset:
                messages.success(request,'Data inserted successfully')
                return redirect('add')
        else:
            context ={
                'first_name':first_name,
                'last_name':last_name,
                'email':email,
                'phone_no':phone_no,
                'address':address
            }
            return render(request,'crudapp/add.html',context)

    return render(request,'crudapp/add.html')

def data_view(request):
    data = Entry.objects.all()
    paginator = Paginator(data, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'datas':page_obj}
    return render(request,'crudapp/view.html',context)

def data_update(request,id):
    queryset = Entry.objects.get(id = id)
    context = {'datas':queryset}
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone_no = request.POST['phone_no']
        address = request.POST['address']
        image = request.FILES.get('image')
        

        queryset.first_name = first_name 
        queryset.last_name = last_name
        queryset.email = email
        queryset.phone_no = phone_no
        queryset.address = address
        queryset.save()
        if image:
            os.remove(queryset.image.path)
            queryset.image = image
            queryset.save()
        messages.success(request,'Data updated successfully.')
        return redirect('view')
    return render(request,'crudapp/update.html',context)

def data_delete(request):
    del_id = request.POST['delete_id']
    data = Entry.objects.get(id = del_id)
    os.remove(data.image.path)
    data.delete()
    messages.success(request,'Data deleted successfully.')
    return redirect('view')
    