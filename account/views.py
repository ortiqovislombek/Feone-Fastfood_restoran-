from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest,HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model  


from main.models import Product,Category,Order
User = get_user_model()


def login_view(request):
    error_login = None
    if request.method == "POST" and 'login_submit' in request.POST:
        username = request.POST.get('login_username')
        password = request.POST.get('login_password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            error_login = "Username yoki parol xato"
    context={
        'error_login': error_login, 
        'show_form': 'login'
    }
    return render(request, 'account/login.html', context=context)


def register_view(request):
    print(request.POST)
    error_register = None
    if request.method == "POST" and 'register_submit' in request.POST:
        username = request.POST.get('register_username')
        email = request.POST.get('register_email')
        password = request.POST.get('register_password')
        password2 = request.POST.get('register_password2')

        if password != password2:
            error_register = "Parollar mos emas"
        elif User.objects.filter(username=username).exists():
            error_register = "Username allaqachon mavjud"
        elif User.objects.filter(email=email).exists():
            error_register = "Email allaqachon mavjud"
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            login(request, user)
            return redirect('home')
    context={
        'error_register': error_register, 
        'show_form': 'register'
    }
    return render(request, 'account/login.html', context=context)



def logout_view(request):
    logout(request)
    return redirect('login')






@login_required()
def profile_view(request:HttpRequest):
    user=request.user
    if request.method == 'POST':
        user.first_name = request.POST.get('first_name')
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.phone = request.POST.get('phone')
        user.birth_date = request.POST.get('birth_date')
        user.gender = request.POST.get('gender')
        user.description = request.POST.get('description')
        
        user.save() 
        messages.success(request,"Muvofaqiyatli ozgartlildi!")
        return redirect('profil')
    context={
        'user':user
    }
    
    return render(request,'account/account.html',context=context)






@login_required()
def order_view(request:HttpRequest):
    orders=Order.objects.filter(user=request.user)
    
    
    context={
        'orders':orders,
    }
    return render(request,'account/my_orders.html',context=context)

@login_required()
def admin_view(request:HttpRequest):
    user=request.user
    products = Product.objects.all()
    
    context={
        'user':user,
        'products':products,
    }
    return render(request,'account/admin_page.html',context=context)







@login_required()
def security_view(request:HttpResponse):
    
    
    return render(request,'account/security.html') 
@login_required()
def create_product(request:HttpRequest):
    categorys=Category.objects.all()
    context={
        'categorys':categorys,
    }
    
    if request.method=='POST':
        category_name = request.POST.get('category')
        try:
            category_instance = Category.objects.get(title=category_name)  
        except Category.DoesNotExist:
            messages.error(request, f"Kategoriya '{category_name}' topilmadi!")
            return redirect('create_product')
        Product.objects.create(
            title=request.POST.get('title'),
            description=request.POST.get('desc'),
            image=request.FILES.get('image'),
            price=request.POST.get('price'),
            discount=request.POST.get('discount'),
            category=category_instance,
            is_active=True if request.POST.get('is_active') else False,
        )
    
        messages.success(request, "Mahsulot muvaffaqiyatli qo‘shildi ✅")
        return redirect('admin')
    
    return render(request,'account/create_form.html',context=context)



@login_required()
def edit_product(request:HttpRequest,pk:int):
    products=Product.objects.get(pk=pk)
    categorys=Category.objects.all()
    
    if request.method=='POST':
        
        category_id = request.POST.get('category')
        
        products.title=request.POST.get('title')
        products.description=request.POST.get('description')
        products.price=request.POST.get('price')
        products.discount=request.POST.get('discount')
        products.is_active = True if request.POST.get('is_active') == 'on' else False
        products.category = Category.objects.get(id=category_id)
        if request.FILES.get('image'):
            products.image = request.FILES.get('image')
            
        
        products.save()

        messages.success(request, "Mahsulot yangilandi")
        return redirect('admin')
        
    
    context={
        'categorys':categorys,
        'products':products,
    }
    
    
    
    return render(request,'account/edit_form.html',context=context)



@login_required()
def delete_product(request:HttpRequest,pk:int):
    products=Product.objects.get(pk=pk)
    
    if request.method == 'POST':
        products.delete()
        messages.success(request,'Muvofaqiyatli ochirildi')
        return redirect('admin')
        
    
   
    
    
    return render(request,'account/admin_page.html')