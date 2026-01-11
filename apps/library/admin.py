from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Category,Member, Book, IssueBook

@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('id','name',)
    search_fields = ('name',)

@admin.register(Member)
class MemberAdmin(ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ('name', 'email', 'phone')

@admin.register(Book)
class BookAdmin(ModelAdmin):
    list_display = ('id','category', 'name', 'author', 'quantity')
    search_fields = ('name', 'author')
    list_filter = ('author',)
    fieldsets = (
        ('Book Category', {'fields': ('category',)}),
        ('Book Details', {'fields': ('name', 'author','book_id','book_image', )}),
        ('Inventory', {'fields': ('quantity', 'price', 'description',)}),
    )
    widgets = [
      
    ]

@admin.register(IssueBook)
class IssueBookAdmin(ModelAdmin):
    list_display = ('book', 'member', 'issue_date', 'return_date','phone')
    list_filter = ('issue_date', 'return_date')
    search_fields = ('book__title', 'member__name')
