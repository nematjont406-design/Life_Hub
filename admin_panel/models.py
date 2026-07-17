from django.db import models

class SiteSettings(models.Model):
    site_name = models.CharField(max_length=100, default='LifeHub')
    admin_email = models.EmailField(blank=True, null=True)
    two_factor_auth = models.BooleanField(default=False)
    force_ssl = models.BooleanField(default=False)
    email_notifications = models.BooleanField(default=True)
    telegram_notifications = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'Sayt sozlamalari'
        verbose_name_plural = 'Sayt sozlamalari'
    
    def save(self, *args, **kwargs):
        # Only one instance of settings
        self.id = 1
        super().save(*args, **kwargs)
    
    @classmethod
    def get_settings(cls):
        try:
            return cls.objects.get(id=1)
        except cls.DoesNotExist:
            return cls.objects.create(id=1)
    
    def __str__(self):
        return 'Sayt sozlamalari'