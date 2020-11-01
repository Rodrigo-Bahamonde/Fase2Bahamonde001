from django.db import models
from django.urls import reverse
import uuid

# Create your models here.

class ComentarioGuerra(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50)
    comentario = models.TextField(max_length=1000)
    fecha = models.DateField(null=True, blank=True)
    
    class Meta:
        ordering = ['fecha']

    def __str__(self):
        return f'{self.id}'
    
    def get_absolute_url(self):
        return reverse('comentarioguerra-detail', args=[str(self.id)])

class ComentarioEndgame(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50)
    comentario = models.TextField(max_length=1000)
    fecha = models.DateField(null=True, blank=True)
    
    class Meta:
        ordering = ['fecha']

    def __str__(self):
        return f'{self.id}'
    
    def get_absolute_url(self):
        return reverse('comentarioEndgame-detail', args=[str(self.id)])

class ComentarioDolittle(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50)
    comentario = models.TextField(max_length=1000)
    fecha = models.DateField(null=True, blank=True)
    
    class Meta:
        ordering = ['fecha']

    def __str__(self):
        return f'{self.id}'
    
    def get_absolute_url(self):
        return reverse('comentarioDolittle-detail', args=[str(self.id)])

class ComentarioJoker(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50)
    comentario = models.TextField(max_length=1000)
    fecha = models.DateField(null=True, blank=True)
    
    class Meta:
        ordering = ['fecha']

    def __str__(self):
        return f'{self.id}'
    
    def get_absolute_url(self):
        return reverse('comentarioJoker-detail', args=[str(self.id)])