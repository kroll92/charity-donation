from django.db import models
from categories.models import Category

class Institution(models.Model):
    TYPE_CHOICES = [
        ('fundacja', 'Fundacja'),
        ('organizacja_pozarządowa', 'Organizacja pozarządowa'),
        ('zbiórka_lokalna', 'Zbiórka lokalna'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, default='fundacja')
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name