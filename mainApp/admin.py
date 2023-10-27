from django.contrib import admin

from .models import *

admin.site.register((Carousel,Maincategory,Subcategory,Brand,Product,Buyer,Wishlist,Checkout,CheckoutProduct,Contact))