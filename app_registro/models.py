from django.db import models

# Create your models here.

class Conferencista(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    experiencia = models.TextField()
    foto = models.ImageField(upload_to='conferencistas', null=True, blank=True)
    
    def __str__(self):
        return self.nombre

class Conferencia(models.Model):
    #Dupla de duplas
    ESTADOS = (
        ('1', 'Pendiente'),
        ('2', 'En Proceso'),
        ('3', 'Finalizada'),
        ('4', 'Cancelada'),
    )
    nombre = models.CharField(max_length=35)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha = models.DateField()
    hora = models.TimeField()
    conferencista = models.ManyToManyField(Conferencista, blank=True)
    estado = models.CharField(max_length=1, choices=ESTADOS, default='1')
    cupos = models.SmallIntegerField(default=10)

    def __str__(self):
        return f'Conferencia: {self.nombre}'
        
class Participante(models.Model):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    correo = models.EmailField()
    twitter = models.CharField(max_length=35, null=True, blank=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Asistencia(models.Model):
    conferencia = models.ForeignKey(Conferencia, on_delete=models.CASCADE)
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE)
    confirmacion = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.conferencia} | {self.participante}'
    
    class Meta:
        unique_together = ('conferencia', 'participante')
