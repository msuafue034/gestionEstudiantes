from django.urls import include, path
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='index'),
    #path('cursos/', views.listar_cursos, name='listar_cursos'),
    path('cursos/', ListarCursos.as_view(), name='listar_cursos'),
    #path('cursos/crear/', views.crear_curso, name='crear_curso'),
    path('cursos/crear/', CrearCurso.as_view(), name='crear_curso'),
    #path('cursos/editar/<int:id>/', views.editar_curso, name='editar_curso'),
    path('cursos/editar/<int:id>/', EditarCurso.as_view(), name='editar_curso'),
    #path('cursos/eliminar/<int:id>/', views.eliminar_curso, name='eliminar_curso'),
    path('cursos/eliminar/<int:id>/', EliminarCurso.as_view(), name='eliminar_curso'),
    
    path('estudiantes/', views.listar_estudiantes, name='listar_estudiantes'),
    path('estudiantes/crear/', views.crear_estudiante, name='crear_estudiante'),
    path('estudiantes/editar/<int:id>/', views.editar_estudiante, name='editar_estudiante'),
    path('estudiantes/eliminar/<int:id>/', views.eliminar_estudiante, name='eliminar_estudiante'),
    
    path('inscripciones/', views.listar_inscripciones, name='listar_inscripciones'),
    path('inscripciones/crear/', views.crear_inscripcion, name='crear_inscripcion'),
    path('inscripciones/eliminar/<int:id>/', views.eliminar_inscripcion, name='eliminar_inscripcion'),
]
