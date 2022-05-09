from django.shortcuts import render
from django.shortcuts import redirect
from MVT.models import Curso, Profesor, Estudiante
from MVT.forms import formularioCursos, formularioProfesores, formularioEstudiantes


def index(request):

    return render(request, 'MVT/index.html')


def agregarProfesores(request):

    if request.method == 'POST':

        genericForm = formularioProfesores(request.POST)

        print(genericForm)

        if genericForm.is_valid:

            data = genericForm.cleaned_data

            profesor = Profesor(nombre=data['nombre'], apellido=data['apellido'],
                                email=data['email'], cargo=data['cargo'])

            profesor.save()

            return redirect('listarProfesores')

    else:

        genericForm = formularioProfesores()

    return render(request, "MVT/agregarProfesores.html", {"genericForm": genericForm})


def agregarCursos(request):

    if request.method == 'POST':

        genericForm = formularioCursos(request.POST)

        print(genericForm)

        if genericForm.is_valid:

            data = genericForm.cleaned_data

            curso = Curso(
                nombre=data['curso'], camada=data['camada'])

            curso.save()

            return redirect('listarCursos')
    else:

        genericForm = formularioCursos()

    return render(request, 'MVT/agregarCursos.html', {'genericForm': genericForm})


def agregarEstudiantes(request):

    if request.method == 'POST':

        genericForm = formularioEstudiantes(request.POST)

        print(genericForm)

        if genericForm.is_valid:

            data = genericForm.cleaned_data

            estudiante = Estudiante(nombre=data['nombre'], apellido=data['apellido'],
                                    email=data['email'], curso=data['curso'], camada=data['camada'])

            estudiante.save()

            return redirect('listarEstudiantes')

    else:

        genericForm = formularioEstudiantes()

    return render(request, "MVT/agregarEstudiantes.html", {"genericForm": genericForm})


def listarProfesores(request):

    listarProfesores = Profesor.objects.all()

    context = {'listarProfesores': listarProfesores}

    return render(request, 'MVT/listarProfesores.html', context)


def listarCursos(request):

    listarCursos = Curso.objects.all()

    context = {'listarCursos': listarCursos}

    return render(request, 'MVT/listarCursos.html', context)


def listarEstudiantes(request):

    listarEstudiantes = Estudiante.objects.all()

    context = {'listarEstudiantes': listarEstudiantes}

    return render(request, 'MVT/listarEstudiantes.html', context)


def buscarCurso(request):
    return render(request, "MVT/buscarCurso.html")


def buscar(request):

    if request.GET["curso"]:

        curso = request.GET['curso']
        cursos = Curso.objects.filter(nombre__contains=curso)

        return render(request, "MVT/resultadosBusqueda.html", {"cursos": cursos})