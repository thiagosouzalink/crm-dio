from django.contrib import admin
from .models import Customer

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    # Visualização
    list_display = ['id', 'first_name', 'last_name', 'email']
