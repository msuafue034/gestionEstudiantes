from datetime import date, timedelta
from django.db import models
from django.forms import ValidationError


# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    codigo = models.CharField(unique=True, max_length=10, verbose_name="Código")
    fecha_inicio = models.DateField(blank=False, null=False, verbose_name="Fecha de inicio")
    fecha_fin = models.DateField(blank=False, null=False, verbose_name="Fecha de fin")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

    def clean(self):
        if self.fecha_inicio >= self.fecha_fin:
            raise ValidationError("La fecha de inicio debe ser anterior a la fecha de finalización.")


class Estudiante(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    email = models.EmailField(unique=True, verbose_name="Email")
    fecha_nacimiento = models.DateField(blank=False, null=False, verbose_name="Fecha de nacimiento")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"

    def clean(self):
        if self.fecha_nacimiento > date.today():
            raise ValidationError("La fecha de nacimiento no debe ser posterior al día actual.")
        if self.fecha_nacimiento > date.today() - timedelta(days=18*365):
            raise ValidationError("El estudiante debe tener al menos 18 años de edad.")
        # timedelta calcula diferencias entre dos fechas (como date, pero con intervalos en vez de fechas específicas)
        # aquí comprueba si 18*365 (18 años) es mayor a la fecha actual y si no, devuelve error

class Inscripcion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name="inscripcionEstudiante")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name="inscripcionCurso")
    fecha_inscripcion = models.DateField(verbose_name="Fecha de inscripción")

    def __str__(self):
        return f"{self.estudiante.nombre} - {self.curso.nombre}"

    class Meta:
        verbose_name = "Inscripcion"
        verbose_name_plural = "Inscripciones"

    def clean(self):
        if self.fecha_inscripcion > date.today():
            raise ValidationError("La fecha de inscripción no puede ser posterior al día actual.")
        if self.fecha_inscripcion > self.curso.fecha_fin:
            raise ValidationError("No se puede inscribir a un curso que ya ha finalizado.")
        if Inscripcion.objects.filter(estudiante=self.estudiante, curso=self.curso).exists():
            raise ValidationError("El estudiante ya está inscrito en este curso.")