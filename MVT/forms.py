from django import forms

class formularioCursos(forms.Form):

    curso = forms.CharField(max_length=30)
    camada = forms.IntegerField()

class formularioProfesores(forms.Form):

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    cargo = forms.CharField(max_length=30)

class formularioEstudiantes(forms.Form):

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    curso = forms.CharField(max_length=30)
    camada = forms.IntegerField()
