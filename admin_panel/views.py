from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from functools import wraps
from django.contrib import messages
from django.db.models import Count
from django.contrib.auth import authenticate, login as auth_login
from users.models import User, Task, Note, Idea, Expense, ImportantDate, Document, Link, Contact, Gallery, Wishlist, HealthReminder, ShoppingList, Goal, PasswordVault, Notification
import json
from datetime import datetime, date
import os
from django.template.loader import render_to_string
from io import BytesIO
from xhtml2pdf import pisa
from django.conf import settings

# Custom admin required decorator
def admin_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('admin_login')
        if not request.user.is_staff:
            return redirect('admin_login')
        return view_func(request, *args, **kwargs)
    return _wrapped_view

@admin_required
def admin_dashboard(request):
    # Get real statistics
    from datetime import date
    today = date.today()
    
    total_users = User.objects.count()
    premium_users = User.objects.filter(is_premium=True).count()
    total_tasks = Task.objects.count()
    total_notes = Note.objects.count()
    total_ideas = Idea.objects.count()
    today_registrations = User.objects.filter(created_at__date=today).count()
    
    context = {
        'total_users': total_users,
        'premium_users': premium_users,
        'total_tasks': total_tasks,
        'total_notes': total_notes,
        'total_ideas': total_ideas,
        'today_registrations': today_registrations,
    }
    return render(request, 'admin_panel/dashboard.html', context)

@admin_required
def admin_users(request):
    users = User.objects.all().order_by('-created_at')
    return render(request, 'admin_panel/users.html', {'users': users})

