from django.shortcuts import render,redirect
from .models import*
from .forms import*
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.

@login_required(login_url='login')
def profile(request):
    return render(request,'user/profile.html')



def user_login(request):
    if request.method == 'POST':
        form = UyeGirisForm(request , data =  request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(username = username , password = password)
            if user is not None:
                login(request,user)
                next_url = request.GET.get('next',None)
                messages.success(request,'You Logged In Successfully!')
                if next_url is None:
                    return redirect('index')
            else:
                return redirect(next_url)
                    
    form = UyeGirisForm()
    return render(request,'user/login.html',{'form':form})



def user_logout(request):
    logout(request)
    return redirect('login')



def user_register(request):
    if request.method == "POST":
        form = UyeKayıt(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request,'user/register.html',{'form':form})
        
    form = UyeKayıt()
    return render(request,'user/register.html',{'form':form})

@login_required(login_url='login/')
def change_password(request):
    if request.method == "POST":
        form = sifreDegistir(request.user,request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            return redirect('index')
        else:
            return render(request,'user/changepassword.html',{'form':form})
    form = sifreDegistir(request.user)
    return render(request,'user/changepassword.html',{'form':form})

