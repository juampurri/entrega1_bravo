from django.http import HttpResponse
from django.shortcuts import render
from app_coder.models import Curso, Profesor, Alumno
from django.template import loader
from app_coder.forms import Curso_formulario , Profesor_formulario , Alumno_formulario
# Create your views here.


def inicio(request):
    return render(request,"plantillas.html")

def cursos(request):
    cursos = Curso.objects.all()
    dicc = {"cursos": cursos}
    plantilla = loader.get_template("cursos.html")
    documento = plantilla.render(dicc)
    return HttpResponse( documento )


def alta_curso(request, nombre):
    curso = Curso(nombre=nombre, camada=252342)
    curso.save()
    texto = f"Se guardó en la BD el Curso: {curso.nombre} Camada: {curso.camada}"
    return HttpResponse(texto)

def alumnos(request):
    return render(request,"alumnos.html")

def contacto(request):
    return render(request, "contacto.html")

def profesores(request):
    return render(request, "profesores.html")

def curso_formulario(request):

    if  request.method == "POST":
        
        mi_formulario = Curso_formulario(request.POST)
        if mi_formulario.is_valid():
            datos =  mi_formulario.cleaned_data
            print(mi_formulario.cleaned_data)
        curso = Curso( nombre=datos['Nombre'] , camada=datos['Camada'])
        curso.save()
        return render(request, "formulario.html")

    return render(request, "formulario.html")

def buscar_curso(request):
    return render(request, "buscar_curso.html")

def buscar(request):
    if  request.GET['nombre']:
        nombre = request.GET['nombre']
        cursos = Curso.objects.filter(nombre__icontains = nombre)
        return render( request, "resultado_busqueda.html", {"cursos" : cursos})
    else:
        return HttpResponse("Campo vacio")

def buscar_curso(request):
    return render(request, "buscar_curso.html")       


#ALTA PROFESORES
def alta_profesores(request):

    if  request.method == "POST":
        
        mi_formulario = Profesor_formulario(request.POST)

        if mi_formulario.is_valid():
            datos =  mi_formulario.cleaned_data

            profesor = Profesor( nombre=datos['nombre'] , materia=datos['materia'])
            profesor.save()

            return HttpResponse("Se contrató el profesor")

    return render(request, "alta_profesores.html")


#ALTA ALUMNO

def alta_alumnos(request):

    if  request.method == "POST":
        
        mi_formulario = Alumno_formulario(request.POST)
        if mi_formulario.is_valid():
            datos =  mi_formulario.cleaned_data

            alumno = Alumno( nombre=datos['nombre'] , camada=datos['camada'])
            alumno.save()
            return HttpResponse("LLegó un alumno nuevo")

    return render(request, "alta_alumnos.html")
