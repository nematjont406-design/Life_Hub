from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_dashboard, name='admin_dashboard'),
    path('login/', views.admin_login, name='admin_login'),
    path('users/', views.admin_users, name='admin_users'),
    path('users/<int:user_id>/', views.admin_user_detail, name='admin_user_detail'),
    path('users/<int:user_id>/edit/', views.admin_user_edit, name='admin_user_edit'),
    path('users/<int:user_id>/delete/', views.admin_user_delete, name='admin_user_delete'),
    path('users/<int:user_id>/pdf/', views.admin_user_pdf, name='admin_user_pdf'),
    path('users/<int:user_id>/pdf/download/', views.admin_user_pdf_download, name='admin_user_pdf_download'),
    path('analytics/', views.admin_analytics, name='admin_analytics'),
    path('notifications/', views.admin_notifications, name='admin_notifications'),
    path('settings/', views.admin_settings, name='admin_settings'),
]