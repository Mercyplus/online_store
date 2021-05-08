from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import Group, User
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout


def home(request, category_slug=None):
	category_page = None
	products = None
	if category_slug != None:
		category_page = get_object_or_404(Category, slug=category_slug)
		products = Product.objects.filter(category=category_page, available=True)
	else:
		products = Product.objects.all().filter(available=True)
	return render(request, 'home.html', {'category': category_page, 'products': products})


def product(request, category_slug, product_slug):
	cart_product_form = CartAddProductForm()
	try:
		product = Product.objects.get(category__slug=category_slug, slug=product_slug)
	except Exception as e:
		raise e
	return render(request, 'product.html', {'product': product, 'cart_product_form': cart_product_form})


def signUpView(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			signup_user = User.objects.get(username=username)
			user_group = Group.objects.get(name='User')
			user_group.user_set.add(signup_user)
	else:
		form = SignUpForm()
	return render(request, 'signup.html', {'form': form})


def loginView(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				return redirect('signup')

	else:
		form = AuthenticationForm()
	return render(request, 'login.html', {'form': form})


def signoutView(request):
	logout(request)
	return redirect('login')
