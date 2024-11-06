from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from inventory.forms import ProductForm, CategoryForm
from inventory.models import Product, Category
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm

class CustomLoginView(LoginView):
    template_name = 'login.html'  # Path to your template
    authentication_form = AuthenticationForm  # Use Django's built-in AuthenticationForm

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_details.html', {'product': product})

@login_required
def add_product(request):
    """View to handle adding a new product."""
    if request.method == 'POST':
        form = ProductForm(request.POST)  # Instantiate the form with POST data
        if form.is_valid():  # Check if the form is valid
            form.save()  # Save the new product to the database
            return redirect('product_list')  # Redirect to the product list page
    else:
        form = ProductForm()  # Display an empty form for GET requests

    return render(request, 'add_product.html', {'form': form})

@login_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect('product_list')

@login_required
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


def product_list_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)

    return render(request, 'product_list.html', {
        'category': category,
        'products': products,
    })

