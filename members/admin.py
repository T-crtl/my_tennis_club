from django.contrib import admin
from .models import Member, Products

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "joined_date")

class ProductAdmin(admin.ModelAdmin):
    list_display = ("Descripcion", "Clave", "existencias")    

admin.site.register(Member, MemberAdmin)
admin.site.register(Products, ProductAdmin)