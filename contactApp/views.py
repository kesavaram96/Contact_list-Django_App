from django.shortcuts import redirect, render
from .models import Contact
# Create your views here.
def index(request):
    context=Contact.objects.all()
    
    search_input=request.GET.get('search-area')
    if search_input:
        context=Contact.objects.filter(full_name__icontains=search_input)
    else:
        context=Contact.objects.all()
    return render(request,'index.html',{'context':context})

def add(request):
    
    if request.method=='POST':
        new_contact=Contact(
        full_name=request.POST['fullname'],
        relationship=request.POST['relationship'],
        phone_number=request.POST['phone_number'],
        email=request.POST['e_mail'],
        address=request.POST['address'],
        
        )
        new_contact.save()
        return redirect('index')
    
    return render(request,'add.html',)

def edit(request,pk):
    context=Contact.objects.get(id=pk)
    if request.method=='POST':
        context.full_name=request.POST['fullname']
        context.relationship=request.POST['relationship']
        context.phone_number=request.POST['phone_number']
        context.email=request.POST['email']
        context.address=request.POST['address']
        context.save()
        
        
        return redirect('/')
    return render(request,'edit.html',{'context':context})

def delete(request,pk):
    cont=Contact.objects.get(id=pk)
    if request.method=='POST':
        cont.delete()
        return redirect('/')
    return render(request,'delete.html',{'cont':cont})

def profile(request,pk):
    context=Contact.objects.get(id=pk)
    
    return render(request,'contact-profile.html',{'context':context})