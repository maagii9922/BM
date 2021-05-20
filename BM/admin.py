from django.contrib import admin
from .models import Customer, Company, Product,ProdType,State

admin.site.register(Customer)
admin.site.register(Company)
admin.site.register(Product)
admin.site.register(ProdType)
admin.site.register(State)