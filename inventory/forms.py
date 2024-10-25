from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'price', 'quantity', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'cols': 40}),  # Customize the description field
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']