from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login


# Create your views here.
from hospital.models import Doctor, Patient, Appointment1, register



def index1(request):
    return render(request, 'index1.html')


def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        if User.objects.filter(username=username).exists():
            messages.info(request, "Username already Exists!")


        else:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already Exists!")
            else:
                data = User.objects.create_user(username=username, password=password, email=email)
                data.save()
                messages.success(request, "User Created Successfully!")
                user = authenticate(username=username, password=password)
                auth_login(request, user)
                return redirect('/')
    return render(request, 'register.html', {'messages': messages})


def User_Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        auth_login(request, user)
        return redirect('add_appointment1/')
    return render(request, 'login1.html')

def View_Appointment1(request):
    if not request.user.is_staff:
        return redirect('login')
    appoint = Appointment1.objects.all()
    d = {'appoint':appoint}
    return render(request,'view_appointment1.html',d)

def Add_Appointment1(request):
    print('11')
    error=""
    if not request.user.is_staff:
        return redirect('login')
    doctor1 = Doctor.objects.all()
    patient1 = Patient.objects.all()
    if request.method=='POST':
        n = request.POST['doctor']
        c = request.POST['patient']
        sp = request.POST['date']
        t = request.POST['time']
        print (n,c,sp,t)
        doctor = Doctor.objects.filter(name=n).first()
        print(doctor.id)
        patient = Patient.objects.filter(name=c).first()
        try:
            Appointment1.objects.create(doctor=doctor,patient=patient,date1=sp,time1=t)
            error="no"
            print('hhh')
        except Exception as e:
            print(e)
            error="yes"
    d = {'doctor':doctor1,'patient':patient1,'error':error}
    return render(request,'add_appointment1.html',d)
