from django.db import models
from django.contrib.auth.models import User # Importamos el usuario de Django

class Pedido(models.Model):
    # Relacionamos el pedido con el usuario que inició sesión
    estudiante = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Campos del pedido
    platillo = models.CharField(max_length=100)
    cantidad = models.IntegerField(default=1)
    descripcion = models.TextField(blank=True, null=True) # Ej: "Sin cebolla"
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    entregado = models.BooleanField(default=False)

    def __str__(self):
        return f"Pedido de {self.platillo} - {self.estudiante.username}"