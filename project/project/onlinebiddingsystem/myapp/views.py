from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render, redirect
from .forms import CreateUserForm, UserCreationForm,BidForm
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Product,Bid,All,Daily,Offer
from django.db.models import Q
from django.contrib.auth import authenticate , login as log_in ,logout

def registerpage(request):
    if request.user.is_authenticated:
        return redirect('main')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data['username']
                messages.success(request ,'Account Created for' +"   " + user)
                return redirect('login')

        context = {'form':form}
        return render(request,"register.html",context)


def loginpage(request):
    if request.user.is_authenticated:
        return redirect('main')
    else:

        if request.method=='POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request,username=username,password=password)
            if user is not None:

                log_in(request,user)
                if request.user.is_authenticated:
                   messages.success(request, f' wecome {username} !!')
                return redirect('main')
            else:
                    messages.warning(request ,'USERNAME OR PASSWORD IS INCORRECT')
        context = {}
        return render(request,"login.html",context)


def logoutUser(request):
    logout(request)
    messages.success(request ,'Logged Out Successfully')
    return redirect('login')



def mainpage(request):
    product = Product.objects.all()[:3]
    daily = Daily.objects.all()[:3]
    dict ={
        'product': product,
        'daily': daily
    }

    return render(request, "main.html", dict)

def auctionpage(request):
    products = Product.objects.all()
    return render(request, "auctions.html", {'product': products})

def dailyauctionpage(request):
    daily = Daily.objects.all()
    return render(request,"dailyauctions.html",{'daily': daily})

def winnerpage(request):
    return render(request,"winner.html")


def testimonialspage(request):
    return render(request,"testimonials.html")


def indexpage(request):
    return render(request,"index.html")

def offerpage(request):
    offer = Offer.objects.all()
    return render(request,"offers.html",{'offer': offer})

def bidpage(request, id):
    if request.method == 'POST':
        form = BidForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data['username']
            messages.success(request ,'Account Created for' +"   " + user)
            return redirect('main')
    else:
        form = BidForm()
    product = Product.objects.get(id=id)
    return render(request,"bid.html", {'product': product})


def dailybidpage(request, id):
    daily = Daily.objects.get(id=id)
    product = Product.objects.get(id=id)
    dict = {
        'daily' : daily,
        'product' : product,
    }
    form = BidForm()
    if request.method == 'POST':
        form = BidForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data['username']
            messages.success(request ,'Account Created for' +"   " + user)
            return redirect('main')
            
    return render(request,"dailybid.html",dict)

def profile(request, id , username):
    user = User.objects.get(id=id)
    bid = Bid.objects.filter(username= username)
    print(username)
    print(Bid.username)
    dict = {
        'user' : user,
        'bid' : bid,
    }
    return render(request, 'profile.html', dict)

def update(request, id ):
    bid = Bid.objects.get(id=id)
    form = BidForm(request.POST, instance = bid)
    if form.is_valid():
        form.save()
        return redirect("main")
    return render(request,'update.html', {'bid': bid})


def updatepro(request, id ):
    user = User.objects.get(id=id)
    form = UserCreationForm(request.POST, instance = user)
    if form.is_valid():
        form.save()
        return redirect("main")
    return render(request,'profileedit.html', {'user': user})

def destroy(request, id):
    bid = Bid.objects.get(id=id)
    bid.delete()
    return redirect("main")
