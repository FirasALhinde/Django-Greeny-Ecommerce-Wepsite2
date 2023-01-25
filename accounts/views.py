from django.shortcuts import render
from.forms import SignupForm
from.models import Profile
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.


def signup(request):
    '''
    form ----> data[submit]- ----> 
    create account [not active] --->
    [send activation code] [redirect: form [activation code]] ----->
    [active] - redict : profile
    '''

    if request.method == 'POST':
        form = SignupForm(request.POST)
       
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            myform = form.save(commit=False)
            myform.active = False
            myform.save()
            profile = Profile.objects.get(user__username=username)
            send_mail(
            'Activate your account',
            f'use this code to  activate your account',
            settings.EMAIL_HOST_USER,
            (email,),
            fail_silently=False,
            )   

    else:
        form = SignupForm()
    return render(request,'regesteration/signup.html',{'form':form})


def profile(request):
    pass

def edit_profile(request):
    pass