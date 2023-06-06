from django.shortcuts import render
from .models import profile

# Create your views here.
def home(request):
    if request.method == 'POST':
        first_name=request.POST.get('fname')
        last_name=request.POST.get('lname')
        Email=request.POST.get('Email')
        phone_number=request.POST.get('phone')
        Qualification=request.POST.get('qualify')
        address=request.POST.get('address')
        en=profile(first_name=first_name,last_name=last_name,Email=Email,phone_number=phone_number,Qualification=Qualification,address=address)
        en.save()

    return render(request,'home.html')

def getuser(request):
    
    alluser=profile.objects.all()
    if request.method =='GET':
        st=request.GET.get('searchname')
        if st!=None:
            alluser=profile.objects.filter(first_name=st)
    context={'profiles':alluser}
    return render(request,'get user.html',context)

