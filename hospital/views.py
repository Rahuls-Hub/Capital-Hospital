from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, logout, login




# Create your views here.

def About(request):
    return render(request,'about.html')

def About_Us(request):
    return render(request,'about_us.html')

def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    return render(request,'index.html')

def Login(request):
    error=""
    if request.method=='POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u,password=p)
        try:
            if user.is_staff:
                login(request,user)
                error="no"
            else:
                error="yes"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'login.html',d)

def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')

def View_Doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Doctor.objects.all()
    d = {'doc':doc}
    return render(request, 'view_doctor.html', d)

def Add_Doctor(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    if request.method=='POST':
        n = request.POST['name']
        c = request.POST['contact']
        sp = request.POST['special']
        try:
            Doctor.objects.create(name=n, mobile=c,special=sp)
            error="no"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'add_doctor.html',d)

def Delete_Doctor(request,pid):
   if not request.user.is_staff:
       return redirect('login')
   doctor = Doctor.objects.get(id=pid)
   doctor.delete()
   return redirect('view_doctor')

def View_Patient(request):
    if not request.user.is_staff:
        return redirect('login')
    pat = Patient.objects.all()
    d = {'pat':pat}
    return render(request,'view_patient.html',d)

def Add_Patient(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':

        n = request.POST['name']
        m = request.POST['mobile']
        a = request.POST['address']


        try:
            Patient.objects.create(name=n,mobile=m,address=a)

            error="no"
        except:
            error="yes"

    d = {'error':error}
    return render(request,'add_patient.html',d)

def Delete_Patient(request,pid):
   if not request.user.is_staff:
       return redirect('login')
   patient = Patient.objects.get(id=pid)
   patient.delete()
   return redirect('view_patient')

def View_Appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    appoint = Appointment.objects.all()
    d = {'appoint':appoint}
    return render(request,'view_appointment.html',d)

def Add_Appointment(request):
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
        patient = Patient.objects.filter(name=c).first()
        try:
            Appointment.objects.create(doctor=doctor,patient=patient,date1=sp,time1=t)
            error="no"
        except Exception as e:
            print(e)
            error="yes"
    d = {'doctor':doctor1,'patient':patient1,'error':error}
    return render(request,'add_appointment.html',d)

def Delete_Appointment(request,pid):
   if not request.user.is_staff:
       return redirect('login')
   appointment = Appointment.objects.get(id=pid)
   appointment.delete()
   return redirect('view_appointment')


