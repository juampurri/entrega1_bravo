from django.urls import path
from . import views

urlpatterns = [
  
  path("cursos", views.cursos),
  path("alta_curso/<nombre>", views.alta_curso)




  #path("alta_curso", views.curso_formulario)
]
