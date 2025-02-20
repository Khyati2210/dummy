from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Blog)


class author_(admin.ModelAdmin):
    list_display=['name','email']

admin.site.register(Author,author_)

class user_(admin.ModelAdmin):
    list_display=['name','email','password']

admin.site.register(userregister,user_)

class category_(admin.ModelAdmin):
    list_display=['name','description','image']

admin.site.register(Category,category_)

class scraptype_(admin.ModelAdmin):
    list_display=['category','name','price_per_kg']

admin.site.register(ScrapType,scraptype_)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'scrap_type', 'weight', 'total_price', 'status', 'created_at')
    search_fields = ('user__username', 'scrap_type')
    list_filter = ('status', 'created_at')

admin.site.register(Order, OrderAdmin)


class PickupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'address', 'status', 'created_at')  # Customize displayed fields
    search_fields = ('name', 'phone', 'address')  # Enable search
    list_filter = ('status', 'created_at')  # Enable filters
    ordering = ('-created_at',)  

admin.site.register(Pickup, PickupAdmin)



from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at')  
    search_fields = ('name', 'email', 'phone')  
    list_filter = ('created_at',)  
    ordering = ('-created_at',)  


admin.site.register(Contact, ContactAdmin)