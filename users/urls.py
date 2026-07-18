from django.urls import path
from . import views

urlpatterns = [
    # Guest pages
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('features/', views.features, name='features'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('privacy/', views.privacy, name='privacy'),
    path('terms/', views.terms, name='terms'),
    
    # Auth
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    
# Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
    path('mobile-dashboard/', views.mobile_dashboard, name='mobile_dashboard'),
    path('ai-assistant/', views.ai_assistant_view, name='ai_assistant'),
    path('mobile-ai-assistant/', views.mobile_ai_assistant_view, name='mobile_ai_assistant'),
    path('calendar/', views.calendar_view, name='calendar'),
    path('tasks/', views.tasks_view, name='tasks'),
    path('notes/', views.notes_view, name='notes'),
    path('expenses/', views.expenses_view, name='expenses'),
    path('important-dates/', views.important_dates_view, name='important_dates'),
    path('documents/', views.documents_view, name='documents'),
    path('links/', views.links_view, name='links'),
    path('contacts/', views.contacts_view, name='contacts'),
    path('gallery/', views.gallery_view, name='gallery'),
    path('statistics/', views.statistics_view, name='statistics'),
    path('notifications/', views.notifications_view, name='notifications'),
    path('profile/', views.profile_view, name='profile'),
    path('settings/', views.settings_view, name='settings'),
    
    # Additional modules
    path('wishlist/', views.wishlist_view, name='wishlist'),
    path('health-reminder/', views.health_reminder_view, name='health_reminder'),
    path('shopping-list/', views.shopping_list_view, name='shopping_list'),
    path('goals/', views.goals_view, name='goals'),
    path('password-vault/', views.password_vault_view, name='password_vault'),
    path('ideas/', views.ideas_view, name='ideas'),
    
    # Add page
    path('add/', views.add_view, name='add'),
    
    # Add item endpoints
    path('add-admin/', views.add_admin, name='add_admin'),
    path('add-task/', views.add_task, name='add_task'),
    path('edit-task/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete-task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('get-task/<int:task_id>/', views.get_task, name='get_task'),
    path('add-expense/', views.add_expense, name='add_expense'),
    path('edit-expense/<int:expense_id>/', views.edit_expense, name='edit_expense'),
    path('delete-expense/<int:expense_id>/', views.delete_expense, name='delete_expense'),
    path('get-expense/<int:expense_id>/', views.get_expense, name='get_expense'),
    path('add-document/', views.add_document, name='add_document'),
    path('edit-document/<int:document_id>/', views.edit_document, name='edit_document'),
    path('delete-document/<int:document_id>/', views.delete_document, name='delete_document'),
    path('get-document/<int:document_id>/', views.get_document, name='get_document'),
    path('add-image/', views.add_image, name='add_image'),
    path('edit-image/<int:image_id>/', views.edit_image, name='edit_image'),
    path('delete-image/<int:image_id>/', views.delete_image, name='delete_image'),
    path('get-image/<int:image_id>/', views.get_image, name='get_image'),
    path('add-idea/', views.add_idea, name='add_idea'),
    path('edit-idea/<int:idea_id>/', views.edit_idea, name='edit_idea'),
    path('delete-idea/<int:idea_id>/', views.delete_idea, name='delete_idea'),
    path('get-idea/<int:idea_id>/', views.get_idea, name='get_idea'),
    path('add-note/', views.add_note, name='add_note'),
    path('edit-note/<int:note_id>/', views.edit_note, name='edit_note'),
    path('delete-note/<int:note_id>/', views.delete_note, name='delete_note'),
    path('get-note/<int:note_id>/', views.get_note, name='get_note'),
    path('add-link/', views.add_link, name='add_link'),
    path('edit-link/<int:link_id>/', views.edit_link, name='edit_link'),
    path('delete-link/<int:link_id>/', views.delete_link, name='delete_link'),
    path('get-link/<int:link_id>/', views.get_link, name='get_link'),
    path('add-contact/', views.add_contact, name='add_contact'),
    path('edit-contact/<int:contact_id>/', views.edit_contact, name='edit_contact'),
    path('delete-contact/<int:contact_id>/', views.delete_contact, name='delete_contact'),
    path('get-contact/<int:contact_id>/', views.get_contact, name='get_contact'),
    
    # Special dates endpoints
    path('add-special-date/', views.add_special_date, name='add_special_date'),
    path('edit-special-date/<int:date_id>/', views.edit_special_date, name='edit_special_date'),
    path('delete-special-date/<int:date_id>/', views.delete_special_date, name='delete_special_date'),
    path('search-special-dates/', views.search_special_dates, name='search_special_dates'),
    path('get-special-date/<int:date_id>/', views.get_special_date, name='get_special_date'),
    
    # Profile
    path('change-password/', views.change_password, name='change_password'),
    
# AI Chat endpoint
    path('ai-chat/', views.ai_chat, name='ai_chat'),
    
    # Logout
    path('logout/', views.logout_view, name='logout'),
]
