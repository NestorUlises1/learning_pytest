from django.db import models
from django.utils.timezone import now

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=30, unique=True)
    LAYOFFS = 'LAYOFFS'
    HIRING_FREEZE = 'HIRING FREEZE'
    HIRING = 'HIRING'
    status_choices = {
        LAYOFFS: 'Layoffs',
        HIRING_FREEZE: 'Hiring Freeze',
        HIRING: 'Hiring'
    }
    status = models.CharField(max_length=13, choices=status_choices, default=HIRING)
    last_update = models.DateTimeField(default=now, editable=True)
    application_link = models.URLField(blank=True)
    notes = models.CharField(max_length=100, blank=True)