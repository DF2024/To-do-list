from django.db import models

# Create your models here.


class Task (models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    description = models.TextField(max_length=200, verbose_name="Descripción")
    complete = models.BooleanField(default=False, verbose_name="Completado")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha")


    def __str__(self):
        return self.title

class Meta: 
    ordering = ['-created_at']