from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Borrow

@receiver(post_save,sender=Borrow)
def notify_owner_on_borrow_request(sender,instance,created,**kwargs):
    if created:
        product = instance.product
        owner_email = product.owner.email
        borrower = instance.borrowed_by.username

        print( f"Hi  {product.owner.username}, \n\n"
                f"Your Product {product.name} has received a borrow request from {borrower}"
                f"Please log in to the application and approve the request from your Dashboard.\n\n"
                f"Thank you. \nBoroNest")
        
        """send_mail(
            subject = "New Borrow request for your Product",
            message=(
                f"Hi  {product.owner.username}, \n\n"
                f"Your Product {product.name} has received a borrow request from {borrower}"
                f"Please log in to the application and approve the request from your Dashboard.\n\n"
                f"Thank you. \nBoroNest"
            ),
            from_email="noreply@boronest.com",
            recipient_list=[owner_email],
        )"""

@receiver(post_save,sender=Borrow)
def notify_borrower_request_approved(sender,instance,created,**kwargs):
    if not created:
        if instance.is_approved and not instance.is_returned:
            product = instance.product
            borrower = instance.borrowed_by.username
            borrower_email =instance.borrowed_by.email
            print(
                    f"Hi  {borrower}, \n\n"
                    f"Your Borrow request for Product {product.name} has been approved"
                    f"Please collect the product from the {product.owner.username}.\n\n"
                    f"Thank you. \nBoroNest"
                )
            
            """send_mail(
                subject = "Borrow request for your Product is approved",
                message=(
                    f"Hi  {borrower}, \n\n"
                    f"Your Borrow request for Product {product.name} has been approved"
                    f"Please collect the product from the {product.owner.username}.\n\n"
                    f"Thank you. \nBoroNest"
                ),
                from_email="noreply@boronest.com",
                recipient_list=[borrower_email],
            )"""

@receiver(post_save,sender=Borrow)
def notify_product_returned(sender,instance,created,**kwargs):
    if not created:
        if instance.is_approved and instance.is_returned:
            product = instance.product
            owner_email = product.owner.email
            borrower = instance.borrowed_by.username

            print(
                    f"Hi  {product.owner.username}, \n\n"
                    f"Return request for your Product {product.name} has been submitted"
                    f"Please collect the product from the {borrower}.\n\n"
                    f"Thank you. \nBoroNest"
                )
            
            """send_mail(
                subject = "Return request for your Product is submitted",
                message=(
                    f"Hi  {product.owner.username}, \n\n"
                    f"Return request for your Product {product.name} has been submitted"
                    f"Please collect the product from the {borrower}.\n\n"
                    f"Thank you. \nBoroNest"
                ),
                from_email="noreply@boronest.com",
                recipient_list=[owner_email],
            )"""