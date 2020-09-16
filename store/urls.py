from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from . import views


urlpatterns = [
	#Leave as empty string for base url
	path('', views.index, name="index"),
	path('store/', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('login/', views.logs, name="logs"),
	path('logo/', views.logout_view, name="logout"),
	path('signup/', views.signup, name='signup'),
	path('search/', views.search, name='search'),
	path('price_filter/', views.price_filter, name='price_filter'),
	path('category/', views.category, name='category'),
	path('vendor/<slug:username>/', views.vendor, name='vendor'),
	path('vendor/', views.vend, name='vend'),
	path('check_login/', views.check_login, name='check_login'),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
	path('profile', views.profile, name="profile"),
	path('product/addcomment/<int:id>', views.addcomment, name='addcomment'),
	path('product/<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),

	path('reset_password/',
		 auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
		 name="reset_password"),

	path('reset_password_sent/',
		 auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),
		 name="password_reset_done"),

	path('reset/<uidb64>/<token>/',
		 auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"),
		 name="password_reset_confirm"),

	path('reset_password_complete/',
		 auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),
		 name="password_reset_complete"),
]