from django import forms 
from .models import * 
  
  
# creating a form 
class SalesDataForm(forms.ModelForm):
    # create meta class 
    class Meta: 
        # specify model to be used 
        model = SalesData
        # specify fields to be used 
        fields = [ 
            'invoice', 
            'stockcode', 
            'description', 
            'quantity', 
            'invoicedate', 
            'price', 
            'customerid'
        ] 