from django.db import models
from django.urls import reverse
import uuid

# Create your models here.
class Tipo(models.Model):

    LOAN_STATUS = (
        ('ro', 'Roll'),
        ('pr', 'Promocion'),
        ('po', 'Postre'),
    )
    nombre = models.CharField(
        max_length=2,
        choices=LOAN_STATUS,
        blank=True,
        default='ro',
        help_text='categoria del producto',
    )

    def __str__(self):
        return self.nombre

class Producto(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    imagen = models.ImageField(upload_to='static/img/', default='static/img/neko.png')
    nombrep = models.CharField(max_length=20)
    tipop = models.ForeignKey('Tipo', on_delete=models.SET_NULL, null=True)
    descripcion = models.TextField(max_length=300)
    precio = models.IntegerField()
    


    def __str__(self):
        return f'{self.id} ({self.nombrep})'