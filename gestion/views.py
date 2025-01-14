from django.shortcuts import render, get_object_or_404, redirect
from .models import Curso, Estudiante, Inscripcion
from .forms import CursoForm, EstudianteForm, InscripcionForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin   # Para necesitar estar logeado para acceder 
#from django.contrib.auth.decorators import login_required --> se añade @login_required antes de la clase para poder acceder solo quien esté logeado

    
############## PRINCIPAL ##############

def index(request):
    return render(request, 'gestion/index.html')

############## CURSO ##############

def listar_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'gestion/listar_cursos.html', {"cursos": cursos})

def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_cursos')
    else:
        form = CursoForm()
    return render(request, 'gestion/crear_curso.html', {'form': form})

def editar_curso(request, id):
    curso = get_object_or_404(Curso, id=id)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('listar_cursos')
    else:
        form = CursoForm(instance=curso)
    return render(request, 'gestion/editar_curso.html', {'form': form})

def eliminar_curso(request, id):
    curso = get_object_or_404(Curso, id=id)
    if request.method == 'POST':
        curso.delete()
        return redirect('listar_cursos')
    return render(request, 'gestion/eliminar_curso.html', {"curso": curso})


############## BASADO EN CLASES - Miércoles 17 ##############

class ListarCursos(LoginRequiredMixin, ListView):
    model = Curso
    form_class = CursoForm
    template_name = 'gestion/listar_cursos.html'
    context_object_name = 'cursos'
    
class CrearCurso(LoginRequiredMixin, CreateView):
    model = Curso
    form_class = CursoForm
    template_name = 'gestion/crear_curso.html'
    context_object_name = 'form'
    success_url = reverse_lazy('listar_cursos')
    
class EditarCurso(LoginRequiredMixin, UpdateView):
    model = Curso
    form_class = CursoForm
    template_name = 'gestion/editar_curso.html'
    context_object_name = 'form'
    pk_url_kwarg='id'
    success_url = reverse_lazy('listar_cursos')
    
class EliminarCurso(LoginRequiredMixin, DeleteView):
    model = Curso
    form_class = CursoForm
    template_name = 'gestion/eliminar_curso.html'
    pk_url_kwarg='id'
    context_object_name = 'curso'
    

############## ESTUDIANTE ##############

def listar_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'gestion/listar_estudiantes.html', {"estudiantes": estudiantes})

def crear_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_estudiantes')
    else:
        form = EstudianteForm()
    return render(request, 'gestion/crear_estudiante.html', {'form': form})

def editar_estudiante(request, id):
    estudiante = get_object_or_404(Estudiante, id=id)
    if request.method == 'POST':
        form = EstudianteForm(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            return redirect('listar_estudiantes')
    else:
        form = EstudianteForm(instance=estudiante)
    return render(request, 'gestion/editar_estudiante.html', {'form': form})

def eliminar_estudiante(request, id):
    estudiante = get_object_or_404(Estudiante, id=id)
    if request.method == 'POST':
        estudiante.delete()
        return redirect('listar_estudiantes')
    return render(request, 'gestion/eliminar_estudiante.html', {"estudiante": estudiante})


############## INSCRIPCION ##############

def listar_inscripciones(request):
    inscripciones = Inscripcion.objects.all()
    return render(request, 'gestion/listar_inscripciones.html', {"inscripciones": inscripciones})

def crear_inscripcion(request):
    if request.method == 'POST':
        form = InscripcionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_inscripciones')
    else:
        form = InscripcionForm()
    return render(request, 'gestion/crear_inscripcion.html', {'form': form})

def eliminar_inscripcion(request, id):
    inscripcion = get_object_or_404(Inscripcion, id=id)
    if request.method == 'POST':
        inscripcion.delete()
        return redirect('listar_inscripciones')
    return render(request, 'gestion/eliminar_inscripcion.html', {"inscripcion": inscripcion})


############## INSCRIPCION - Jueves 19 ##############

class ListarInscripciones(ListView):
    model = Inscripcion
    form_class = InscripcionForm
    template_name = 'gestion/listar_inscripciones.html'
    context_object_name = 'inscripciones'
    
    def get_datos(self):
        estudiante_nombre = self.request.GET.get('estudiante', '').strip()
        curso_nombre = self.request.GET.get('curso', '').strip()
        
        inscripciones = Inscripcion.objects.all()

        if estudiante_nombre:
            inscripciones = inscripciones.filter(estudiante__nombre__icontains=estudiante_nombre)
        if curso_nombre:
            inscripciones = inscripciones.filter(curso__nombre__icontains=curso_nombre)

        return inscripciones

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['inscripciones'] = self.get_datos()
        return context
    
class CrearInscripcion(CreateView):
    model = Inscripcion
    form_class = InscripcionForm
    template_name = 'gestion/crear_inscripcion.html'
    context_object_name = 'inscripciones'
    success_url = reverse_lazy('listar_inscripciones')
    
class EliminarInscripcion(DeleteView):
    model = Inscripcion
    form_class = InscripcionForm
    template_name = 'gestion/eliminar_inscripcion.html'
    pk_url_kwarg='id'
    context_object_name = 'inscripciones'
    