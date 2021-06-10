from django.db import models

# Create your models here.

class Conferencista(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    experiencia = models.TextField()

    def __str__(self):
        return self.nombre

class Conferencia(models.Model):
    nombre = models.CharField(max_length=35)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha = models.DateField()
    hora = models.TimeField()
    conferencista = models.ForeignKey(Conferencista, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'Conferencia; {self.nombre} - Conferencista: {self.conferencista}'
        
class Participante(models.Model):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    correo = models.EmailField()
    twitter = models.CharField(max_length=35, null=True, blank=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
