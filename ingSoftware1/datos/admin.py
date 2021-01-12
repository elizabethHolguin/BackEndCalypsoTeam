from django.contrib import admin
from .models import Tarjeta,Cliente,Pedido, Perfil, Categoria, Vendedor, Comidas, Calendario, Dias, DetallePedido, Detalle_dias, Administrador, Configuracion, FormaDePago, Iva, TipoSuscripcion, Suscripcion, Factura, ClienteSuscripcion

# Register your models here.

admin.site.register(Tarjeta)
admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(Perfil)
admin.site.register(Categoria)
admin.site.register(Vendedor)
admin.site.register(Comidas)
admin.site.register(Calendario)
admin.site.register(Dias)
admin.site.register(DetallePedido)
admin.site.register(Detalle_dias)
admin.site.register(Administrador)
admin.site.register(Configuracion)
admin.site.register(FormaDePago)
admin.site.register(Iva)
admin.site.register(TipoSuscripcion)
admin.site.register(Suscripcion)
admin.site.register(Factura)
admin.site.register(ClienteSuscripcion)