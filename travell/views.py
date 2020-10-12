from django.shortcuts import render,redirect
from . models import Destination
from. models import Place , Feedback
from django.core.mail import EmailMessage
from django.conf import settings
from django.http import HttpResponse
import psycopg2
from django.template.loader import render_to_string
# Create your views here.
def index(request):
    dests = Destination.objects.all()
    return render(request,'index.html',{'dests':dests})
def home(request):
    return render(request,'index.html')
def contact(request):
    return render(request,"contact.html")
def find_destination(request):
    if request.method=='GET':
        city=request.GET["city"]
        city=city.capitalize()
        #budget=request.GET["budget"]
        
        dests=Destination.objects.all().filter(name=city)
       
        return render(request,'search.html',{'destination':dests,'city':city})
def feedback(request):

    if request.method=='POST':
        name=request.POST['name']
        mail=request.POST['mail']
        subject=request.POST['subject']
        message=request.POST['message']
        #connection= psycopg2.connect()
        
        data=Feedback(name=name,mail=mail,subject=subject,feedback=message)
        data.save()
        
        email = EmailMessage(
                    'Thank You For Your feedback',
                    "Our Executive will contact soon.Thank you for your time.Have Great Day",
                    settings.EMAIL_HOST_USER,
                    [mail],
                    
                )
            
        email.send(fail_silently = False)
        return redirect('contact')
