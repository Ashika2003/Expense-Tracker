from django.contrib import admin
from .models import Expense
# Register your models here.
@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display=['name','amount','Cateogry','date']
# Register your models here.
