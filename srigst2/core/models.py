from django.db import models


class ProjectImage(models.Model):
    title = models.CharField(max_length=200, blank=True, default='Recent Project')
    image = models.ImageField(upload_to='projects/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-uploaded_at']

    def __str__(self):
        return f"{self.title} ({self.uploaded_at.strftime('%d %b %Y')})"


class Review(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True, default='Bhimavaram')
    text = models.TextField()
    stars = models.CharField(max_length=10, default='★★★★★')
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} – {self.stars}"


class Enquiry(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    service = models.CharField(max_length=100, blank=True)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Enquiries'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} – {self.phone}"
