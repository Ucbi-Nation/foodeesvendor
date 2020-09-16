from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.index, name='user_index'),
	path('profile/', views.index, name="info"),
	path('login/', views.login_form, name='logined'),
	path('logout/', views.logout_vendor, name='logout_vendor'),
	path('signup/', views.signup_form, name='signuped'),
	path('user_update/', views.user_update, name='user_update'),
	path('orders/', views.orders, name='all_orders'),
	path('product/add_product/', views.add_product, name='add_product'),
	path('update_image/', views.update_image, name='update_image'),
	path('update_product/<int:id>/<slug:name>/', views.update_product, name='update_product'),
	path('view_product/', views.view_product, name='view_product'),
]