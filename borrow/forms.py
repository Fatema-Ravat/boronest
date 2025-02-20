from django.forms import ModelForm
from .models import Product


class ProductListingCreateForm(ModelForm):
    class Meta:
        model = Product
        fields = {'name','picture','description','category'}

