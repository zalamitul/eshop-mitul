from django.shortcuts import render,redirect
from .models.product import Product
from django.contrib.auth.hashers import check_password,make_password
from .models.category import Category
from .models.order import Order
from .models.customer import Customer
from store.middleware.middleware import auth_middleware
from django.http import HttpResponse


def cart(req):
    categories = Category.get_all_categories()
    data={}
    data1 = []
    print("dsada")
    try:
        arr = dict(req.session.get('cart'))
        for i in arr.keys():
            products= Product.objects.get(pk=int(i))
            data1.append(products)
        total = 0
        for i in req.session.get('cart'):
            for j in data1:
                if int(i) == j.id:
                    total = total + j.price * arr[i]
        data['products'] = data1
        data['total'] = total
        data['categories'] = categories
        print("hhhh")
    except:
        arr=[]
        data['value']="disabled"
        try:
            data['customer'] = req.session['customer']
        except:
            data['customer'] = None
    print(data['products'])
    return render(req,'cart.html',data)

def logout(req):
    req.session.clear()
    return redirect('homepageq')

def login(req):
    error='incorrect password'
    if req.method=='GET':
        return render(req,'login.html')
    else:
        url=req.GET.get('returnUrl')
        if not url:
            ulr=None
        email=req.POST.get('email')
        password=req.POST.get('password')
        try:
            damy=Customer.get_password(email)
            if check_password(password,damy.password):
                req.session['customerid'] = damy.id
                req.session['customer'] = email
                if url:
                    return redirect(url)
                elif url=='/order/':
                    return redirect(url)
                return redirect('homepageq')
            else:
                return render(req,'login.html',{ 'error':error})
        except:
            return render(req,'login.html',{ 'error':'User does not exist'})


def index(req):
    if req.method=='GET':
        categories = Category.get_all_categories()
        category = req.GET.get('category', 'all')
        products = Product.get_products(category)
        data = {}
        data['products']=products
        data['categories']=categories
        try:
            data['customer']=req.session['customer']
        except:
            data['customer']=None
        return render(req, 'index.html', data)
    elif req.method=='POST':
        categories = Category.get_all_categories()
        products = Product.get_products('all')
        data = {}
        # print(req.GET.get('categoriy'))
        data['products']=products
        # print(products)
        data['categories']=categories
        cart=req.session.get('cart')
        # print('ASDsd',cart)
        value = req.POST.get('productId')
        remove = req.POST.get('remove')
        if cart:
            q = req.session.get('cart').get(value)
            if q:
                if remove:
                    if q==1:
                        cart.pop(value)
                    else:
                        cart[value] = q - 1
                else:
                    cart[value] = q + 1
            else:
                cart[value] = 1
        else:
            cart={}
            cart[value]=1
        req.session['cart']=cart
        data['cart']=dict(cart)
        return render(req, 'index.html', data)
    else:
        return HttpResponse("h")

def order(req):
    customer=req.session.get('customerid')
    data={}
    data['orders'] = Order.objects.filter(customer= customer)
    print(data)
    x=0
    for item in data['orders']:
        x=x+item.price
    data['total']=x
    print(data['total'])
    return render(req,'order.html',data)

def check_out(req):
    phone=req.POST.get("phone")
    customer=req.session.get('customerid')
    address= req.POST.get("address")
    print(phone," hello ",address,"",customer)
    cart=req.session.get('cart')
    print(cart)
    print(cart.get('9'))
    products=Product.get_products_byid(cart.keys())
    print(products)
    for product in products:
        print(cart.get(str(product.id)),product.price)
        order = Order(product=product,customer=Customer(id=customer),quantity=cart.get(str(product.id)),price=int(product.price)*int(cart.get(str(product.id))),image=product.image,phone=phone,address=address)
        order.save()
    req.session['cart']={}
    return redirect('order')

def homepage(req):
    categories = Category.get_all_categories()
    category = req.GET.get('category', 'all')
    products = Product.get_products(category)
    data = {}
    data['products']=products
    data['categories']=categories
    data['customer']=req.session.get('customer')
    return render(req,'homepage.html',data)

def signup(req):
    if req.method=='GET':
        return render(req, 'signup.html')
    elif req.method=='POST':
        error_msg = None
        data = Customer(fname=req.POST.get('fname'), lname=req.POST.get('lname'), password=req.POST.get('password'),
                        email=req.POST.get('email'), phone=req.POST.get('phone'))
        if data.fname=='':
            error_msg="name is required"
        elif data.lname=='':
            error_msg = "last name is required"
        elif data.phone =='':
            error_msg='phone number is recuired'
        elif len(data.phone)<10 :
            error_msg='enter correct phoone number'
        else:

            flag = Customer.check_email(data.email)
            if flag:
                error_msg="email alredy exsist"
            else:
                print(flag)
        if not error_msg:
            data.password=make_password(data.password)
            data.save()
            return redirect(req,'homepage')
        else:
            data1={}
            data1['data']=data
            data1['error']=error_msg
            return render(req,'signup.html',data1)
    else:
        return HttpResponse("sorry")

def profile(req):
    return HttpResponse("hadh")