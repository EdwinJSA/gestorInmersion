from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    class TipoUsuario(models.IntegerChoices):
        ESTUDIANTE = 1, 'Estudiante'
        PROFESOR = 2, 'Profesor'

    tipoUser = models.IntegerField(choices=TipoUsuario.choices, null=False)

class Estudiante(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=False)
    numeroEstudiante = models.CharField(max_length=12, null=False)
    edad = models.IntegerField(null=False)
    nombrePadre = models.CharField(max_length=100, null=False)
    numeroPadre = models.CharField(max_length=12, null=False)
    direccion = models.CharField(max_length=200, null=False)
    fechaNac = models.DateField(null=False)
    estado = models.BooleanField(null=False)
    idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)   
    
    def __str__(self):
        return self.nombre

class Correos(models.Model):
    id = models.AutoField(primary_key=True)
    idOrigen = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='correos_enviados')
    idDestino = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='correos_recibidos')
    asunto = models.CharField(max_length=100, null=False)
    cuerpo = models.TextField(max_length=1000, null=False)
    fecha = models.DateField(null=False)

    class Estado(models.TextChoices):
        ENVIADO = 'enviado', 'Enviado'
        RECIBIDO = 'recibido', 'Recibido'
        LEIDO = 'leido', 'Leído'

    estado = models.CharField(max_length=10, choices=Estado.choices, default=Estado.ENVIADO)
    linkArchivo = models.URLField(max_length=1000, null=False)

    def __str__(self):
        return self.asunto

class Curso(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=False)
    
    def __str__(self):
        return self.nombre

class CursoEstudiante(models.Model):
    idEstudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    idCurso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('idEstudiante', 'idCurso')

class Recomendaciones(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.TextField(max_length=1000, null=False)
    fecha = models.DateField(null=False)
    idEstudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Recomendación para {self.idEstudiante.nombre}"

class Videos(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, null=False)
    descripcion = models.TextField(max_length=1000, null=False)
    link = models.URLField(max_length=1000, null=False)
    idCurso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    visibilidad = models.BooleanField(null=False)
    
    def __str__(self):
        return self.titulo

class Documentos(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, null=False)
    descripcion = models.TextField(max_length=1000, null=False)
    fecha = models.DateField(null=False)
    visibilidad = models.BooleanField(null=False)
    idCurso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.titulo