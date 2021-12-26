from django.shortcuts import render
from .models import Login
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def login(request):
    if request.method=='POST':
        name = request.POST['name']
        lastname = request.POST['lastname']
        email = request.POST['email']
        birthdate = request.POST['birthdate']
        phonenumber = request.POST['phonenumber']
        height = request.POST['height']
        weight = request.POST['weight']
        branch = request.POST['branch']
        login=Login(name=name,lastname=lastname,email=email,birthdate=birthdate,phonenumber=phonenumber,height=height,weight=weight,branch=branch)
        login.save()
        
    
    subject = 'Registertion Complete'
    message = f'Hi{Login.name} thank you for registering in our gym.yours time shedule on'
    email_from = settings.EMAIL_HOST_USER
    reply_to = ['pradeepnarale35@gmail.com']
    send_mail( subject, message, email_from, reply_to )
    return render(request,"login.html")

