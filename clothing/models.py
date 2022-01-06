from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from phonenumber_field.modelfields import PhoneNumberField


gender = (
    ('Муж.', 'Муж.'),
    ('Жен.', 'Жен.')
)
season = (
    ('зима', 'Зима'),
    ('весна', 'Весна'),
    ('лето', 'Лето'),
    ('осень', 'Осень')
)


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    phone = PhoneNumberField(null=False, blank=False, unique=True, region='RU')
    email = models.EmailField(unique=True, null=True, max_length=100)
    address = models.CharField(max_length=150, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Tag(models.Model):
    title = models.CharField(max_length=100, verbose_name='теги товаров')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Size(models.Model):
    """Размеры товаров"""
    sizes_latin = models.CharField(max_length=10, verbose_name='Размеры на латинском')
    numeric_size = models.IntegerField()

    def __str__(self):
        return f'{self.sizes_latin} : {self.numeric_size}'


class Brand(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название фирмы')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    """Товары"""
    title = models.CharField(max_length=250, verbose_name='Название товара')
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(max_length=1200)
    tags = models.ManyToManyField(Tag)
    sizes = models.ManyToManyField(Size)
    gender = models.CharField(choices=gender, max_length=10)
    season = models.CharField(choices=season, max_length=10)
    image = models.ImageField(upload_to='product/%Y/%M', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена товара')
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse('slug', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


# class CartProduct(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)
#
#
# class Cart(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


# class Order(models.Model):
#     """Товары для заказа"""
#     cart = models.ForeignKey(Cart, on_delete=models.SET)
#     is_ordering = models.BooleanField(default=False)
