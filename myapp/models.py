from django.db import models
from django.contrib.auth.models import User

class Booking(models.Model):
    SERVICE_CHOICES = [
        ('Haircut & Style', 'Haircut & Style'),
        ('Balayage', 'Balayage'),
        ('Keratin', 'Keratin'),
        ('Facial', 'Facial'),
        ('Spa Massage', 'Spa Massage'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    service = models.CharField(max_length=100, choices=SERVICE_CHOICES)
    date = models.DateField()
    time = models.TimeField()
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Confirmed')

    def __str__(self):
        return f"{self.user.username} - {self.service} on {self.date}"

    class Meta:
        ordering = ['date', 'time']

from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name








