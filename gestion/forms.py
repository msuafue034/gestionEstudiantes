from django import forms
from .models import Curso, Estudiante, Inscripcion
from django.forms import ValidationError
from datetime import date


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'codigo', 'fecha_inicio', 'fecha_fin']

    def clean(self):
        cleaned_data = super().clean()
        fecha_inicio = cleaned_data.get('fecha_inicio')
        fecha_fin = cleaned_data.get('fecha_fin')

        if fecha_inicio and fecha_fin and fecha_inicio >= fecha_fin:
            raise forms.ValidationError("La fecha de inicio debe ser anterior a la fecha de finalización.")


class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'email', 'fecha_nacimiento']

    def clean_fecha_nacimiento(self):
        fecha_nacimiento = self.cleaned_data.get('fecha_nacimiento')

        if not fecha_nacimiento:
            raise ValidationError("La fecha de nacimiento es obligatoria.")
        
        if fecha_nacimiento > date.today():
            raise ValidationError("La fecha de nacimiento no puede ser mayor a la fecha actual.")

        edad = date.today().year - fecha_nacimiento.year - (
            (date.today().month, date.today().day) < (fecha_nacimiento.month, fecha_nacimiento.day)
        )

        if edad < 18:
            raise ValidationError("El estudiante debe tener al menos 18 años.")
        
        return fecha_nacimiento


class InscripcionForm(forms.ModelForm):
    class Meta:
        model = Inscripcion
        fields = ['estudiante', 'curso', 'fecha_inscripcion']

    def clean(self):
        cleaned_data = super().clean()
        fecha_inscripcion = cleaned_data.get('fecha_inscripcion')
        curso = cleaned_data.get('curso')
        estudiante = cleaned_data.get('estudiante')

        # Validar que la fecha de inscripción no sea futura
        if fecha_inscripcion and fecha_inscripcion > date.today():
            raise ValidationError("La fecha de inscripción no puede ser posterior al día actual.")

        # Validar que el curso no haya finalizado
        if curso and fecha_inscripcion and fecha_inscripcion > curso.fecha_fin:
            raise ValidationError("No se puede inscribir a un curso que ya ha finalizado.")

        # Validar que el estudiante no esté ya inscrito en el curso
        if curso and estudiante and Inscripcion.objects.filter(estudiante=estudiante, curso=curso).exists():
            raise ValidationError("El estudiante ya está inscrito en este curso.")
