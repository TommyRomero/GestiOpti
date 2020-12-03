from django.db import models
from paciente.models import Paciente
from users.models import User

# Create your models here.
class Producto(models.Model):
    nombre =models.CharField(max_length=200)
    clasificacion=models.CharField(max_length=200)
    precio=models.FloatField(blank=False)

    def __str__(self):
        return self.nombre

class TipoPago(models.Model):
    nombre =models.CharField(max_length=200)
    descripcion=models.TextField(max_length=200)

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    ESTADO_TYPE_CHOICES = (
        ('Pendiente',"Pendiente"),
        ('Pedido',"Pedido"),
        ('Taller',"Taller"),
        ('Finalizado',"Finalizado"),
    )
    
    id_paciente=models.ForeignKey(Paciente,on_delete=models.CASCADE)
    id_usuario=models.ForeignKey(User,on_delete=models.CASCADE)
    id_tipo_pago=models.ForeignKey(TipoPago,on_delete=models.CASCADE)
    estado=models.CharField(max_length=10,choices=ESTADO_TYPE_CHOICES)
    subtotal=models.FloatField()
    total=models.FloatField()

class ProductoPedido(models.Model):
    LENTE_TYPE_DISTANCIA = (
        ('Lejos',"Lejos"),
        ('Cerca',"Cerca")
    )
    LENTE_TYPE_POSICION = (
        ('Derecho',"Derecho"),
        ('Izquierdo',"Izquierdo")
    )
    LENTE_ARMAZON = (
        ('Si',"Si"),
        ('No',"No")
    )
    id_pedido=models.ForeignKey(Pedido,on_delete=models.CASCADE)
    id_producto=models.ForeignKey(Producto,on_delete=models.CASCADE)
    lente_distancia=models.CharField(max_length=6,choices=LENTE_TYPE_DISTANCIA)
    lente_posicion=models.CharField(max_length=10,choices=LENTE_TYPE_POSICION)
    lente_armazon=models.CharField(max_length=2,choices=LENTE_ARMAZON)
    cantidad=models.IntegerField()
    precio=models.FloatField()
    
