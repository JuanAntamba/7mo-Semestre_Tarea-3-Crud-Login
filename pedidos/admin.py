from django.contrib import admin
from .models import Pedido # Importamos el modelo que acabas de crear

# Le decimos a Django que muestre esta tabla en el panel
admin.site.register(Pedido)