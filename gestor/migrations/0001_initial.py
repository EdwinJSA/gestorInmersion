# Generated by Django 5.1.4 on 2025-01-01 19:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('numeroEstudiante', models.CharField(max_length=12)),
                ('edad', models.IntegerField()),
                ('nombrePadre', models.CharField(max_length=100)),
                ('numeroPadre', models.CharField(max_length=12)),
                ('direccion', models.CharField(max_length=200)),
                ('fechaNac', models.DateField()),
                ('estado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('tipoUser', models.IntegerField(choices=[(1, 'Estudiante'), (2, 'Profesor')])),
                ('contrasena', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Documentos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=1000)),
                ('fecha', models.DateField()),
                ('visibilidad', models.BooleanField()),
                ('idCurso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestor.curso')),
            ],
        ),
        migrations.CreateModel(
            name='Recomendaciones',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.TextField(max_length=1000)),
                ('fecha', models.DateField()),
                ('idEstudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestor.estudiante')),
            ],
        ),
        migrations.AddField(
            model_name='estudiante',
            name='idUsuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestor.usuario'),
        ),
        migrations.CreateModel(
            name='Correos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('asunto', models.CharField(max_length=100)),
                ('cuerpo', models.TextField(max_length=1000)),
                ('fecha', models.DateField()),
                ('estado', models.CharField(choices=[('enviado', 'Enviado'), ('recibido', 'Recibido'), ('leido', 'Leído')], default='enviado', max_length=10)),
                ('linkArchivo', models.URLField(max_length=1000)),
                ('idDestino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='correos_recibidos', to='gestor.usuario')),
                ('idOrigen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='correos_enviados', to='gestor.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=1000)),
                ('link', models.URLField(max_length=1000)),
                ('visibilidad', models.BooleanField()),
                ('idCurso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestor.curso')),
            ],
        ),
        migrations.CreateModel(
            name='CursoEstudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idCurso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestor.curso')),
                ('idEstudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestor.estudiante')),
            ],
            options={
                'unique_together': {('idEstudiante', 'idCurso')},
            },
        ),
    ]
