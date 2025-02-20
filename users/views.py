from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib import messages
from .forms import UserLoginForm,RegisterUserForm,EditUserForm,EditProfileForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from borrow.models import Product,Borrow

# Create your views here.
def user_login(request):
    if request.method == 'POST':
        user_login_form = UserLoginForm(request.POST)
        if user_login_form.is_valid():
            data = user_login_form.cleaned_data
            login_user = authenticate(request,username=data['username'],password=data['password'])
            if login_user is not None:
                login(request,login_user)
                return redirect('dashboard')
            else:
                return HttpResponse('Not a valid user')
        else:
            print(user_login_form.errors.as_data())
            print(user_login_form.errors)
            return HttpResponse('Form Data not valid')
        
    else:
        user_login_form = UserLoginForm()
        return render(request,'users/login.html',{'user_login_form':user_login_form})

@login_required(login_url='user_login')
def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('dashboard')
    else:
        return render(request,'users/logout.html',{})
    
@login_required(login_url='user_login')
def dashboard(request):
    my_products = Product.objects.filter(owner = request.user)
    my_borrows = Borrow.objects.filter(borrowed_by = request.user,is_approved='True',is_archived='False')
    my_approvals = Borrow.objects.filter(is_approved='False',is_archived='False',product__owner = request.user)
    return render(request,'users/dashboard.html',{'my_products':my_products,'my_borrows':my_borrows,'my_approvals':my_approvals})

def register_user(request):
    user_form = RegisterUserForm(request.POST or None)
    if request.method == 'POST':
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            password = user_form.check_password()
            new_user.set_password(password)
            new_user.save()
            apartment_number = user_form.cleaned_data.get('apartment_number')
            phone_number = user_form.cleaned_data.get('phone_number')
            apartment_name =user_form.cleaned_data.get('apartment_name')
            user_profile = Profile(user=new_user,apartment_name=apartment_name,apartment_number=apartment_number,phone_number=phone_number)
            # add other details
            user_profile.save()
            messages.success(request, 'You have signed up successfully.')
            return redirect('user_login')
        else:
            print(user_form.errors)
            return HttpResponse('Form Data not valid')
    else:
        return render(request,'users/register.html',{'user_form':user_form})

@login_required() 
def edit_user(request):
    if request.method == 'POST':
        user_form = EditUserForm(instance=request.user, data=request.POST)
        user_profile = Profile.objects.get(user=request.user)
        profile_form = EditProfileForm(instance=user_profile, data=request.POST,files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'User data updated successfully')
            return redirect('dashboard')
        else:
            print(user_form.errors)
            print(profile_form.errors)
            return HttpResponse('Form Data not valid')
    else:
        user_form = EditUserForm(instance=request.user)
        profile_form = EditProfileForm(instance=request.user.userprofile)

        return render(request,'users/edit_user.html',{'user_form':user_form,'profile_form':profile_form})
