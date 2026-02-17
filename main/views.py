from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.db.models import Q
import stripe
from config import settings

from .models import HeroSlider, Category, Product, Feedback, Order




@login_required(login_url='/account/login/')
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
            order=Order.objects.create(
                user=request.user,
                product=products,
                full_name=full_name,
                phone=phone,
                address=address,
                payment_method=payment_method,
                quantity=int(quantity),
                total_price=float(total_price),
            )
            if payment_method == "card":
                return redirect("payment", order_id=order.id)
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




@login_required(login_url='/account/login/')
def payment(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    domain_url = "http://127.0.0.1:8000"

    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],  
            line_items=[
                {
                    "price_data": {
                        "currency": "usd",
                        "product_data": {
                            "name": order.product.title,
                        },
                        "unit_amount": int(order.product.price * 100),
  
                    },
                    "quantity": order.quantity,
                }
            ],
            mode="payment",
            success_url=domain_url + f"/payment/success/{order.id}/",
            cancel_url=domain_url + f"/payment/cancel/{order.id}/",
        )
        return redirect(checkout_session.url)
    except Exception as e:
        return HttpResponse(str(e))

@login_required(login_url='/account/login/')
def payment_success(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    order.status = "yetkazildi"
    order.save()
    return render(request, 'payment_success.html', {"order": order})

@login_required(login_url='/account/login/')
def payment_cancel(request, order_id):
    return render(request, 'payment_cancel.html')