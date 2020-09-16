from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http import  HttpResponseRedirect
import json
from django.core.paginator import Paginator
import datetime
from .models import *
from .utils import cookieCart, cartData, guestOrder
from django.contrib import messages
import random
from django.db.models import Q
from django.contrib import messages as re
from django.contrib.auth import authenticate, login,logout
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from chef.models import UserProfile
from django.core.files.storage import FileSystemStorage
import slug


def index(request):
	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	products = Product.objects.all().filter(available=True, popular="Yes")[:6]
	context = {'products': products, 'cartItems': cartItems}
	return render(request, 'store/index.html', context)


def search(request):
	query = request.GET.get('q')
	search=""
	if request.method == 'GET' and query is not None:
		search = Product.objects.filter(Q(name__icontains=query))
	else:
		search=""
	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	context = {'products': search, 'cartItems': cartItems}
	return render(request, 'store/search.html', context)


def category(request):
	query = request.GET.get('q')
	search=""
	if request.method == 'GET' and query is not None:
		search = Product.objects.filter(Q(name__icontains=query) | Q(category__icontains=query))
	else:
		search=""
	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	context = {'products': search, 'cartItems': cartItems}
	return render(request, 'store/search.html', context)

def price_filter(request):
	start = request.GET.get('from')
	to = request.GET.get('to')
	search=""
	if request.method == 'GET' and start is not None and to is not None:
		search = Product.objects.filter(Q(price__gte=start) & Q(price__lte=to))
	else:
		search=""
	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	context = {'products': search, 'cartItems': cartItems}
	return render(request, 'store/search.html', context)

def vendor(request,username):
	user = User.objects.get(username=username)
	products = Product.objects.filter(user=user)
	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	context = {'products': products, 'cartItems': cartItems}
	return render(request, 'store/search.html', context)

def top(request):

	return render(request, 'store/top.html')

def store(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	products = Product.objects.all()
	profile = UserProfile.objects.all()

	sh= Product.objects.all().filter(category='yoghurt')[0]
	sh2 = Product.objects.all().filter(category='shawarma')[0]
	sh3 = Product.objects.all().filter(category='cake')[0]
	sh4 = Product.objects.all().filter(category='grill')[0]
	sh5 = Product.objects.all().filter(category='pop-corn')[0]
	sh6 = Product.objects.all().filter(category='smothie')[0]
	sh7 = Product.objects.all().filter(category='grill')[0]
	sh8 = Product.objects.all().filter(category='bread' or 'drink')[0]


	context = {'products':products, 'cartItems':cartItems, 'sh':sh.price,'sh2':sh2.price,'sh3':sh3.price,
	'sh4':sh4.price,'sh5':sh5.price,'sh6':sh6.price,'sh7':sh7.price,'sh8':sh8.price,'profile':profile}
	return render(request, 'store/store.html', context)

def cart(request):
	location = Location.objects.all()
	products = Product.objects.all()
	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	if request.method == 'POST':
		state = request.POST['state']
		side = request.POST['side']
		info = request.POST['info']

		if request.POST['state']=="":
			messages.info(request, 'Pls enter the state')
			return redirect("cart")
		elif request.POST['side']=="":
			messages.info(request, 'Pls enter the state side in  '+state)
			return redirect("cart")
		elif request.POST['state']!="enugu":
			messages.info(request, 'We only deliver to enugu state')
			return redirect("cart")
		elif Location.objects.filter(state=state,sides=side).exists()==False:
			messages.info(request, 'Your side is not available in Enugu State, contact admin')
			return redirect("cart")
		else:
			costs=Location.objects.get(state=state,sides=side)
			delivery = {'state': state, 'side': side, 'cost': costs.price,'info':info}
			return checkout(request,delivery)

	context = {'items': items, 'order': order, 'cartItems': cartItems,'location': location,'products': products,}
	return render(request, 'store/cart.html', context)


def checkout(request,delivery):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	phone=''
	if request.user.is_authenticated:
		customer = request.user.customer
		phone=customer.phone_number
		net_total = delivery['cost'] + order.get_cart_total
	else:
		net_total = delivery['cost'] + order['get_cart_total']
	randomlist = random.sample(range(1000, 9999), 1)
	randlis = randomlist[0]
	context = {'items':items, 'order':order, 'cartItems':cartItems, 'phone_number':phone,'delivery':delivery,'code':randlis,'net_total':net_total}
	return render(request, 'store/checkout.html', context)

def updateItem(request):

	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)

