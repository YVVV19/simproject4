from django.shortcuts import render, redirect

from django.shortcuts import render
from django.http import HttpResponse

from .models import ProductImage, Product
from .forms import ProductForm

# Lazarchuk
def index(request):
    return render(request, 'shop/home.html')

def add_product(request):
    if request.method == 'POST':
        if "add" in request.POST:
            form = ProductForm(request.POST)
            if form.is_valid():
                product_instance = form.save()
                for img in request.FILES.getlist('product_images'):
                    ProductImage.objects.create(product=product_instance, image_file=img)
                return render(request, 'Shop/add_product.html', {
                    "form": ProductForm(),
                    "success": True
                })
    else:
        form = ProductForm()
    return render(request, 'Shop/add_product.html', {"form": form})

def edit_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == "POST":
        if "edit" in request.POST:
            form = ProductForm(request.POST, instance=product)
            if form.is_valid():
                form.save()
                for img in request.FILES.getlist("image_file[]"):
                    ProductImage.objects.create(product=product, image_file=img)
            return render(request, 'Shop/edit_product.html', {"form": form, "success": True})
        elif "delet" in request.POST:
            product.delete()
            return redirect('/')
    else:
        form = ProductForm(instance=product)
        return render(request, 'Shop/edit_product.html', {"form": form})
# ---
