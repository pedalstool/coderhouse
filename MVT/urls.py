from django.urls import path

from MVT import views

urlpatterns = [   
    path('', views.index, name="index"),
    path('agregarCursos', views.agregarCursos, name="agregarCursos"),
    path('listarCursos', views.listarCursos, name="listarCursos"),
    path('agregarProfesores', views.agregarProfesores, name="agregarProfesores"),
    path('listarProfesores', views.listarProfesores, name = 'listarProfesores'),
    path('agregarEstudiantes', views.agregarEstudiantes, name="agregarEstudiantes"),
    path('listarEstudiantes', views.listarEstudiantes, name="listarEstudiantes"),
    path('buscarCurso', views.buscarCurso, name='buscarCurso'),
    path('buscar/', views.buscar)
]