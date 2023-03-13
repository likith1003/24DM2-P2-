from django.shortcuts import render
from home.models import Register
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'index.html')
def register(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        pno=request.POST.get('pno')
        email=request.POST.get('email')
        gender=request.POST.get('gender')
        address=request.POST.get('loc')
        username=request.POST.get('username')
        password1=request.POST.get('pass1')
        password2=request.POST.get('pass2')
        existing_users=Register.objects.all()
        if password1!=password2:
            messages.info(request,'Password dosent matched')
            return render(request,'register.html')
        x=True
        for i in existing_users:
            if i.username==username:
                x=False
        if x==True:
            register=Register(name=fname,pno=pno,email=email,address=address,gender=gender,username=username,password=password1)
            register.save()
            return render(request,'login.html')
        else:
            messages.info(request,'User Exists')
            return render(request,'register.html')
    else:
        return render(request,'register.html')
def login(request):
    if request.method=='POST':
        username=request.POST.get('uname')
        password=request.POST.get('pass')
        users=Register.objects.all()
        for i in users:
            if i.username==username and i.password==password:
                return render (request,'user.html',{'username':i.username})
    return render(request,'login.html')