def check_login(request):
    if request.method == "GET":
        raise Http404("URL doesn't exists")
    else:
        response_data = {}
        login = request.POST["login"]
        user = None
        try:
            try:
                # we are matching the input again hardcoded value to avoid use of DB.
                # You can use DB and fetch value from table and proceed accordingly.
                if User.objects.filter(username__iexact=login).exists():
                    user = True
            except ObjectDoesNotExist as e:
                pass
            except Exception as e:
                raise e
            if not user:
                response_data["is_success"] = True
            else:
                response_data["is_success"] = False
        except Exception as e:
            response_data["is_success"] = False
            response_data["msg"] = "Some error occurred. Please let Admin know."

        return JsonResponse(response_data)
def signup(request):
	if request.user.is_authenticated:
		logout(request)
	if request.method == 'POST' and request.user.is_superuser == False:
		username = request.POST["username"]
		password = request.POST["password"]
		confirmpassword = request.POST["confirm_password"]
		first_name = request.POST["first_name"]
		last_name = request.POST["last_name"]
		email = request.POST["email"]
		phone_number = request.POST["phone_number"]

		# if any of the fields are blank - restart registration with message
		for val in [username, password, first_name, last_name, email, phone_number]:
			if val == '':
				messages.info(request, 'pls fill all the information')
				return redirect('signup')
			elif User.objects.filter(username__iexact=username).exists():
				messages.info(request, 'Username Taken')
				return redirect('signup')
			elif User.objects.filter(email__iexact=email).exists():
				messages.info(request, 'Email already exist')
				return redirect('signup')
			elif password != confirmpassword:
				messages.info(request, "your password does not match")
				return redirect('signup')
			elif len(phone_number) < 11:
				messages.info(request, 'Your phone number is incorrect')
				return redirect('signup')
			elif len(phone_number) > 12:
				messages.info(request, 'Your phone number is incorrect')
				return redirect('signup')
			elif Customer.objects.filter(phone_number__iexact=phone_number).exists():
				messages.info(request, 'Phone number already exists, click on forgert pass'
									   'word if you can\'t remenber your password')
				return redirect('signup')
			elif len(password) < 5:
				messages.info(request, 'password must be at least 5')
				return redirect('signup')
			else:
				use = User.objects.create_user(username=username, email=email, password=password, first_name=first_name,
											   last_name=last_name)
				use.save();
				na = User.objects.get(username=username)
				cus = Customer.objects.create(user=na, name=username, email=email, phone_number=phone_number)
				cus.save();
				user = authenticate(request, username=username, password=password)
				if user is not None:
					login(request, user)
					return redirect('store')
	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	context = {'cartItems': cartItems}
	return render(request, 'store/signup.html', context)

def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
	else:
		customer, order = guestOrder(request, data)

	total = float(data['form']['total'])
	order.transaction_id = transaction_id


	addresss = data['shipping']['address']
	side = data['shipping']['side']
	state = data['shipping']['state']
	order_code = data['shipping']['code']
	info = data['shipping']['info']
	delivery_fee = int(data['shipping']['deliverycost'])
	phone_number = data['shipping']['phone_number']
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	detail = ''
	location = Location.objects.all()
	costs = Location.objects.get(state=state,sides=side)
	cs=costs.price
	price_check=False
	if request.user.is_authenticated:
		price=order.get_cart_total
		net_total=costs.price+price
		is_user=True
	else:
		price = order['get_cart_total']
		net_total = costs.price + price
		is_user = False
	cus = lists.objects.create(customer=customer,detail=detail , address=addresss, phone_number=phone_number,
							   total=price,status='Ordered', price_check=price_check,info=info,deliveryfee=costs.price,Net_total=net_total,is_user=is_user,code=order_code,
							   side=side,state=state,transaction_id = transaction_id)

	if request.user.is_authenticated:
		if total == order.get_cart_total:
			if cs == delivery_fee:
				cus.price_check = True
	else:
		if total == order['get_cart_total']:
			if cs == delivery_fee:
				cus.price_check = True
	if request.user.is_authenticated:
		for items in items:
			cus.detail += items.product.name
			cus.detail += '   @'
			cus.detail += str(items.product.price)
			cus.detail += '  x  '
			cus.detail += str(items.quantity)
			cus.detail += '  =  '
			cus.detail += str(items.product.price*items.quantity)
			cus.detail += '  , '
			cus.detail += '\n'
			cus.detail += '   '
		cus.save()
	else:
		for items in items:
			cus.detail += items['product']['name']
			cus.detail += '   @'
			cus.detail += str(items['product']['price'])
			cus.detail += '  x  '
			cus.detail += str(items['quantity'])
			cus.detail += '  =  '
			cus.detail += str(items['product']['price']*items['quantity'])
			cus.detail += '  , '
			cus.detail += '\n'
			cus.detail += '   '
		cus.save()

	if request.user.is_authenticated:
		if total == order.get_cart_total:
			order.complete = True
		order.save()
	else:
		if total == order['get_cart_total']:
			order['complete'] = True
		order['save']=True
	return JsonResponse('Payment submitted..', safe=False)


