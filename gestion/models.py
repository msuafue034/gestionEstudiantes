from datetime import date
from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length = 100, verbose_name = "Nombre")
    codigo = models.CharField(unique = True, max_length = 10, verbose_name = "Código")
    fecha_inicio = models.DateField(blank = False, null = False, verbose_name = "Fecha de inicio")
    fecha_fin = models.DateField(blank = False, null = False, verbose_name = "Fecha de fin")
    # Si las fechas no tienen valor no se puede ejecutar la restricción
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        
    def clean(self):
        if self.fecha_inicio < self.fecha_fin:
            return("La fecha de inicio debe ser anterior a la fecha de finalización.")
    
    
class Estudiante(models.Model):
    nombre = models.CharField(max_length = 100, verbose_name = "Nombre")
    email = models.EmailField(unique = True, verbose_name = "Email")
    fecha_nacimiento = models.DateField(blank = False, null = False, verbose_name = "Fecha de nacimiento") 
    # Si fecha_nacimiento no tiene valor puede dar error al ejecutar la restricción
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"
        
    def clean(self):
        if self.fecha_inicio > date.today():
            return("La fecha de nacimiento no debe ser posterior al día actual.")
    
    
class Inscripcion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name="inscripcionEstudiante")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name="inscripcionCurso")
    fecha_inscripcion = models.DateField(verbose_name = "Fecha de inscripción")
   
    class Meta:
        verbose_name = "Inscripcion"
        verbose_name_plural = "Inscripciones"
        
    def clean(self):
        if self.fecha_inicio > date.today():
            return("La fecha de nacimiento no debe ser posterior al día actual.")