@admin_required
def admin_user_detail(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user_tasks = Task.objects.filter(user=user)
    user_notes = Note.objects.filter(user=user)
    user_ideas = Idea.objects.filter(user=user)
    user_expenses = Expense.objects.filter(user=user)
    user_dates = ImportantDate.objects.filter(user=user)
    user_documents = Document.objects.filter(user=user)
    user_links = Link.objects.filter(user=user)
    user_contacts = Contact.objects.filter(user=user)
    user_gallery = Gallery.objects.filter(user=user)
    user_wishlist = Wishlist.objects.filter(user=user)
    user_health = HealthReminder.objects.filter(user=user)
    user_shopping = ShoppingList.objects.filter(user=user)
    user_goals = Goal.objects.filter(user=user)
    user_passwords = PasswordVault.objects.filter(user=user)
    
    context = {
        'user_obj': user,
        'user_tasks': user_tasks,
        'user_notes': user_notes,
        'user_ideas': user_ideas,
        'user_expenses': user_expenses,
        'user_dates': user_dates,
        'user_documents': user_documents,
        'user_links': user_links,
        'user_contacts': user_contacts,
        'user_gallery': user_gallery,
        'user_wishlist': user_wishlist,
        'user_health': user_health,
        'user_shopping': user_shopping,
        'user_goals': user_goals,
        'user_passwords': user_passwords,
    }
    return render(request, 'admin_panel/user_detail.html', context)

@admin_required
def admin_user_edit(request, user_id):
    user = get_object_or_404(User, id=user_id)
    
    if request.method == 'POST':
        user.username = request.POST.get('username', user.username)
        user.email = request.POST.get('email', user.email)
        user.phone = request.POST.get('phone', user.phone)
        user.bio = request.POST.get('bio', user.bio)
        user.is_premium = request.POST.get('is_premium') == 'on'
        user.is_active = request.POST.get('is_active') == 'on'
        user.is_staff = request.POST.get('is_staff') == 'on'
        user.save()
        messages.success(request, f"Foydalanuvchi {user.username} muvaffaqiyatli yangilandi!")
        return redirect('admin_user_detail', user_id=user.id)
    
    return render(request, 'admin_panel/user_edit.html', {'user_obj': user})

@admin_required
def admin_user_delete(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        username = user.username
        user.delete()
        messages.success(request, f"Foydalanuvchi {username} muvaffaqiyatli o'chirildi!")
        return redirect('admin_users')
    return render(request, 'admin_panel/user_delete.html', {'user_obj': user})

@admin_required
def admin_user_pdf(request, user_id):
    user = get_object_or_404(User, id=user_id)
    
    # Get all user data
    user_tasks = Task.objects.filter(user=user)
    user_notes = Note.objects.filter(user=user)
    user_ideas = Idea.objects.filter(user=user)
    user_expenses = Expense.objects.filter(user=user)
    user_dates = ImportantDate.objects.filter(user=user)
    user_documents = Document.objects.filter(user=user)
    user_links = Link.objects.filter(user=user)
    user_contacts = Contact.objects.filter(user=user)
    user_gallery = Gallery.objects.filter(user=user)
    user_wishlist = Wishlist.objects.filter(user=user)
    user_health = HealthReminder.objects.filter(user=user)
    user_shopping = ShoppingList.objects.filter(user=user)
    user_goals = Goal.objects.filter(user=user)
    user_passwords = PasswordVault.objects.filter(user=user)
    
    # Handle POST request for selecting data to include
    if request.method == 'POST':
        selected_data = request.POST.getlist('data_type')
    else:
        # Default: include all data types
        selected_data = ['tasks', 'notes', 'ideas', 'expenses', 'dates', 'documents', 
                         'links', 'contacts', 'gallery', 'wishlist', 'health', 
                         'shopping', 'goals', 'passwords']
    
    context = {
        'user_obj': user,
        'user_tasks': user_tasks if 'tasks' in selected_data else None,
        'user_notes': user_notes if 'notes' in selected_data else None,
        'user_ideas': user_ideas if 'ideas' in selected_data else None,
        'user_expenses': user_expenses if 'expenses' in selected_data else None,
        'user_dates': user_dates if 'dates' in selected_data else None,
        'user_documents': user_documents if 'documents' in selected_data else None,
        'user_links': user_links if 'links' in selected_data else None,
        'user_contacts': user_contacts if 'contacts' in selected_data else None,
        'user_gallery': user_gallery if 'gallery' in selected_data else None,
        'user_wishlist': user_wishlist if 'wishlist' in selected_data else None,
        'user_health': user_health if 'health' in selected_data else None,
        'user_shopping': user_shopping if 'shopping' in selected_data else None,
        'user_goals': user_goals if 'goals' in selected_data else None,
        'user_passwords': user_passwords if 'passwords' in selected_data else None,
        'selected_data': selected_data,
    }
    
    return render(request, 'admin_panel/user_pdf.html', context)

@admin_required
def admin_user_pdf_download(request, user_id):
    user = get_object_or_404(User, id=user_id)
    
    # Get all user data
    user_tasks = Task.objects.filter(user=user)
    user_notes = Note.objects.filter(user=user)
    user_ideas = Idea.objects.filter(user=user)
    user_expenses = Expense.objects.filter(user=user)
    user_dates = ImportantDate.objects.filter(user=user)
    user_documents = Document.objects.filter(user=user)
    user_links = Link.objects.filter(user=user)
    user_contacts = Contact.objects.filter(user=user)
    user_gallery = Gallery.objects.filter(user=user)
    user_wishlist = Wishlist.objects.filter(user=user)
    user_health = HealthReminder.objects.filter(user=user)
    user_shopping = ShoppingList.objects.filter(user=user)
    user_goals = Goal.objects.filter(user=user)
    user_passwords = PasswordVault.objects.filter(user=user)
    
    # Handle POST request for selecting data to include
    if request.method == 'POST':
        selected_data = request.POST.getlist('data_type')
    else:
        # Default: include all data types
        selected_data = ['tasks', 'notes', 'ideas', 'expenses', 'dates', 'documents', 
                         'links', 'contacts', 'gallery', 'wishlist', 'health', 
                         'shopping', 'goals', 'passwords']
    
    context = {
        'user_obj': user,
        'user_tasks': user_tasks if 'tasks' in selected_data else None,
        'user_notes': user_notes if 'notes' in selected_data else None,
        'user_ideas': user_ideas if 'ideas' in selected_data else None,
        'user_expenses': user_expenses if 'expenses' in selected_data else None,
        'user_dates': user_dates if 'dates' in selected_data else None,
        'user_documents': user_documents if 'documents' in selected_data else None,
        'user_links': user_links if 'links' in selected_data else None,
        'user_contacts': user_contacts if 'contacts' in selected_data else None,
        'user_gallery': user_gallery if 'gallery' in selected_data else None,
        'user_wishlist': user_wishlist if 'wishlist' in selected_data else None,
        'user_health': user_health if 'health' in selected_data else None,
        'user_shopping': user_shopping if 'shopping' in selected_data else None,
        'user_goals': user_goals if 'goals' in selected_data else None,
        'user_passwords': user_passwords if 'passwords' in selected_data else None,
        'selected_data': selected_data,
        'current_date': datetime.now(),
    }
    
    # Render HTML template for PDF
    html_string = render_to_string('admin_panel/user_pdf_content.html', context, request=request)
    
    # Create PDF
    pdf_buffer = BytesIO()
    pdf = pisa.CreatePDF(html_string, dest=pdf_buffer, encoding='UTF-8')
    
    if pdf.err:
        return HttpResponse('PDF yaratishda xatolik yuzaga keldi', status=500)
    
    # Return PDF for download
    pdf_buffer.seek(0)
    response = HttpResponse(pdf_buffer.read(), content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="user_{user.id}_report.pdf"'
    
    return response

@admin_required
def admin_analytics(request):
    total_users = User.objects.count()
    premium_users = User.objects.filter(is_premium=True).count()
    total_tasks = Task.objects.count()
    total_notes = Note.objects.count()
    total_ideas = Idea.objects.count()
    total_expenses = Expense.objects.count()
    
    context = {
        'total_users': total_users,
        'premium_users': premium_users,
        'total_tasks': total_tasks,
        'total_notes': total_notes,
        'total_ideas': total_ideas,
        'total_expenses': total_expenses,
    }
    return render(request, 'admin_panel/analytics.html', context)

@admin_required
def admin_notifications(request):
    return render(request, 'admin_panel/notifications.html')

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user and user.is_staff:
            auth_login(request, user)
            return redirect('admin_dashboard')
        else:
            messages.error(request, 'Noto\'g\'ri foydalanuvchi nomi yoki parol!')
    return render(request, 'admin_panel/login.html')

@admin_required
def admin_settings(request):
    from .models import SiteSettings
    
    settings = SiteSettings.get_settings()
    
    if request.method == 'POST':
        # Get form data
        settings.site_name = request.POST.get('site_name', 'LifeHub')
        settings.admin_email = request.POST.get('admin_email', '')
        settings.two_factor_auth = request.POST.get('two_factor') == 'on'
        settings.force_ssl = request.POST.get('force_ssl') == 'on'
        settings.email_notifications = request.POST.get('email_notifications') == 'on'
        settings.telegram_notifications = request.POST.get('telegram_notifications') == 'on'
        
        settings.save()
        messages.success(request, 'Sozlamalar muvaffaqiyatli saqlandi!')
    
    context = {
        'settings': settings,
    }
    return render(request, 'admin_panel/settings.html', context)