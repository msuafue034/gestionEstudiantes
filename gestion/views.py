from django.shortcuts import render, get_object_or_404, redirect
from .models import Curso, Estudiante, Inscripcion
from .forms import CursoForm, EstudianteForm, InscripcionForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

############## BASADO EN CLASES - Miércoles 17 ##############

class ListarCursos(ListView):
    model = Curso
    form_class = CursoForm
    template_name = 'gestion/listar_cursos.html'
    context_object_name = 'cursos'
    
class CrearCurso(CreateView):
    model = Curso
    form_class = CursoForm
    template_name = 'gestion/crear_curso.html'
    context_object_name = 'form'
    success_url = reverse_lazy('listar_cursos')
    
class EditarCurso(UpdateView):
    model = Curso
    form_class = CursoForm
    template_name = 'gestion/editar_curso.html'
    context_object_name = 'form'
    pk_url_kwarg='id'
    success_url = reverse_lazy('listar_cursos')
    
class EliminarCurso(DeleteView):
    model = Curso
    form_class = CursoForm
    template_name = 'gestion/eliminar_curso.html'
    pk_url_kwarg='id'
    context_object_name = 'curso'
    
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
