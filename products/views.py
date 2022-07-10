from tkinter import Message
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
# from compfest import products

# Create your views here.
from . models import Product
from .forms import ProductForm

def home(request):
    return render(request, "authentication/index.html")

def index(request):
    products = Product.objects.all()
    
    context = {
        'products': products,
    }
    return render(request, 'index.html', context)


def productDetail(request, pk):
    eachProduct = Product.objects.get(id = pk)
    context = {
        'eachProduct': eachProduct,
    }
    return render(request, 'productDetail.html', context)

def addProduct(request):
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm()

    context = {
        "form":form
    }

    return render(request, 'addProduct.html', context)

def deleteProduct(request, id):
    product = Product.objects.get(id=id)
    price = request.GET.get("price")
    print(price)
    product.delete()
    return redirect('home')



