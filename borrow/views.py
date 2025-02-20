from django.shortcuts import render,redirect,get_object_or_404
from .models import Product,Borrow
from django.contrib.auth.models import User
from users.models import Profile
from .forms import ProductListingCreateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    if request.user.is_authenticated:
        product_list = Product.objects.exclude(owner = request.user)
    else:
        product_list = Product.objects.all()
    return render(request,'borrow/index.html',{'product_list':product_list})

@login_required
def new_listing(request):
    if request.method == 'POST':
        listing_form = ProductListingCreateForm(data=request.POST,files=request.FILES)
        if listing_form.is_valid():
            new_listing = listing_form.save(commit=False)
            new_listing.owner = request.user
            new_listing.save()
            messages.success(request,'New Product Listing created successfully')
            return redirect('dashboard')
        else:
            messages.error(request, 'Form data invalid')    
    listing_form = ProductListingCreateForm()
    return render(request,'borrow/new_listing.html',{'listing_form':listing_form})

@login_required
def borrow_product(request,pk):
    product =get_object_or_404(Product,pk=pk)
    Borrow.objects.create(product=product,borrowed_by = request.user)
    #next a signal should be sent to owner to approve.
    messages.success(request,'Product Borrow request sent to owner for approval')
    return redirect('index')
   
@login_required
def approve_request(request,pk):
    product =get_object_or_404(Product,pk=pk)
    borrow_product = Borrow.objects.get(product=product,is_archived='False')
    borrow_product.approve_request()
    messages.success(request,'Product Borrow request Approved')
    return redirect('dashboard')

@login_required
def return_request(request,pk):
    product =get_object_or_404(Product,pk=pk)
    borrow_product = Borrow.objects.get(product=product,is_archived='False')
    borrow_product.return_request()
    messages.success(request,'Product Borrow request Approved')
    return redirect('dashboard')

def search(request):
    if request.method == 'POST':
        searchValue = request.POST.get('searchValue')
        product_list = Product.objects.filter(name__icontains=searchValue)
    return render(request,'borrow/index.html',{'product_list':product_list})
    
