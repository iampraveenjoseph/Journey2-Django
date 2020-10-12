from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.core.mail import send_mail,EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.utils.encoding import force_bytes,force_text,DjangoUnicodeDecodeError
from .token import generate_token
from django.urls import reverse
from django.core.mail import EmailMessage
from django.conf import settings
from django.http import HttpResponse
from .forms import SignupForm
from django.contrib.auth import login, authenticate
#from .utils import token_generator 
# Create your views here.
def register(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        mail=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        
        if password1==password2:
            if User.objects.filter(username=username).exists():
                userexist="User name taken.Please try another Username"
                return render(request,'register.html',{'mes':userexist})
            elif User.objects.filter(email=mail).exists():
               emailexist="Email is already exist.Please try another email"
               return render(request,'register.html',{'mes':emailexist})
            
            else:    
                user = User.objects.create_user(username=username,password=password1,email=mail,first_name=first_name,last_name=last_name,is_active=False)
                Domain = get_current_site(request).domain
                #uidb64=urlsafe_base64_encode(force_bytes(user.pk))
                '''form=SignupForm(request.POST)
                if form.is_valid():
                    user = form.save(commit=False)
                    user.is_active = False
                    user.save()'''

                
                    #link=reverse('activate',{'uid64':uid64,'token':generate_token.make_token(user)}
                    #ur ='http://'+domain+link
                tem = render_to_string("success_reg.html",{
                        'domain': Domain,
                        'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                        'token':generate_token.make_token(user),'name' : first_name})
                user.set_password(password2)
                
                email = EmailMessage(
                        'Activate Your Account',
                        tem,
                        settings.EMAIL_HOST_USER,
                        [mail],
                        
                    )
                
                email.send(fail_silently = False)
                msg='Please confirm your email address to complete the registration'
                return render(request,"completion.html",{'msg': msg})
                #user.save()
                
                #else:
                    #print(form.is_valid)
                    
                    #return render(request, 'login.html' )

              
        else:
            passmismatch="Password Mismatch.Please try again"
            return render(request,'register.html',{'mes':passmismatch})
    
    return render(request,'register.html')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            message='Invalid details.Please check Your details'
            return render(request,'login.html',{'msg':message})
    return render(request,'login.html')   
def logout(request):
    auth.logout(request)
    return redirect('/')
def home(request):
    return redirect('/')
def contact(request):
    return render(request,"contact.html")
def activate(request,uidb64,token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and generate_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request)
        Domain = get_current_site(request).domain
        # return redirect('home')
        msg='Thank you for your email confirmation. Now you can login your account.'
        return render(request,'returnHome.html',{'msg':msg,'domain':Domain})
        
    else:
        return HttpResponse('Activation link is invalid!')
    return redirect('login')

    
