from django.db import models


class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)
    def __str__(self):
        return str(self.first_name + self.last_name)


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()
    image = models.ImageField(upload_to="media/", default=None)
    def __str__(self):
        return str(self.name)
    
class Genero(models.Model):
    id_genero  = models.AutoField(db_column='idGenero', primary_key=True) 
    genero     = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.genero)    
    
class Postulante(models.Model):
    rut              = models.CharField(primary_key=True, max_length=10)
    nombre           = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(blank=False, null=False) 
    id_genero        = models.ForeignKey('Genero',on_delete=models.CASCADE, db_column='idGenero')  
    telefono         = models.CharField(max_length=45)
    email            = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    direccion        = models.CharField(max_length=50, blank=True, null=True)  
    activo           = models.IntegerField()

    def __str__(self):
        return str(self.nombre)+" "+str(self.apellido_paterno)       
        




class Colegio(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    colegio = models.ForeignKey(Colegio, on_delete=models.CASCADE, related_name="cursos")

    def __str__(self):
        return f"{self.nombre} - {self.colegio.nombre}"



from django.db import models
from django.contrib.auth.models import User

class Curso(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name="alumnos")
    apoderado = models.ForeignKey(User, on_delete=models.CASCADE, related_name="alumnos")

    def __str__(self):
        return f"{self.nombre} - {self.curso.nombre}"





from django.db import models
from django.contrib.auth.models import User
from demo.models import Curso  # Asegúrate de tener un modelo Curso

class Fondo(models.Model):
    curso = models.OneToOneField(Curso, on_delete=models.CASCADE, related_name="fondo")
    total_colectivo = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Fondo del curso {self.curso.nombre}"

class Deposito(models.Model):
    apoderado = models.ForeignKey(User, on_delete=models.CASCADE, related_name="depositos")
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name="depositos")

    def __str__(self):
        return f"Depósito de {self.monto} por {self.apoderado.username} ({self.fecha})"

class Seguro(models.Model):
    apoderado = models.ForeignKey(User, on_delete=models.CASCADE, related_name="seguros")
    tipo = models.CharField(max_length=100)
    fecha_contratado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Seguro {self.tipo} contratado por {self.apoderado.username}"
