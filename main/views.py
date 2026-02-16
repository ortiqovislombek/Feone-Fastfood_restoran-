from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.db.models import Q

from .models import HeroSlider, Category, Product, Feedback, Order

def search(request: HttpRequest):
    word=request.GET.get('q')
    products=Product.objects.filter(Q(title__icontains=word) | Q(description__icontains=word), is_active=True)
    
    return render(request,"menu.html",{"products":products})

@login_required(login_url='/account/login/')
def home(request: HttpRequest):
    sliders = HeroSlider.objects.filter(published=True)
    categories = Category.objects.all()
    products = Product.objects.filter(is_active=True)
    discounted_products = Product.objects.filter(is_active=True, discount__gt=0)[:2]
    feedbacks = Feedback.objects.all()
    context = {
        "sliders": sliders,
        "categories": categories,
        "products": products,
        "discounted_products": discounted_products,
        "feedbacks": feedbacks,
    }

    return render(request, "index.html", context=context)

@login_required(login_url='/account/login/')
def menu(request: HttpRequest):
    categories = Category.objects.all()
    products = Product.objects.filter(is_active=True)
    context = {
        "categories": categories,
        "products": products,
    }

    return render(request, "menu.html", context=context)

@login_required(login_url='/account/login/')
def about(request: HttpRequest):

    return render(request, "about.html")

@login_required(login_url='/account/login/')
def book(request: HttpRequest):

    return render(request, "book.html")

@login_required(login_url='/account/login/')
def chekout(request: HttpRequest, pk: int):
    products = Product.objects.get(pk=pk)

    if request.method == "POST":

        full_name = request.POST.get("customer_name")
        phone = request.POST.get("customer_phone")
        address = request.POST.get("shipping_address")
        payment_method = request.POST.get("payment_method")
        quantity = request.POST.get("quantity")
        total_price = request.POST.get("total_price")

        if payment_method:
            Order.objects.create(
                user=request.user,
                product=products,
                full_name=full_name,
                phone=phone,
                address=address,
                payment_method=payment_method,
                quantity=int(quantity),
                total_price=float(total_price),
            )
        else:
            return render(
                request,
                "checkout.html",
                {"products": products, "error": "To‘lov usulini kiriting!"},
            )

        return redirect("menu")

    context = {
        "products": products,
    }
    return render(request, "checkout.html", context=context)

@login_required(login_url='/account/login/')
def orders(request: HttpRequest):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')


    context = {
        "orders": orders,
    }

    return render(request, "my_orders.html", context=context)
