from django.db import models

# Create your models here.
class Tarjeta(models.Model):
    nombre_propietario = models.CharField(max_length=200)
    tipo_tarjeta = models.CharField(max_length=200)
    fecha_caducidad = models.DateField()
    direccion_facturacion = models.CharField(max_length=350)
    cvv = models.IntegerField(default=0)
    numero_tarjeta = models.CharField(max_length=16)

    def __str__(self):
        return self.nombre_propietario + ' . ' + self.numero_tarjeta

class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=250)
    email = models.CharField(max_length=300)
    usuario = models.CharField(max_length=200)
    contraseña = models.CharField(max_length=200)
    direccion = models.CharField(max_length=350)
    fecha_nacimiento = models.DateField()
    id_tarjeta = models.ForeignKey(Tarjeta, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre + ' - ' + self.apellido 

class Pedido(models.Model):
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_emitido = models.DateTimeField('Fecha de emisión')
    estado = models.IntegerField(default=0)
    
    def __str__(self):
        return self.id_cliente
        
class Perfil(models.Model):
    nombre = models.CharField(max_length=200)
    peso_inicio = models.FloatField()
    peso_meta = models.FloatField()
    id_cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    nombre_perfil = models.ForeignKey(Perfil, on_delete = models.CASCADE)

    def __str__(self):
        return self.nombre

class Vendedor(models.Model):
    usuario = models.CharField(max_length=200)
    contraseña = models.CharField(max_length=200)

    def __str__(self):
        return self.usuario

class Comidas(models.Model):
    nombre =  models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    calorias_totales = models.FloatField()
    macronutrientes = models.CharField(max_length=1000)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    id_vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    imagen = models.ImageField()
    direccion_envio = models.CharField(max_length=500)

    def __str__(self):
        return self.nombre + ' - ' + self.descripcion

class Calendario(models.Model):
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_cliente
        
class Dias(models.Model):
    id_calendario = models.ForeignKey(Calendario, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_calendario

class DetallePedido(models.Model):
    id_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    fecha_emitido = models.DateTimeField('Fecha de emisión')
    id_comida = models.ForeignKey(Comidas, on_delete=models.CASCADE)
    id_dias = models.ForeignKey(Dias, on_delete=models.CASCADE)
    hora_entrega = models.TimeField()
    estado_pedido = models.IntegerField(default=0)
       
    def __str__(self):
        return self.id_comida

class Detalle_dias(models.Model):
    id_dias = models.ForeignKey(Dias, on_delete=models.CASCADE)
    hora_entrega = models.DateTimeField('Hora de entrega')
    id_comida = models.ForeignKey(Comidas, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_dias

class Administrador(models.Model):
    usuario = models.CharField(max_length=200)
    contraseña = models.CharField(max_length=200)
 
    def __str__(self):
        return self.usuario

class Configuracion(models.Model):
    dolares_por_kilometros = models.FloatField()
    valor_comida = models.FloatField()
    direccion_fija = models.CharField(max_length=500)
    no_comidas_por_semana = models.IntegerField(default=0)
    no_de_comida_por_dia = models.IntegerField(default=0)

    def __str__(self):
        return self.direccion_fija 

class FormaDePago(models.Model):
    forma_pago = models.CharField(max_length=250)

    def __str__(self):
        return self.forma_pago
    
class Iva(models.Model):
    porcentaje = models.FloatField()
    nombre_impuesto = models.CharField(max_length=300)

    def __str__(self):
        return self.nombre_impuesto


class TipoSuscripcion(models.Model):
    nombre = models.CharField(max_length=350)
    duracion = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre 

class Suscripcion(models.Model):
    nombre = models.CharField(max_length=200)
    id_tipo_suscripcion = models.ForeignKey(TipoSuscripcion, on_delete=models.CASCADE)
    precio = models.FloatField()
    cantidad_comidas = models.IntegerField(default=0)
    comidas_gratis = models.IntegerField(default=0)
    color = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Factura(models.Model):
    id_suscripcion = models.ForeignKey(Suscripcion, on_delete=models.CASCADE)
    id_forma_pago = models.ForeignKey(FormaDePago, on_delete=models.CASCADE)
    id_iva = models.ForeignKey(Iva, on_delete=models.CASCADE)
    monto = models.FloatField()

    def __str__(self):
        return self.id_iva

class ClienteSuscripcion(models.Model):
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_suscripcion = models.ForeignKey(Suscripcion, on_delete=models.CASCADE)
    comidas_consumidas = models.IntegerField(default=0)
    fecha_inicio = models.DateField()
    fecha_de_caducidad = models.DateField()
    fecha_facturacion = models.DateField()
    comidas_disponibles = models.IntegerField(default=0)
    comidas_gratis_disponibles = models.IntegerField(default=0)
    comidas_gratis_consumidas = models.IntegerField(default=0)

    def __str__(self):
        return self.id_cliente










