from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from .models import *
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.shortcuts import HttpResponse
from django.contrib import messages
from django.contrib import messages as re
from django.contrib import messages as red
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from store.models import Product, Customer

# Create your views here.
from django.utils import translation

from .forms import ImageUpdate
from .models import UserProfile



@login_required(login_url='/chef/login') # Check login
def index(request):
    try:
        UserProfile.objects.get(user=request.user)
        current_user = request.user  # Access User Session information
        profile = UserProfile.objects.get(user=request.user)
        if profile is None:
            return HttpResponseRedirect('/')
        if request.method == 'POST':
            profile_form = ImageUpdate(request.POST, request.FILES, instance=request.user.userprofile)
            if profile_form.is_valid():
                profile_form.save()
                messages.success(request, 'Your image has been updated!')
                return HttpResponseRedirect('/chef')
        else:

            pro = ('yoghurt', 'shawarma', 'cake', 'pop-corn', 'toppings', 'smoothie', 'grill', 'bread','drink')
            Image_Update = ImageUpdate(instance=request.user.userprofile) #"userprofile" model -> OneToOneField relatinon with user
            context = {

                'image_update': Image_Update,'profile':profile,'pro':pro,
            }
    except:
        return HttpResponseRedirect('/')

    return render(request,'user_profile.html',context)


