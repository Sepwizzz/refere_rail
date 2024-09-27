from django.db import models

class Arbitros(models.Model):
    cedula = models.CharField(max_length=11, primary_key=True)
    nombreCompleto = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    celular = models.CharField(max_length=20)
    disciplina = models.CharField(max_length=50, blank=True, null=True)
    tipoArbitro = models.CharField(max_length=50, blank=True, null=True)
    ciudad = models.CharField(max_length=10, )
    localidad = models.CharField(max_length=50, blank=True, null=True)
    perfilDeportivo = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100)

class Organizador(models.Model):
    cedula_Organizador = models.CharField(max_length=11, primary_key=True)
    nombre_completo = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    celular = models.CharField(max_length=20)
    contrasena = models.CharField(max_length=100)



class Evento(models.Model):
    TIPOS_CHOICES = (
        ('amistoso', 'Amistoso'),
        ('torneo', 'Torneo'),
    )  
    estados = (
        ('espera', 'Espera'),
        ('reservado', 'Reservado'),
        ('compleatdo','Compleatdo')
    )
    LOCALIDADES_CHOICES = (
        ('Usaquén', 'Usaquén'),
        ('Chapinero', 'Chapinero'),
        ('Santa Fe', 'Santa Fe'),
        ('San Cristóbal', 'San Cristóbal'),
        ('Usme', 'Usme'),
        ('Tunjuelito', 'Tunjuelito'),
        ('Bosa', 'Bosa'),
        ('Kennedy', 'Kennedy'),
        ('Fontibón', 'Fontibón'),
        ('Engativá', 'Engativá'),
        ('Suba', 'Suba'),
        ('Barrios Unidos', 'Barrios Unidos'),
        ('Teusaquillo', 'Teusaquillo'),
        ('Los Mártires', 'Los Mártires'),
        ('Antonio Nariño', 'Antonio Nariño'),
        ('Puente Aranda', 'Puente Aranda'),
        ('La Candelaria', 'La Candelaria'),
        ('Rafael Uribe Uribe', 'Rafael Uribe Uribe'),
        ('Ciudad Bolívar', 'Ciudad Bolívar'),
        ('Usme', 'Usme'),
        ('Tunjuelito', 'Tunjuelito'),
        ('Bosa', 'Bosa'),
        ('Kennedy', 'Kennedy'),
        ('Fontibón', 'Fontibón'),
        ('Engativá', 'Engativá'),
        ('Suba', 'Suba'),
        ('Barrios Unidos', 'Barrios Unidos'),
        ('Teusaquillo', 'Teusaquillo'),
        ('Los Mártires', 'Los Mártires'),
        ('Antonio Nariño', 'Antonio Nariño'),
        ('Puente Aranda', 'Puente Aranda'),
        ('La Candelaria', 'La Candelaria'),
        ('Rafael Uribe Uribe', 'Rafael Uribe Uribe'),
        ('Ciudad Bolívar', 'Ciudad Bolívar'),
        ('Sumapaz', 'Sumapaz'),
        ('Soacha', 'Soacha'),  # Agregamos Soacha a las localidades
    )
    
    fecha_de_inicio = models.DateField()
    fecha_de_finalizacion = models.DateField(null=True, blank=True)
    hora = models.TimeField()
    localidad=models.CharField(max_length=20, choices=LOCALIDADES_CHOICES)
    lugar = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPOS_CHOICES)
    tipo_de_arbitro = models.CharField(max_length=100)
    arbitros = models.ForeignKey(Arbitros,on_delete=models.CASCADE,null=True, blank=True)  # Relación muchos a muchos con Arbitros
    organizador = models.ForeignKey(Organizador, on_delete=models.CASCADE)  # Relación uno a muchos con Organizador
    estado = models.CharField(max_length=20, choices=estados)


    def __str__(self):
        return f"{self.tipo.capitalize()} - {self.fecha_de_inicio}"