def logs(request):
	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	context = {'cartItems': cartItems}
	if request.method == 'POST' and request.user.is_superuser == False:
		username = request.POST['username']
		password = request.POST['password']


		user = authenticate(request,username=username,password=password)

		if user is not None:
			login(request, user)
			return redirect("/")
		else:
			messages.info(request, 'invalid credentials')
			return redirect('logs')
	else:
	   return render(request, 'store/login.html',context)

def logout_view(request):
    logout(request)
    return redirect('/')


def profile(request):
	if request.user.is_authenticated == False:
		return redirect('logs')
	if 'report' in request.POST:
		order = lists.objects.filter(pk=request.POST['id']).first()
		order.report = True
		order.save()
	if request.user.is_authenticated:
		data = cartData(request)
		cartItems = data['cartItems']
		customer = request.user.customer
		count = lists.objects.filter(customer=customer).count()
		report = lists.objects.filter(customer=customer,report=True).count()
		ongoing = lists.objects.filter(customer=customer, status='Ordered').count()
		complete = lists.objects.filter(customer=customer, status='Complete').count()
		cancelled = lists.objects.filter(customer=customer, status='Cancelled').count()
		draft = lists.objects.filter(customer=customer, status='Draft').count()


		contact_list = lists.objects.filter(customer=customer).order_by('-id')
		paginator = Paginator(contact_list, 7)  # Show 25 contacts per page
		page = request.GET.get('page')
		contacts = paginator.get_page(page)

		context = {'contacts': contacts,'count':count,'report':report,'cancelled':cancelled,'ongoing':ongoing,'complete':complete,'draft':draft,'cartItems':cartItems}
	return render(request, 'store/profile.html',context)

def push(request):
	payload = {"head": "Welcome!", "body": "Hello World"}
	user=request.user
	send_user_notification(user=user, payload=payload, ttl=1000)

	return render(request, 'store/webpush.html')

def popup(request):

	return render(request, 'store/popup.html')



def product_detail(request,id,slug):
	# = Product.objects.all().filter(pk=id)
	product = Product.objects.get(pk=id)
	pics = UserProfile.objects.get(user=product.user)
	vendor_product = Product.objects.filter(user=product.user)[:3]
	popular_product = Product.objects.filter(popular='Yes')[:4]
	comments = Comment.objects.filter(product=product.id, status='True')
	comment_no = Comment.objects.filter(product=product.id, status='True').count()
	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	context = {'items': items, 'product': product, 'comments': comments,'comment_no':comment_no,'vendor_product':vendor_product, 'popular_product':popular_product,'pics':pics, 'cartItems': cartItems, 'profileid': id}

	return render(request, 'store/product_detail.html', context)

def view_product(request):
    current_user = request.user  # Access User Session information

    profile = UserProfile.objects.get(user_id=current_user.id)
    if request.method == 'POST':
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


def addcomment(request,id):
   url = request.META.get('HTTP_REFERER')  # get last url
   #return HttpResponse(url)
   if request.method == 'POST':  # check post
      form = CommentForm(request.POST)
      if form.is_valid() and form.cleaned_data['comment'] != '':
         data = Comment()  # create relation with model
         data.subject = form.cleaned_data['subject']
         data.comment = form.cleaned_data['comment']
         data.rate = form.cleaned_data['rate']
         data.ip = request.META.get('REMOTE_ADDR')
         data.product_id=id
         current_user= request.user
         data.user_id=current_user.id
         data.save()  # save data to table
         messages.success(request, "Your review has been sent. Thank you for your interest.")
         return HttpResponseRedirect(url)

   return HttpResponseRedirect(url)

def vend(request):
   url = '/chef/signup'


   return HttpResponseRedirect(url)


