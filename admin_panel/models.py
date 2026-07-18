from django.db import models

class SiteSettings(models.Model):
    site_name = models.CharField(max_length=100, default='LifeHub')
    admin_email = models.EmailField(blank=True, null=True)
    two_factor_auth = models.BooleanField(default=False)
    force_ssl = models.BooleanField(default=False)
    email_notifications = models.BooleanField(default=True)
    telegram_notifications = models.BooleanField(default=False)
    
    # Social media links
    telegram_channel = models.URLField(blank=True, null=True, help_text='Telegram kanal havoli')
    instagram_link = models.URLField(blank=True, null=True, help_text='Instagram havoli')
    youtube_link = models.URLField(blank=True, null=True, help_text='YouTube havoli')
    tiktok_link = models.URLField(blank=True, null=True, help_text='TikTok havoli')
    
    # Site branding
    logo = models.ImageField(upload_to='site/', blank=True, null=True, help_text='Sayt logotipi')
    banner = models.ImageField(upload_to='site/', blank=True, null=True, help_text='Sayt banneri')
    
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


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Murojaat'
        verbose_name_plural = 'Murojaatlar'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.subject}"
