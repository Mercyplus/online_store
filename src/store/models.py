from django.db import models
from django.urls import reverse


class Category(models.Model):
	name = models.CharField(max_length=250, unique=True)
	slug = models.SlugField(max_length=250, unique=True)
	description = models.TextField(blank=True)
	image = models.ImageField(upload_to='category', null=True, blank=True)

	class Meta:
		ordering = ('name',)
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'

	def get_url(self):
		return reverse('products_by_category', args=[self.slug])

	def __str__(self):
		return self.name


class Product(models.Model):
	name = models.CharField(max_length=250, unique=True, verbose_name='Имя продукта')
	slug = models.SlugField(max_length=250, unique=True, verbose_name='Слаг продукта')
	description = models.TextField(blank=True, verbose_name='Описание продукта')
	category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
	price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='Цена')
	image = models.ImageField(upload_to='products', null=True, blank=True, verbose_name='Изображение')
	stock = models.IntegerField(null=True, blank=True, verbose_name='Колличество товара на складе')
	available = models.BooleanField(default=True, verbose_name='В наличии')
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('name',)
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'

	def get_url(self):
		return reverse('product_detail', args=[self.category.slug, self.slug])

	def __str__(self):
		return self.name
