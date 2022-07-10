import imp
from django import forms
from . models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['image', 'name', 'price', 'description']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }
        # labels = {
        #     'name' : 'Enter Product Name:',
        #     'image': 'Select an Image: ',
        #     'price': 'Enter a price: ',
        #     'description': 'Enter a Description: ',
        # }