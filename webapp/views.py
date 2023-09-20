from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm
from django.contrib.messages import success
from . models import Record

from django.contrib import messages

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
            messages.success(request, "Account created successfully!")
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
                
                messages.success(request, 'Login successful')
                
                return redirect('dashboard')
            
    context = {'form': form}
    
    return render(request, 'webapp/login.html', context=context)


def LogoutPage(request):
    auth.logout(request)
    
    messages.success(request, 'Logout successful')
    
    return redirect('home')


@login_required(login_url='login')
def DashboardPage(request):
    
    records = Record.objects.filter(user=request.user)
    
    context = {'records': records}
    
    return render(request, 'webapp/dashboard.html', context=context)


@login_required(login_url='login')
def CreateRecordPage(request):
    if request.method == 'POST':
        form = CreateRecordForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.user = request.user
            record.save()
            messages.success(request, 'Create record successfully')
            return redirect('dashboard')
    else:
        form = CreateRecordForm()

    context = {'form': form}
    
    return render(request, 'webapp/create-record.html', context=context)


@login_required(login_url='login')
def UpdateRecordPage(request, pk):
    record = Record.objects.get(id=pk)
    # form = UpdateRecordForm(instance=record)
    
    # if request.method == 'POST':
    #     form = UpdateRecordForm(request.POST, instance=record)
        
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request, 'Record updated successfully')
    #         return redirect('dashboard')
    # context = {'form': form}
    
    # return render(request, 'webapp/update-record.html', context=context)

    # Get the record by its primary key
    record = Record.objects.get(id=pk)
    
    # Check if the record belongs to the currently logged-in user
    if record.user == request.user:
        form = UpdateRecordForm(instance=record)
        
        if request.method == 'POST':
            form = UpdateRecordForm(request.POST, instance=record)
            
            if form.is_valid():
                form.save()
                messages.success(request, 'Record updated successfully')
                return redirect('dashboard')
    else:
        # Handle the case where the user is trying to update a record that doesn't belong to them
        messages.error(request, "You don't have permission to update this record.")
        return redirect('dashboard')

    context = {'form': form}
    
    return render(request, 'webapp/update-record.html', context=context)


@login_required(login_url='login')
def ViewRecordPage(request, pk):
    # Get the record by its primary key
    record = Record.objects.get(id=pk)
    
    # Check if the record belongs to the currently logged-in user
    if record.user == request.user:
        context = {'record': record}
        
        return render(request, 'webapp/view-record.html', context=context)
    else:
        # Handle the case where the user is trying to view a record that doesn't belong to them
        messages.error(request, "You don't have permission to view this record.")
        return redirect('dashboard')


@login_required(login_url='login')
def DeleteRecordPage(request, pk):
    # record = Record.objects.get(id=pk)
    # record.delete()
    # messages.warning(request, 'Record deleted successfully')
    # return redirect('dashboard')
    
    
    # Get the record by its primary key
    record = Record.objects.get(id=pk)

    # Check if the record belongs to the currently logged-in user
    if record.user == request.user:
        record.delete()
        messages.success(request, 'Record deleted successfully')
        return redirect('dashboard')
    else:
        # Handle the case where the user is trying to delete a record that doesn't belong to them
        messages.error(request, "You don't have permission to delete this record.")
        return redirect('dashboard')