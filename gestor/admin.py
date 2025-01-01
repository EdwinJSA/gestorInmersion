from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Curso)
admin.site.register(models.Estudiante)
admin.site.register(models.Documentos)
admin.site.register(models.Videos)
admin.site.register(models.Recomendaciones)
admin.site.register(models.Correos)
admin.site.register(models.CursoEstudiante)
admin.site.register(models.Usuario)