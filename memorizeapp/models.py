from django.db import models

# Create your models here.

class Topic(models.Model):
    """Temat tworzony przez użytkownika"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        """Zwrot w postaci ciągu tekstowego"""
        return self.text

class Entry(models.Model):
    """Wpis dodawany przez użytkownika"""
    topic = models.ForeignKey(Topic)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    """Forma entries zamiast Entrys przy odwoływaniu się do kilku wpisów"""
    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.text[:50] + "..."
