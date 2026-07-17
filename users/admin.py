from django.contrib import admin
from .models import User, Task, Note, Expense, ImportantDate, Document, Link, Contact, Gallery, Wishlist, HealthReminder, ShoppingList, Goal, PasswordVault, Notification

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_premium', 'created_at']
    list_filter = ['is_premium', 'created_at']
    search_fields = ['username', 'email']

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'deadline', 'priority', 'status']
    list_filter = ['priority', 'status', 'deadline']
    search_fields = ['title', 'description']

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'is_pinned', 'is_favorite']
    list_filter = ['is_pinned', 'is_favorite']
    search_fields = ['title', 'content']

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['amount', 'user', 'category', 'date']
    list_filter = ['category', 'date']
    search_fields = ['description']

@admin.register(ImportantDate)
class ImportantDateAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'date', 'type']
    list_filter = ['type', 'date']
    search_fields = ['title']

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'created_at']
    search_fields = ['title']

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'url']
    search_fields = ['title', 'url']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'phone', 'email']
    search_fields = ['name', 'phone', 'email']

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'is_favorite']
    list_filter = ['is_favorite']

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'price', 'is_purchased']
    list_filter = ['is_purchased']

@admin.register(HealthReminder)
class HealthReminderAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'time']
    search_fields = ['title']

@admin.register(ShoppingList)
class ShoppingListAdmin(admin.ModelAdmin):
    list_display = ['item', 'user', 'is_purchased']
    list_filter = ['is_purchased']

@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'target_date', 'progress']
    list_filter = ['progress']

@admin.register(PasswordVault)
class PasswordVaultAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'username']
    search_fields = ['title', 'username']

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'is_read', 'created_at']
    list_filter = ['is_read', 'created_at']