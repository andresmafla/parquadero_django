from django.db import models

# Create your models here.
class tipo(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class carro(models.Model):
    id = models.AutoField(primary_key=True)
    placa = models.CharField(max_length=100, verbose_name='Placa')
    entrada = models.DateTimeField(verbose_name='Entrada')
    tipo = models.ForeignKey(tipo, on_delete=models.PROTECT)
    salida = False
    tiempo = False
    total = False

    def  __str__(self):
        fila="Placa: "+ self.placa +" - "+"Entrada: "+ str(self.entrada)+" - "+"Tipo: "+str(self.tipo)
        return fila
    
    def delete(self, using=None, keep_parents=False):
        super().delete()