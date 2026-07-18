from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import JsonResponse
from .models import User, Task, Note, Idea, Expense, ImportantDate, Document, Link, Contact, Gallery, Wishlist, HealthReminder, ShoppingList, Goal, PasswordVault, Notification
import re


def is_mobile(request):
    """Detect if the request is coming from a mobile device"""
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    mobile_patterns = [
        r'Mobile', r'Android', r'iPhone', r'iPad', r'iPod', r'BlackBerry',
        r'IEMobile', r'Opera Mini', r'Windows Phone', r'webOS'
    ]
    return any(re.search(pattern, user_agent) for pattern in mobile_patterns)

# Guest pages
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def features(request):
    return render(request, 'features.html')

def contact(request):
    if request.method == 'POST':
        from admin_panel.models import ContactMessage
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        if name and email and subject and message:
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            return render(request, 'contact.html', {'success': True})
    
    return render(request, 'contact.html')

def faq(request):
    return render(request, 'faq.html')

def privacy(request):
    return render(request, 'privacy.html')

def terms(request):
    return render(request, 'terms.html')

# Auth views
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        
        if password == password_confirm:
            if User.objects.filter(username=username).exists():
                return render(request, 'register.html', {'error': 'Bu username allaqachon mavjud! Boshqa username tanlang.'})
            user = User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password
            )
            login(request, user)
            return redirect('dashboard')
    return render(request, 'register.html')

def forgot_password(request):
    return render(request, 'forgot-password.html')

# Dashboard views
@login_required
def dashboard(request):
    user = request.user
    today_tasks = Task.objects.filter(user=user, deadline__date=timezone.now().date()).count()
    today_expenses = Expense.objects.filter(user=user, date=timezone.now().date())
    total_expenses = sum(e.amount for e in today_expenses)
    upcoming_reminders = ImportantDate.objects.filter(user=user, date__gt=timezone.now().date())[:3]
    important_docs = Document.objects.filter(user=user).count()
    notifications = Notification.objects.filter(user=user, is_read=False).count()
    
    context = {
        'today': timezone.now(),
        'today_tasks': today_tasks,
        'today_expenses': total_expenses,
        'upcoming_reminders': upcoming_reminders,
        'important_docs': important_docs,
        'notifications': notifications,
    }
    # Use mobile template for mobile devices
    if is_mobile(request):
        return render(request, 'dashboard/mobile_dashboard.html', context)
    return render(request, 'dashboard/dashboard.html', context)

@login_required
def ai_assistant_view(request):
    # Use mobile template for mobile devices
    if is_mobile(request):
        return render(request, 'dashboard/mobile_ai_assistant.html')
    return render(request, 'dashboard/ai_assistant.html')

@login_required
def mobile_ai_assistant_view(request):
    return render(request, 'dashboard/mobile_ai_assistant.html')

@login_required
def mobile_dashboard(request):
    return render(request, 'dashboard/mobile_dashboard.html')

@login_required
def calendar_view(request):
    user = request.user
    important_dates = ImportantDate.objects.filter(user=user).order_by('date')
    context = {
        'important_dates': important_dates,
    }
    # Use mobile template for mobile devices
    if is_mobile(request):
        return render(request, 'dashboard/mobile_calendar.html', context)
    return render(request, 'dashboard/calendar.html', context)

@login_required
def tasks_view(request):
    tasks = Task.objects.filter(user=request.user).order_by('-created_at')
    context = {
        'tasks': tasks,
    }
    # Use mobile template for mobile devices
    if is_mobile(request):
        return render(request, 'dashboard/mobile_tasks.html', context)
    return render(request, 'dashboard/tasks.html', context)

@login_required
def notes_view(request):
    notes = Note.objects.filter(user=request.user).order_by('-created_at')
    context = {
        'notes': notes,
    }
    # Use mobile template for mobile devices
    if is_mobile(request):
        return render(request, 'dashboard/mobile_notes.html', context)
    return render(request, 'dashboard/notes.html', context)

@login_required
def expenses_view(request):
    expenses = Expense.objects.filter(user=request.user).order_by('-date', '-created_at')
    context = {
        'expenses': expenses,
    }
    # Use mobile template for mobile devices
    if is_mobile(request):
        return render(request, 'dashboard/mobile_expenses.html', context)
    return render(request, 'dashboard/expenses.html', context)

