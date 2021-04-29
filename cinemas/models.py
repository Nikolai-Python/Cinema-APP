from django.conf import settings 
from django.db import models 
from django.urls import reverse

class Cinema(models.Model):
    title = models.CharField('Cinema', max_length=255) 
    address = models.TextField('Address', max_length=200)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
    )
    def __str__ (self):
        return self.title

    def get_absolute_url(self):
        return reverse('cinema_detail', args=[str(self.id)])



class Seans(models.Model):
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, related_name='seanses')
    seans = models.TextField('Film', max_length=100)
    date = models.DateField(help_text='example: 2021-01-21', blank=True, null=True) 
    time = models.TimeField(help_text='example: 12:00', blank=True, null=True)
    
    def __str__ (self):
        return self.seans

    def get_absolute_url(self):
        return reverse('cinema_list')