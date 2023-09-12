
from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from . models import *
from django.contrib import messages

# Create your views here.
def home(request):
    # return HttpResponse('Hello world')
    if 'email' in request.session:
        user=Register.objects.filter(email=request.session['email']).first()
        request.session['name']=user.name
    else:
        user=''
    data={'title':'home | MyShop','user':user}
    return render(request,'index.html',data)
def about(request):
    data={'title':'about | MyShop'}
    return render(request,'about.html',data)
def contact(request):
    data={'title':'contact | MyShop'}
    return render(request,'contact.html',data)
def kidboy(request):
    kidboys = KidBoys.objects.all()
    data={'title':'kidboy | MyShop','kidboys':kidboys}
    return render(request,'kidboys.html',data)
def kidgawn(request):
    kidgawn=KidGawn.objects.all()
    data={'title':'kidgawn | MyShop','kidgawn':kidgawn}
    return render(request,'kidgawn.html',data)
def kidgirlsummer(request):
    kidsummer=KidSummer.objects.all()
    data={'title':'kidgirlsummer | MyShop','kidsummer':kidsummer}
    return render(request,'kidgirlsummer.html',data)
def menjeans(request):
    menjeans = MenJeans.objects.all()
    data={'title':'menjeans | MyShop','menjeans':menjeans}
    return render(request,'menjeans.html',data)
def menshirt(request):
    menshirt = MenShirt.objects.all()
    data={'title':'menshirt | MyShop','menshirt':menshirt}
    return render(request,'menshirt.html',data)
def mentshirt(request):
    mentshirt =MenTShirt.objects.all()
    data={'title':'mentshirt | MyShop','mentshirt':mentshirt}
    return render(request,'mentshirt.html',data)
def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        phoneno = request.POST['phoneno']
        email = request.POST['email']
        password = request.POST['password']
        cpassword=request.POST['cpassword']
        if password==cpassword:
            checkemail=Register.objects.filter(email=email).first()
            if checkemail is not None:
                return HttpResponse('This email id already exits')
            else:
                data=Register.objects.create(name=name,phoneno=phoneno,email=email,password=password)
                messages.add_message(request,messages.SUCCESS,'Register successful')
                return redirect('home')
        else:
            return  HttpResponse('Password Not Match with Confirm Password')
    data={'title':'signup | MyShop'}
    return render(request,'signup.html',data)
def womenjeans(request):
    womenjeans = WomenJeans.objects.all()
    data={'title':'womenjeans | MyShop','womenjeans':womenjeans}
    return render(request,'womenjeans.html',data)
def womenkurti(request):
    womenkurti = WomenKurti.objects.all()
    data={'title':'womenkurti | MyShop','womenkurti':womenkurti}
    return render(request,'womenkurti.html',data)
def womentop(request):
    womentop = WomenTop.objects.all()
    data={'title':'womentop | MyShop','womentop':womentop}
    return render(request,'womentop.html',data)
def regis(request):
    li=Register.objects.all()
    #li=Register.objects.filter(status=1)
    return render(request,'table.html',{'data':li})
def edit_user(request,id):
    user=Register.objects.get(id=id)
    data={'title':'update | MyShop','user':user}
    return render(request,'Edit.html',data)
def delete_user(request,id):
    user=Register.objects.get(id=id)
    #user.delete()
    user.status=0
    user.save()
    return redirect('regis')
def retrive_user(request,id):
    user=Register.objects.get(id=id)
    #user.delete()
    user.status=1
    user.save()
    return redirect('regis')
def update(request):
    if request.method=="POST":
        name=request.POST['name']
        phoneno = request.POST['phoneno']
        email = request.POST['email']
        password = request.POST['password']
        id=request.POST['edit_id']
        user=Register.objects.get(id=id)
        user.name=name
        user.phoneno=phoneno
        user.email=email
        user.password=password
        user.save()
    return redirect('regis')
def loginpage(request):
    data={'title':'loginpage | MyShop'}
    return render(request,'loginpage.html',data)
def loginsuccess(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        users=Register.objects.filter(email=email ,password=password).first()
        if users is not None:
            request.session['email']=email
            messages.add_message(request,messages.SUCCESS,'Login successful')
            return redirect('home')
        else:
            messages.add_message(request,messages.ERROR,'Try Again')
            return redirect('loginpage')
def logout(request):
    del request.session['email']  
    messages.add_message(request,messages.SUCCESS,'Logout successful')
    return redirect('home')

def cart(request):
    if 'email' in request.session:
        user = Register.objects.filter(email=request.session['email']).first()
        if user:
            cart_items = CartItem.objects.filter(user=user)
            total_price = sum(item.product.offerp * item.quantity for item in cart_items)
            # cart_items = CartItem.objects.all()
        data={'title':'cart | MyShop','cart_items': cart_items,'total_price':total_price}
    else:
        data = {'title':'cart | MyShop'}
    return render(request, 'cart.html',data)

def add_to_cart(request, product_type, product_id):
    product = None
    if product_type == 'menshirt':
        product = get_object_or_404(MenShirt, id=product_id)
    elif product_type == 'mentshirt':
        product = get_object_or_404(MenTShirt, id=product_id)
    elif product_type == 'menjeans':
        product = get_object_or_404(MenJeans, id=product_id)
    elif product_type == 'womenjeans':
        product = get_object_or_404(WomenJeans, id=product_id)
    elif product_type == 'womenkurti':
        product = get_object_or_404(WomenKurti, id=product_id)
    elif product_type == 'womentop':
        product = get_object_or_404(WomenTop, id=product_id)
    elif product_type == 'kidboys':
        product = get_object_or_404(KidBoys, id=product_id) 
    elif product_type == 'kidgawn':
        product = get_object_or_404(KidGawn, id=product_id)
    elif product_type == 'kidsummer':
        product = get_object_or_404(KidSummer, id=product_id)
    if product and 'email' in request.session:
        user = Register.objects.filter(email=request.session['email']).first()
        if user:
            cart_item, created = CartItem.objects.get_or_create(user=user, product=product)
            messages.add_message(request,messages.SUCCESS,'Added to Cart')
            if not created:
                cart_item.quantity += 1
                cart_item.save()
    return redirect('home')

def qty_less(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    # cart_item.delete()
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')

def qty_up(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    # cart_item.delete()
    if cart_item.quantity >= 1:
        cart_item.quantity += 1
        cart_item.save()
    # else:
    #     cart_item.delete()
    return redirect('cart')

def del_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart_item.delete()
    messages.add_message(request,messages.SUCCESS,'Deleted Successfully')
    return redirect('cart')

def buy_now(request):
    if 'email' in request.session:
        user = Register.objects.filter(email=request.session['email']).first()
        if user:
            cart_items = CartItem.objects.filter(user=user)
            total_price = sum(item.product.price * item.quantity for item in cart_items)
            if cart_items:
                order = Order.objects.create(user=user, total_price=total_price)
                for cart_item in cart_items:
                    OrderedItem.objects.create(user=user,order=order, product=cart_item.product)
                cart_items.delete()
                messages.add_message(request,messages.SUCCESS,'Successfully Ordered')
    return redirect('order_history')

def order_history(request):
    if 'email' in request.session:
        user = Register.objects.filter(email=request.session['email']).first()
        if user:
            orders = Order.objects.filter(user=user).order_by('-created_at')
            return render(request, 'order.html', {'orders': orders})
    return redirect('home')