@login_required
def important_dates_view(request):
    important_dates = ImportantDate.objects.filter(user=request.user).order_by('date')
    context = {
        'important_dates': important_dates,
    }
    # Use mobile template for mobile devices
    if is_mobile(request):
        return render(request, 'dashboard/mobile_calendar.html', context)
    return render(request, 'dashboard/important_dates.html', context)

@login_required
def documents_view(request):
    documents = Document.objects.filter(user=request.user).order_by('-created_at')
    context = {
        'documents': documents,
    }
    # Use mobile template for mobile devices
    if is_mobile(request):
        return render(request, 'dashboard/mobile_documents.html', context)
    return render(request, 'dashboard/documents.html', context)

@login_required
def links_view(request):
    links = Link.objects.filter(user=request.user).order_by('-created_at')
    context = {
        'links': links,
    }
    # Use mobile template for mobile devices
    if is_mobile(request):
        return render(request, 'dashboard/mobile_links.html', context)
    return render(request, 'dashboard/links.html', context)

@login_required
def contacts_view(request):
    contacts = Contact.objects.filter(user=request.user).order_by('-created_at')
    context = {
        'contacts': contacts,
    }
    # Use mobile template for mobile devices
    if is_mobile(request):
        return render(request, 'dashboard/mobile_contacts.html', context)
    return render(request, 'dashboard/contacts.html', context)

@login_required
def gallery_view(request):
    images = Gallery.objects.filter(user=request.user).order_by('-created_at')
    context = {
        'images': images,
    }
    # Use mobile template for mobile devices
    if is_mobile(request):
        return render(request, 'dashboard/mobile_gallery.html', context)
    return render(request, 'dashboard/gallery.html', context)

@login_required
def statistics_view(request):
    # Use mobile template for mobile devices
    if is_mobile(request):
        return render(request, 'dashboard/mobile_statistics.html')
    return render(request, 'dashboard/statistics.html')

@login_required
def notifications_view(request):
    # Use mobile template for mobile devices
    if is_mobile(request):
        return render(request, 'dashboard/mobile_notifications.html')
    return render(request, 'dashboard/notifications.html')

