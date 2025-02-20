from django.shortcuts import render, redirect,HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import*
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages


# Create your views here.
def update(request):
   try:
       if request.method=='POST':
           authordata=Author.objects.get(name='a')
           authordata.name=request.POST['name']
           authordata.email=request.POST['email']
           authordata.save()
           return render(request,'update.html',{'author':authordata})
       else:
            authordata=Author.objects.get(name='a')
            return render(request,'update.html',{'author':authordata})
   except:
        return render(request,'update.html')     
        


def home(request):
   if 'email' in request.session:
      return render(request,'home.html',{'session':True})
   return render(request, 'home.html', {'session': False})   
 
def register(request):
    if request.method == 'POST':
        user=userregister()
        user.name=request.POST['name']
        user.email=request.POST['email']
        user.password=request.POST['password']
        useralready=userregister.objects.filter(email = request.POST['email'])
        if len(useralready)>0:
             return render(request,'signup.html',{'already':"This mail is already registerd"})
        else:
            user.save()
            return render(request,'signup.html',{'store':"Welcome !"})
    else:
        return render(request,'signup.html')

def login(request):
    if request.method == 'POST':
        try:
            useremail= userregister .objects.get(email = request.POST['email'])
            if useremail.password== request.POST['password']:
                request.session['email']=useremail.email
                print(useremail.name,useremail.password,"111111")
                print(request.session['email'])
                return redirect('home')
            else:
                return render(request,'login.html',{'pass':"password is incorrect!!"})
        except:
            return render(request,'login.html',{'reg':"Before login you have to register"})
    else:
       return render(request,'login.html')

def logout(request):
    del request.session['email']
    return redirect('home')

def request_pickup(request):
     return render(request,'request_pickup.html')

def recycle(request):
     return render(request,'recycle.html')

def collect(request):
     return render(request,'collect.html')

from django.shortcuts import render, get_object_or_404
from .models import Category, ScrapType

from django.shortcuts import render, get_object_or_404
from .models import Category, ScrapType

def category_list(request):
    categories = Category.objects.all()  # Fetch categories first
    
    if 'email' in request.session:
        return render(request, 'categories.html', {'session': True, 'categories': categories})
    
    return render(request, 'categories.html', {'categories': categories})



def scrap_list(request, category_id):
    category = get_object_or_404(Category, id=category_id)  # Get the category first
    scrap_types = ScrapType.objects.filter(category=category)  # Get scrap types for the category
    
    if 'email' in request.session:
        return render(request, 'buy1.html', {'session': True, 'category': category, 'scrap_types': scrap_types})
    
    return render(request, 'buy1.html', {'category': category, 'scrap_types': scrap_types})

from decimal import Decimal


def buy_scrap(request, scrap_id):
    scrap = get_object_or_404(ScrapType, id=scrap_id)  # Get the scrap type

    weight = request.GET.get('weight', 1)  # Get weight from request (default 1kg)
    
    try:
        weight = Decimal(weight)  # Convert weight to Decimal
    except:
        weight = Decimal(1)  # Default to 1 if conversion fails

    total_price = scrap.price_per_kg * weight  # Calculate total price

    return render(request, 'check.html', {
        'session': 'email' in request.session,  # Pass session status
        'scrap': scrap,
        'weight': weight,
        'total_price': total_price
    })


def about(request):
    if 'email' in request.session:
      return render(request,'about.html',{'session':True})
    return render(request,'about.html')

def contact(request):
    # if 'email' in request.session:
    #   return render(request,'contact.html',{'session':True})
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        Message=request.POST.get('Message')
        s=Contact(name=name,email=email,phone=phone,message=Message)
        s.save()
    return render(request,'contact.html')

def checkout(request):
    return render(request,'checkout.html')

def prof(request):
    if 'email' in request.session:
      userdetails=userregister.objects.get(email=request.session['email'])
      if request.method=='POST':
        userdetails.name=request.POST['name']
        userdetails.mob=request.POST['mob']
        userdetails.add=request.POST['add']
        userdetails.save()
        return render(request,'profile.html',{'user':userdetails,'session':True})
      else:
          return render(request,'profile.html',{'user':userdetails,'session':True})
    else:
        return redirect('login')
    
@login_required
def checkout(request):
    if request.method == "POST":
        print("Checkout POST request received")  # Debugging message

        user = request.user  # Ensure user is logged in
        scrap_type = request.POST.get("scrap_type")
        weight = request.POST.get("weight")
        total_price = request.POST.get("total_price")

        if not (scrap_type and weight and total_price):
            print("Missing form data")  # Debugging message
            return render(request, "checkout.html", {"error": "All fields are required"})

        print(f"User: {user}, Scrap Type: {scrap_type}, Weight: {weight}, Total Price: {total_price}")

        # Save the order
        order = Order.objects.create(
            user=user,
            scrap_type=scrap_type,
            weight=weight,
            total_price=total_price,
            status="Pending"
        )
        order.save()
        print("Order saved successfully!")  # Debugging message

        return redirect(request,"home")  # Redirect to success page

    return render(request, "checkout.html")



def order_success(request, order_id):
    return render(request, "order_success.html", {"order_id": order_id})


def request_pickup(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        status=request.POST.get("email")
        p=Pickup(name=name,phone=phone,address=address,status=status)
        p.save()
    return render(request, "request_pickup.html")

def compost(request):
    return render(request, "compost.html")