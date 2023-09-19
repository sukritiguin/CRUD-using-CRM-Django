from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm
from django.contrib.messages import success
from . models import Record

# Create your views here.
def HomePage(request):
    return render(request, 'webapp/index.html')

def RegisterPage(request):
    # form = CreateUserForm()
    
    # if request.method == 'POST':
    #     form = LoginForm(request.POST)
        
    #     if form.is_valid():
    #         form.save()
            
    #         messages.success(request, "Account created successfully!")
            
    #         return redirect('login')
    
    # context = {'form': form}
    
    # return render(request, 'webapp/register.html', context=context)
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in after registration
            login(request, user)
            success(request, "Account created successfully!")
            return redirect('dashboard')
    else:
        form = CreateUserForm()

    context = {'form': form}
    return render(request, 'webapp/register.html', context=context)


def LoginPage(request):
    form = LoginForm()
    
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                auth.login(request, user)
                
                return redirect('dashboard')
            
    context = {'form': form}
    
    return render(request, 'webapp/login.html', context=context)


def LogoutPage(request):
    auth.logout(request)
    
    return redirect('home')


@login_required(login_url='login')
def DashboardPage(request):
    
    records = Record.objects.all()
    
    context = {'records': records}
    
    return render(request, 'webapp/dashboard.html', context=context)


@login_required(login_url='login')
def CreateRecordPage(request):
    if request.method == 'POST':
        form = CreateRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CreateRecordForm()

    context = {'form': form}
    
    return render(request, 'webapp/create-record.html', context=context)


@login_required(login_url='login')
def UpdateRecordPage(request, pk):
    record = Record.objects.get(id=pk)
    form = UpdateRecordForm(instance=record)
    
    if request.method == 'POST':
        form = UpdateRecordForm(request.POST, instance=record)
        
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {'form': form}
    
    return render(request, 'webapp/update-record.html', context=context)