@login_required
def profile_view(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        user.email = request.POST.get('email', user.email)
        user.phone = request.POST.get('phone') or None
        user.bio = request.POST.get('bio') or None
        
        if request.FILES.get('avatar'):
            user.avatar = request.FILES.get('avatar')
        
        user.save()
        return redirect('profile')
    
    # Use mobile template for mobile devices
    if is_mobile(request):
        return render(request, 'dashboard/mobile_profile.html')
    return render(request, 'dashboard/profile.html')

@login_required
def change_password(request):
    if request.method == 'POST':
        user = request.user
        old_password = request.POST.get('old_password')
        new_password1 = request.POST.get('new_password1')
        new_password2 = request.POST.get('new_password2')
        
        if user.check_password(old_password):
            if new_password1 == new_password2:
                user.set_password(new_password1)
                user.save()
                return redirect('login')
    
    return redirect('profile')

@login_required
def settings_view(request):
    # Use mobile template for mobile devices
    if is_mobile(request):
        return render(request, 'dashboard/mobile_settings.html')
    return render(request, 'dashboard/settings.html')

# Additional modules
@login_required
def wishlist_view(request):
    return render(request, 'dashboard/wishlist.html')

@login_required
def health_reminder_view(request):
    return render(request, 'dashboard/health_reminder.html')

@login_required
def shopping_list_view(request):
    return render(request, 'dashboard/shopping_list.html')

@login_required
def goals_view(request):
    return render(request, 'dashboard/goals.html')

@login_required
def password_vault_view(request):
    return render(request, 'dashboard/password_vault.html')

# Add page
@login_required
def add_view(request):
    return render(request, 'add.html')

# Add item endpoints
@login_required
def add_admin(request):
    if not request.user.is_staff:
        return redirect('dashboard')
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if username and email and password:
            User.objects.create_user(
                username=username,
                email=email,
                password=password,
                is_staff=True
            )
            return redirect('add')
    return redirect('add')

@login_required
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        deadline = request.POST.get('deadline')
        priority = request.POST.get('priority')
        if title and deadline:
            Task.objects.create(
                user=request.user,
                title=title,
                description=description,
                deadline=deadline,
                priority=priority
            )
            return redirect('tasks')
    return redirect('add')

@login_required
def edit_task(request, task_id):
    if request.method == 'POST':
        try:
            task = Task.objects.get(id=task_id, user=request.user)
            task.title = request.POST.get('title')
            task.description = request.POST.get('description')
            task.deadline = request.POST.get('deadline')
            task.priority = request.POST.get('priority')
            task.save()
        except Task.DoesNotExist:
            pass
    return redirect('tasks')

@login_required
def delete_task(request, task_id):
    if request.method == 'POST':
        try:
            task = Task.objects.get(id=task_id, user=request.user)
            task.delete()
        except Task.DoesNotExist:
            pass
    return redirect('tasks')

@login_required
def get_task(request, task_id):
    try:
        task = Task.objects.get(id=task_id, user=request.user)
        data = {
            'id': task.id,
            'title': task.title,
            'description': task.description or '',
            'deadline': task.deadline.strftime('%Y-%m-%dT%H:%M'),
            'priority': task.priority,
        }
        return JsonResponse(data)
    except Task.DoesNotExist:
        return JsonResponse({'error': 'Task not found'}, status=404)

@login_required
def add_expense(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        amount = request.POST.get('amount')
        category = request.POST.get('category')
        description = request.POST.get('description')
        date = request.POST.get('date')
        if amount and category:
            Expense.objects.create(
                user=request.user,
                title=title,
                amount=amount,
                category=category,
                description=description,
                date=date if date else timezone.now().date()
            )
            return redirect('expenses')
    return redirect('add')

@login_required
def edit_expense(request, expense_id):
    if request.method == 'POST':
        try:
            expense = Expense.objects.get(id=expense_id, user=request.user)
            expense.title = request.POST.get('title')
            expense.amount = request.POST.get('amount')
            expense.category = request.POST.get('category')
            expense.description = request.POST.get('description')
            expense.date = request.POST.get('date') or timezone.now().date()
            expense.save()
        except Expense.DoesNotExist:
            pass
    return redirect('expenses')

@login_required
def delete_expense(request, expense_id):
    if request.method == 'POST':
        try:
            expense = Expense.objects.get(id=expense_id, user=request.user)
            expense.delete()
        except Expense.DoesNotExist:
            pass
    return redirect('expenses')

@login_required
def get_expense(request, expense_id):
    try:
        expense = Expense.objects.get(id=expense_id, user=request.user)
        data = {
            'id': expense.id,
            'title': expense.title or '',
            'amount': str(expense.amount),
            'category': expense.category,
            'description': expense.description or '',
            'date': expense.date.strftime('%Y-%m-%d'),
        }
        return JsonResponse(data)
    except Expense.DoesNotExist:
        return JsonResponse({'error': 'Expense not found'}, status=404)

@login_required
def add_document(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        file = request.FILES.get('file')
        folder = request.POST.get('folder')
        if title and file:
            Document.objects.create(
                user=request.user,
                title=title,
                file=file,
                folder=folder
            )
            return redirect('documents')
    return redirect('add')

@login_required
def edit_document(request, document_id):
    if request.method == 'POST':
        try:
            document = Document.objects.get(id=document_id, user=request.user)
            document.title = request.POST.get('title')
            if request.FILES.get('file'):
                document.file = request.FILES.get('file')
            document.folder = request.POST.get('folder') or ''
            document.save()
        except Document.DoesNotExist:
            pass
    return redirect('documents')

@login_required
def delete_document(request, document_id):
    if request.method == 'POST':
        try:
            document = Document.objects.get(id=document_id, user=request.user)
            document.delete()
        except Document.DoesNotExist:
            pass
    return redirect('documents')

@login_required
def get_document(request, document_id):
    try:
        document = Document.objects.get(id=document_id, user=request.user)
        data = {
            'id': document.id,
            'title': document.title,
            'folder': document.folder or '',
            'file_url': document.file.url,
        }
        return JsonResponse(data)
    except Document.DoesNotExist:
        return JsonResponse({'error': 'Document not found'}, status=404)

@login_required
def add_image(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.FILES.get('image')
        folder = request.POST.get('folder')
        if title and image:
            Gallery.objects.create(
                user=request.user,
                title=title,
                image=image,
                folder=folder
            )
            return redirect('gallery')
    return redirect('add')

@login_required
def edit_image(request, image_id):
    if request.method == 'POST':
        try:
            image = Gallery.objects.get(id=image_id, user=request.user)
            image.title = request.POST.get('title')
            if request.FILES.get('image'):
                image.image = request.FILES.get('image')
            image.folder = request.POST.get('folder') or ''
            image.save()
        except Gallery.DoesNotExist:
            pass
    return redirect('gallery')

@login_required
def delete_image(request, image_id):
    if request.method == 'POST':
        try:
            image = Gallery.objects.get(id=image_id, user=request.user)
            image.delete()
        except Gallery.DoesNotExist:
            pass
    return redirect('gallery')

@login_required
def get_image(request, image_id):
    try:
        image = Gallery.objects.get(id=image_id, user=request.user)
        data = {
            'id': image.id,
            'title': image.title,
            'folder': image.folder or '',
            'image_url': image.image.url,
        }
        return JsonResponse(data)
    except Gallery.DoesNotExist:
        return JsonResponse({'error': 'Image not found'}, status=404)

# Special dates endpoints
@login_required
def add_special_date(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = request.POST.get('date')
        time = request.POST.get('time') or None
        date_type = request.POST.get('type')
        emoji = request.POST.get('emoji')
        
        if title and date and date_type:
            ImportantDate.objects.create(
                user=request.user,
                title=title,
                description=description,
                date=date,
                time=time,
                type=date_type,
                emoji=emoji
            )
            return redirect('calendar')
    return redirect('calendar')

@login_required
def edit_special_date(request, date_id):
    if request.method == 'POST':
        try:
            special_date = ImportantDate.objects.get(id=date_id, user=request.user)
            special_date.title = request.POST.get('title')
            special_date.description = request.POST.get('description')
            special_date.date = request.POST.get('date')
            special_date.time = request.POST.get('time') or None
            special_date.type = request.POST.get('type')
            special_date.emoji = request.POST.get('emoji')
            special_date.save()
        except ImportantDate.DoesNotExist:
            pass
    return redirect('calendar')

@login_required
def delete_special_date(request, date_id):
    if request.method == 'POST':
        try:
            special_date = ImportantDate.objects.get(id=date_id, user=request.user)
            special_date.delete()
        except ImportantDate.DoesNotExist:
            pass
    return redirect('calendar')

# Search special dates
@login_required
def search_special_dates(request):
    from django.db.models import Q
    query = request.GET.get('q', '')
    if query:
        dates = ImportantDate.objects.filter(
            user=request.user
        ).filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
    else:
        dates = ImportantDate.objects.filter(user=request.user)
    
    results = []
    for date in dates.distinct():
        results.append({
            'id': date.id,
            'title': date.title,
            'description': date.description or '',
            'date': date.date.strftime('%Y-%m-%d'),
            'time': date.time.strftime('%H:%M') if date.time else '',
            'type': date.get_type_display(),
            'emoji': date.emoji,
        })
    
    return JsonResponse({'results': results})

# Get single special date for editing
@login_required
def get_special_date(request, date_id):
    try:
        date = ImportantDate.objects.get(id=date_id, user=request.user)
        data = {
            'id': date.id,
            'title': date.title,
            'description': date.description or '',
            'date': date.date.strftime('%Y-%m-%d'),
            'time': date.time.strftime('%H:%M') if date.time else '',
            'type': date.type,
            'emoji': date.emoji,
        }
        return JsonResponse(data)
    except ImportantDate.DoesNotExist:
        return JsonResponse({'error': 'Date not found'}, status=404)

# Ideas views
@login_required
def ideas_view(request):
    ideas = Idea.objects.filter(user=request.user)
    context = {
        'ideas': ideas,
    }
    return render(request, 'dashboard/ideas.html', context)

@login_required
def add_idea(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        folder = request.POST.get('folder', 'ideas')
        if title and content:
            Idea.objects.create(
                user=request.user,
                title=title,
                content=content,
                folder=folder
            )
            return redirect('ideas')
    return redirect('ideas')

@login_required
def edit_idea(request, idea_id):
    if request.method == 'POST':
        try:
            idea = Idea.objects.get(id=idea_id, user=request.user)
            idea.title = request.POST.get('title')
            idea.content = request.POST.get('content')
            idea.folder = request.POST.get('folder', 'ideas')
            idea.save()
        except Idea.DoesNotExist:
            pass
    return redirect('ideas')

@login_required
def delete_idea(request, idea_id):
    if request.method == 'POST':
        try:
            idea = Idea.objects.get(id=idea_id, user=request.user)
            idea.delete()
        except Idea.DoesNotExist:
            pass
    return redirect('ideas')

@login_required
def get_idea(request, idea_id):
    try:
        idea = Idea.objects.get(id=idea_id, user=request.user)
        data = {
            'id': idea.id,
            'title': idea.title,
            'content': idea.content,
            'folder': idea.folder,
        }
        return JsonResponse(data)
    except Idea.DoesNotExist:
        return JsonResponse({'error': 'Idea not found'}, status=404)

# Notes endpoints
@login_required
def add_note(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        folder = request.POST.get('folder', 'all')
        if title and content:
            Note.objects.create(
                user=request.user,
                title=title,
                content=content,
                folder=folder
            )
            return redirect('notes')
    return redirect('notes')

@login_required
def edit_note(request, note_id):
    if request.method == 'POST':
        try:
            note = Note.objects.get(id=note_id, user=request.user)
            note.title = request.POST.get('title')
            note.content = request.POST.get('content')
            note.folder = request.POST.get('folder', 'all')
            note.save()
        except Note.DoesNotExist:
            pass
    return redirect('notes')

@login_required
def delete_note(request, note_id):
    if request.method == 'POST':
        try:
            note = Note.objects.get(id=note_id, user=request.user)
            note.delete()
        except Note.DoesNotExist:
            pass
    return redirect('notes')

@login_required
def get_note(request, note_id):
    try:
        note = Note.objects.get(id=note_id, user=request.user)
        data = {
            'id': note.id,
            'title': note.title,
            'content': note.content,
            'folder': note.folder,
        }
        return JsonResponse(data)
    except Note.DoesNotExist:
        return JsonResponse({'error': 'Note not found'}, status=404)

# Links endpoints
@login_required
def add_link(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        url = request.POST.get('url')
        category = request.POST.get('category')
        if title and url:
            Link.objects.create(
                user=request.user,
                title=title,
                url=url,
                category=category
            )
            return redirect('links')
    return redirect('links')

@login_required
def edit_link(request, link_id):
    if request.method == 'POST':
        try:
            link = Link.objects.get(id=link_id, user=request.user)
            link.title = request.POST.get('title')
            link.url = request.POST.get('url')
            link.category = request.POST.get('category') or ''
            link.save()
        except Link.DoesNotExist:
            pass
    return redirect('links')

@login_required
def delete_link(request, link_id):
    if request.method == 'POST':
        try:
            link = Link.objects.get(id=link_id, user=request.user)
            link.delete()
        except Link.DoesNotExist:
            pass
    return redirect('links')

@login_required
def get_link(request, link_id):
    try:
        link = Link.objects.get(id=link_id, user=request.user)
        data = {
            'id': link.id,
            'title': link.title,
            'url': link.url,
            'category': link.category or '',
        }
        return JsonResponse(data)
    except Link.DoesNotExist:
        return JsonResponse({'error': 'Link not found'}, status=404)

# Contacts endpoints
@login_required
def add_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        telegram = request.POST.get('telegram')
        email = request.POST.get('email')
        birthday = request.POST.get('birthday') or None
        note = request.POST.get('note')
        if name:
            Contact.objects.create(
                user=request.user,
                name=name,
                phone=phone,
                telegram=telegram,
                email=email,
                birthday=birthday,
                note=note
            )
            return redirect('contacts')
    return redirect('contacts')

@login_required
def edit_contact(request, contact_id):
    if request.method == 'POST':
        try:
            contact = Contact.objects.get(id=contact_id, user=request.user)
            contact.name = request.POST.get('name')
            contact.phone = request.POST.get('phone')
            contact.telegram = request.POST.get('telegram')
            contact.email = request.POST.get('email')
            contact.birthday = request.POST.get('birthday') or None
            contact.note = request.POST.get('note')
            contact.save()
        except Contact.DoesNotExist:
            pass
    return redirect('contacts')

@login_required
def delete_contact(request, contact_id):
    if request.method == 'POST':
        try:
            contact = Contact.objects.get(id=contact_id, user=request.user)
            contact.delete()
        except Contact.DoesNotExist:
            pass
    return redirect('contacts')

@login_required
def get_contact(request, contact_id):
    try:
        contact = Contact.objects.get(id=contact_id, user=request.user)
        data = {
            'id': contact.id,
            'name': contact.name,
            'phone': contact.phone or '',
            'telegram': contact.telegram or '',
            'email': contact.email or '',
            'birthday': contact.birthday.strftime('%Y-%m-%d') if contact.birthday else '',
            'note': contact.note or '',
        }
        return JsonResponse(data)
    except Contact.DoesNotExist:
        return JsonResponse({'error': 'Contact not found'}, status=404)

# AI Chat endpoint
@login_required
def ai_chat(request):
    if request.method == 'POST':
        import json
        data = json.loads(request.body)
        message = data.get('message', '')
        
        # Simple AI response logic (can be enhanced with actual AI integration)
        response = get_ai_response(message)
        
        return JsonResponse({'response': response})
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def get_ai_response(message):
    """Simple AI response generator - can be replaced with actual AI API"""
    message_lower = message.lower()
    
    # Task-related responses
    if 'task' in message_lower or 'vazifa' in message_lower or 'reja' in message_lower:
        return "Sizga vazifalarni tartiblashda yordam bera olaman! Eslatma: Har bir vazifaga prioritet belgilang va muddatini ko'rsating. Bugun qaysi vazifalarni bajarish kerak?"
    
    # Expense-related responses
    elif 'xarajat' in message_lower or 'expense' in message_lower or 'pul' in message_lower:
        return "Xarajatlaringizni tahlil qilishni xohlaysizmi? Men sizga xarajatlarni kategoriyalash va tejash bo'yicha maslahat beraiman. Qaysi kategoriya xarajatlari sizni qiziqtiryapti?"
    
    # Study-related responses
    elif 'o\'qish' in message_lower or 'study' in message_lower:
        return "O'qish rejasini tuzishdan mamnunman! Quyidagi tavsiyalarni bajarishingiz mumkin:\n1. Mavzularni tushunish uchun oldadan reja tuzing\n2. Har kuni 2-3 soat muntazam o'qish vaqti belgilang\n3. O'zlashtirgan mavzularni amalga o'tkazish uyg'otkich sifatida qabul qiling\n4. O'qishdan keyin qisqacha tushintirish yozing"
    
    # Health-related responses
    elif 'sog\'lom' in message_lower or 'health' in message_lower or 'uyqu' in message_lower:
        return "Sog'lom odatlar juda muhim! Kundalik rejangizda quyidagi tavsiyalarni inobatga olish mumkin:\n- Ertalab 10-15 daqiqa jismoniy mashg'ulot\n- Kun davomiida 2-3 marta qisqa dam olish\n- 22:00 dan oldin ekran vaqtni cheklang\n- Kuniga kamida 2 litr suv iching"
    
    # Motivation
    elif 'motivatsiya' in message_lower or 'motivation' in message_lower:
        return "Hech qachon bomaslikka yo'l bermang! Har bir kichik qadam katta marta bilan birga yetishadi. Bugungi kichik maqsadni aniqlab, uni amalga oshiring. Siz qila olasiz! 💪"
    
    # Calendar/schedule
    elif 'calendar' in message_lower or 'taklif' in message_lower or 'jadval' in message_lower:
        return "Taqvim va rejalashtirish! Bugungi sana: " + str(timezone.now().date()) + ". Siz uchun bugungi rejamni tuzishimni xohlaysizmi? Quyidagi vazifalarni kelmadi:"
    
    # Default response
    else:
        return "Assalomu alaykum! Men LifeHub AI. Sizga quyidagi mavzularda yordam bera olaman:\n- Vazifalarni tartiblash\n- Xarajatlarni tahlil qilish\n- O'qish rejalashtirish\n- Sog'lom odatlar tavsiyalari\n- Motivatsiya berish\n\nQaysi mavzu bo'yicha maslahat kerak?"

# Logout
def logout_view(request):
    logout(request)
    return redirect('home')
