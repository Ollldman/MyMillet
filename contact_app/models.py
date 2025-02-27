from django.db import models
# Модель формы обратной связи:
# contact/models.py
class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    email = models.EmailField(verbose_name='Email')
    subject = models.CharField(max_length=200, verbose_name='Topic')
    message = models.TextField(verbose_name='Message')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Date')

    def __str__(self):
        return f"Message by {self.name} ({self.email})"

    class Meta:
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedback'