from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
# Create your models here.

class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)
	phone_number = models.CharField(max_length=20, null=True)
	manager = models.BooleanField(default=False, null=False)
	def __str__(self):
		return self.name

class Product(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	price = models.FloatField(max_length=200,blank=True)
	date_added = models.DateTimeField(auto_now_add=True)
	digital = models.BooleanField(default=False,null=True, blank=True)
	image = models.ImageField(null=True, blank=True,upload_to='images/product')
	profile_image = models.CharField(null=True,default='/images/images/users/ygig.png', max_length=200)
	desc = models.CharField(null=True, max_length=200)
	category = models.CharField(blank=True, max_length=20, choices=[
		('yoghurt', 'yoghurt'),
		('shawarma', 'shawarma'),
		('cake', 'cake'),
		('pop-corn', 'pop-corn'),
		('smothie', 'smothie'),
		('grill', 'grill'),
		('bread', 'bread'),
		('toppings', 'toppings'),
		('drink', 'drink'),
	])
	time = models.IntegerField(blank=True, default="10" )
	ip = models.CharField(max_length=20, blank=True)
	status = models.BooleanField(default=False,null=True, blank=True)
	toppings = models.BooleanField(default=False,null=True, blank=True)
	available = models.BooleanField(default=True)

	popular = models.CharField(blank=True ,max_length=20, choices=[
		('Yes', 'Yes'),
		('No', 'No'),
	])
	class_top = models.CharField(blank=True, max_length=20, choices=[
		('price1', 'price1'),
		('price2', 'price2'),
		('price3', 'price3'),
		('price4', 'price4'),
		('price5', 'price5'),
		('price6', 'price6'),
		('price7', 'price7'),
		('price8', 'price8'),
	])
	class_bottom = models.CharField(blank=True, max_length=20, choices=[
		('price', 'price'),
		('price22', 'price22'),
		('price33', 'price33'),
		('price44', 'price44'),
		('price55', 'price55'),
		('price66', 'price66'),
		('price77', 'price77'),
		('price88', 'price88'),
	])
	class_btn = models.CharField(blank=True, max_length=20, choices=[
		('btn1', 'btn1'),
		('btn2', 'btn2'),
		('btn3', 'btn3'),
		('btn4', 'btn4'),
		('btn5', 'btn5'),
		('btn6', 'btn6'),
		('btn7', 'btn7'),
		('btn8', 'btn8'),
	])
	slides = models.CharField(blank=True, max_length=20, choices=[
		('slider1', 'slider1'),
		('slider2', 'slider2'),
		('slider3', 'slider3'),
		('slider4', 'slider4'),
		('slider5', 'slider5'),
		('slider6', 'slider6'),
		('slider7', 'slider7'),
		('slider8', 'slider8'),
		('slider8', 'sli '),
	])
	color = models.CharField(blank=True, max_length=20, choices=[
		('#E32435', '#E32435'),
		('#6CD96A', '#6CD96A'),
		('#4795D1', '#4795D1'),
		('#292a2f', '#292a2f'),
	])
	color2 = models.CharField(blank=True, max_length=20, choices=[
		('#A30F22', '#A30F22'),
		('#00986F', '#00986F'),
		('#006EB8', '#006EB8'),
		('#131519', '#131519'),
	])

	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url


class Location(models.Model):
	state = models.CharField(max_length=100, choices=[
		('enugu', 'enugu'),
	])
	sides = models.CharField(max_length=100, null=True)
	price = models.IntegerField(null=True)

	def __str__(self):
		return str(self.sides)

class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)

	@property
	def shipping(self):
		shipping = False
		orderitems = self.orderitem_set.all()
		for i in orderitems:
			if i.product.digital == False:
				shipping = True
		return shipping

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total

class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total

class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address

class lists(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)
	detail = models.CharField(max_length=1000, null=False)
	agent = models.CharField(max_length=100, null=False)
	phone_number = models.CharField(max_length=20, null=True)
	total = models.CharField(max_length=20, null=True)
	price_check = models.BooleanField(default=False)
	deliveryfee = models.IntegerField(default=0, null=True)
	code = models.CharField(max_length=10, null=False)
	state = models.CharField(max_length=10, null=True)
	side = models.CharField(max_length=50, null=True)
	Net_total = models.CharField(max_length=20, null=True)
	is_user = models.BooleanField(default=False)
	info = models.CharField(max_length=400, null=True)
	report = models.BooleanField(default=False)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	transaction_id = models.CharField(max_length=100, null=True)
	status = models.CharField(max_length=20, choices=[
		('Draft', 'Draft'),
		('Ordered', 'Ordered'),
		('Cancelled', 'Cancelled'),
		('Complete', 'Complete')
	])
	def __str__(self):
		return str(self.id)

class managers(models.Model):
	user = models.OneToOneField(User, null=False, blank=False, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=20, null=False)
	last_name = models.CharField(max_length=20, null=False)
	username = models.CharField(max_length=20, null=False)
	email = models.CharField(max_length=50, null=False)
	phone_number = models.CharField(max_length=20, null=False)
	date_added = models.DateTimeField(auto_now_add=True)
	auth = models.BooleanField(default=False)
	manager = models.BooleanField(default=True, null=False)
	def __str__(self):
		return self.username


#----------------------------------------------------------------------------------------------

class Comment(models.Model):
    STATUS = (
        ('New', 'New'),
        ('True', 'True'),
        ('False', 'False'),
    )
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50, blank=True)
    comment = models.CharField(max_length=250,blank=True)
    rate = models.FloatField(default=1)
    ip = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=10,choices=STATUS, default='New')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['subject', 'comment', 'rate']

class AddProduct(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'time']
