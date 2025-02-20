from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

class Product(models.Model):
    category_choices = {
        'BK':'Book',
        'EL':'Electronic',
        'TY':'Toys',
        'MISC':'Others',
    }

    name = models.CharField(max_length=100)
    picture = models.FileField(upload_to='borrow',default='borrow/images/default_pic.png')
    description = models.TextField()
    owner = models.ForeignKey(to=User,on_delete=models.CASCADE)
    is_listed = models.BooleanField(default=True)
    is_availabe = models.BooleanField(default=True)
    category = models.CharField(max_length=50,choices=category_choices,default="BK")
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Borrow(models.Model):
    product = models.ForeignKey(to=Product,related_name='borrowproduct',on_delete=models.CASCADE)
    borrowed_by = models.ForeignKey(to=User,related_name='borrowing_user',on_delete=models.CASCADE)
    request_date = models.DateField(auto_now_add=True)
    borrow_date = models.DateField(blank=True,null=True)
    return_date = models.DateField(blank=True,null=True)
    is_returned = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)

    def approve_request(self):
        self.is_approved = True
        self.borrow_date = now()
        self.product.is_availabe = False
        self.product.save()
        self.save()


    def return_request(self):
        self.is_returned = True
        self.is_archived = True
        self.return_date = now()
        self.product.is_availabe = True
        self.product.save()
        self.save()
    
    def __str__(self):
        return f"{self.borrowed_by.username} -> {self.product.name}"