def login_form(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        try:
            if user is not None and UserProfile.objects.get(user=user) is not None:
                login(request, user)
                return HttpResponseRedirect('/chef')
            else:
                messages.warning(request,"Login Error !! Username or Password is incorrect")
                return HttpResponseRedirect('')
        except:
            if user is None:
                messages.warning(request, "Login Error !! Username or Password is incorrect")
                return HttpResponseRedirect('')
            messages.warning(request, "Sorry you do not have access to this page")
            return HttpResponseRedirect('')
    # Return an 'invalid login' error message.
    #category = Category.objects.all()
    context = {
     }
    return render(request, 'login_form.html',context)

def logout_vendor(request):
    logout(request)
    return redirect('/chef/login')

@login_required(login_url='/chef/login')
def update_image(request):
    current_user = request.user  # Access User Session information

    profile = UserProfile.objects.get(user_id=current_user.id)
    if request.method == 'POST' and UserProfile.objects.get(user=request.user) is not None:
        profile_form = ImageUpdate(request.POST, request.FILES, instance=request.user.userprofile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your image has been updated!')
            return HttpResponseRedirect('/chef')
    else:
        Image_Update = ImageUpdate(instance=request.user.userprofile) #"userprofile" model -> OneToOneField relatinon with user
        context = {

            'image_update': Image_Update,'profile':profile,
        }

    return render(request, 'user_product.html',context)

@login_required(login_url='/chef/login')
def update_product(request,id,name):
    current_user = request.user  # Access User Session information
    profile = UserProfile.objects.get(user=request.user)
    if request.method == 'POST' and UserProfile.objects.get(user=request.user) is not None:
        data = Product.objects.get(id=id)
        data.name = request.POST["food_name"]
        data.category = request.POST["food_category"]
        data.price = request.POST["price"]
        data.time = request.POST["time"]
        data.desc = request.POST["food_description"]
        data.ip = request.META.get('REMOTE_ADDR')
        data.image = request.FILES["myfile"]
        current_user = request.user
        data.user_id = current_user.id
        data.status = False
        data.save()
        profile_form = ImageUpdate(request.POST, request.FILES, instance=request.user.userprofile)
        return HttpResponseRedirect('/chef/view_product/')
    else:
        update = Product.objects.get(user=request.user,id=id)
        pro = ('yoghurt','shawarma' ,'cake' ,'pop-corn', 'yoghurt', 'smothie' , 'grill','bread')
        Image_Update = ImageUpdate(instance=request.user.userprofile) #"userprofile" model -> OneToOneField relatinon with user
        context = {

            'image_update': Image_Update,'profile':profile,'update':update,'pro':pro,
        }

    return render(request, 'update_product.html',context)

@login_required(login_url='/chef/login')
def view_product(request):
    products = Product.objects.filter(user=request.user)

    context = {'products': products,}
    current_user = request.user  # Access User Session information
    profile = UserProfile.objects.get(user_id=current_user.id)
    if request.method == 'POST' and UserProfile.objects.get(user=request.user) is not None:
        profile_form = ImageUpdate(request.POST, request.FILES, instance=request.user.userprofile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your image has been updated!')
            return HttpResponseRedirect('/chef')
    else:
        Image_Update = ImageUpdate(instance=request.user.userprofile)  # "userprofile" model -> OneToOneField relatinon with user
        context = {

            'image_update': Image_Update, 'profile': profile,'products': products,
        }
    return render(request, 'user_product.html',context)


def signup_form(request):
    if request.user.is_authenticated:
        logout(request)
    if request.method == 'POST' and request.user.is_authenticated == False:
        username = request.POST["username"]
        password = request.POST["password"]
        confirmpassword = request.POST["confirm_password"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        phone_number = request.POST["phone_number"]
        address = request.POST["address"]

        # if any of the fields are blank - restart registration with message
        for val in [username, password, first_name, last_name, email,address, phone_number]:
            if val == '':
                messages.info(request, 'pls fill all the information')
                return redirect('signuped')
            elif User.objects.filter(username__iexact=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signuped')
            elif User.objects.filter(email__iexact=email).exists():
                messages.info(request, 'Email already exist')
                return redirect('signuped')
            elif password != confirmpassword:
                messages.info(request, "your password does not match")
                return redirect('signuped')
            elif len(phone_number) < 11:
                messages.info(request, 'Your phone number is incorrect')
                return redirect('signuped')
            elif len(phone_number) > 12:
                messages.info(request, 'Your phone number is incorrect')
                return redirect('signuped')
            elif UserProfile.objects.filter(phone_number__iexact=phone_number).exists():
                messages.info(request, 'Phone number already exists, click on forget pass'
                                       'word if you can\'t remember your password')
                return redirect('signuped')
            elif len(password) < 5:
                messages.info(request, 'password must be at least 5')
                return redirect('signuped')
            else:
                use = User.objects.create_user(username=username, email=email, password=password, first_name=first_name,
                                               last_name=last_name)
                use.save();
                na = User.objects.get(username=username)
                cus = UserProfile.objects.create(user=na, email=email, username=username,first_name=first_name,
                                               last_name=last_name, image="images/users/user.png", phone_number=phone_number,address=address)
                cus.save();
                customer = Customer.objects.create(user=na, name=username, email=email, phone_number=phone_number)
                customer.save();
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Your profile has been created ')
                    return redirect('user_index')


    context = { }
    return render(request, 'register.html', context)

@login_required(login_url='/chef/login')
def add_product(request):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST' and request.user.is_authenticated and UserProfile.objects.get(user=request.user) is not None:
        food_name=request.POST["food_name"]
        category=request.POST["food_category"]
        price=request.POST["price"]
        time=request.POST["time"]
        desc=request.POST["food_description"]

        for val in[food_name,price,time,desc,category]:
            if val == '':
                re.success(request, "Pls fill out the required spaces")
                return HttpResponseRedirect(url)
            else:
                data = Product()
                profile=UserProfile.objects.get(user=request.user)
                data.name = request.POST["food_name"]
                data.category = request.POST["food_category"]
                data.price = request.POST["price"]
                data.time = request.POST["time"]
                data.desc = request.POST["food_description"]
                data.ip = request.META.get('REMOTE_ADDR')
                data.image = request.FILES["myfile"]
                data.profile_image = profile.image.url
                current_user = request.user
                data.user_id = current_user.id
                data.status = False
                data.save()
                messages.success(request, "Your food "+request.POST["food_name"]+" have been uploaded, it will start showing once its approved by the admin")
                return HttpResponseRedirect(url)

    return HttpResponseRedirect(url)


@login_required(login_url='/login') # Check login
def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user) # request.user is user  data
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been updated!')
            return HttpResponseRedirect('/user')
    else:
        profile = UserProfile.objects.get(user=request.user)
        user_profile = User.objects.get(username=profile.user)
         #"userprofile" model -> OneToOneField relatinon with user
        context = {
            'user_profile' :user_profile,
            'profile': profile,
        }
        return render(request, 'user_update.html', context)\

@login_required(login_url='/login') # Check login
def orders(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user) # request.user is user  data
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been updated!')
            return HttpResponseRedirect('/user')
    else:
        profile = UserProfile.objects.get(user=request.user)
        user_profile = User.objects.get(username=profile.user)
         #"userprofile" model -> OneToOneField relatinon with user
        context = {
            'user_profile' :user_profile,
            'profile': profile,
        }
        return render(request, 'data-table.html', context)


 

