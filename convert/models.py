from django.db import models

# Create your models here.
from django.db import models

class ChoosePatternModel(models.Model):
    CYRILLIC = 'cyrillic'
    LATIN = 'latin'

    PATTERN_CHOICES = [
        (CYRILLIC, 'Cyrillic'),
        (LATIN, 'Latin'),
    ]

    pattern = models.CharField(max_length=100, choices=PATTERN_CHOICES)
    date = models.DateTimeField(auto_now=True)
    text = models.TextField()

    def __str__(self):
        return f"{self.date.strftime('%Y-%m-%d %H:%M:%S')} - {self.pattern}"


class ChoosePatternModelFile(models.Model):
    CYRILLIC = 'cyrillic'
    LATIN = 'latin'

    PATTERN_CHOICES = [
        (CYRILLIC, 'Cyrillic'),
        (LATIN, 'Latin'),
    ]

    pattern = models.CharField(max_length=100, choices=PATTERN_CHOICES)
    date = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to='uploads/%Y/%m')

    def __str__(self):
        return f"{self.date.strftime('%Y-%m-%d %H:%M:%S')} - {self.pattern}"
