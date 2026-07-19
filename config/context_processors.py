from admin_panel.models import SiteSettings
from django.db.utils import OperationalError

def site_settings(request):
    """Add site settings to all templates"""
    try:
        settings = SiteSettings.get_settings()
    except OperationalError:
        # Database not ready yet (migrations not run)
        settings = None
    return {
        'site_settings': settings,
    }
