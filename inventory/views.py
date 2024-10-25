from django.shortcuts import render, get_object_or_404, redirect

from inventory.forms import ProductForm, CategoryForm
from inventory.models import Product, Category


# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_details.html', {'product': product})

def add_product(request):
    """View to handle adding a new product."""
    if request.method == 'POST':
        form = ProductForm(request.POST)  # Instantiate the form with POST data
        if form.is_valid():  # Check if the form is valid
            form.save()  # Save the new product to the database
            return redirect('product_list')  # Redirect to the product list page
    else:
        form = ProductForm()  # Display an empty form for GET requests

    return render(request, 'product_edit.html', {'form': form})

# views.py
def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')  # Redirect to category list after saving
    else:
        form = CategoryForm()
    return render(request, 'add_category.html', {'form': form})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})
