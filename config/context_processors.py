from admin_panel.models import SiteSettings

def site_settings(request):
    """Add site settings to all templates"""
    try:
        settings = SiteSettings.objects.get(id=1)
    except SiteSettings.DoesNotExist:
        settings = None
    return {
        'site_settings': settings,
    }