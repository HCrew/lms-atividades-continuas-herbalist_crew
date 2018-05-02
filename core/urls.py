"""lms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import (
    index, sobre, cursos, contato, login, disciplinaADS,
    matricula, ads, adm, disciplinaBancoDeDados, logicaDeProgramacao,
    novoCurso, novaDisciplina
)

urlpatterns = [
    path('', index, name='index'),
    path('sobre/', sobre, name='sobre'),
    path('cursos/', cursos, name='cursos'),
    path('contato/', contato, name='contato'),
    path('login/', login, name='login'),
    path('disciplinaADS/', disciplinaADS, name='disciplinaADS'),
    path('disciplinaBancoDeDados/', disciplinaBancoDeDados, name='disciplinaBancoDeDados'),
    path('matricula/', matricula, name='matricula'),
    path('ADS/', ads, name='ads'),
    path('ADM/', adm, name='adm'),
    path('ADS/logicaDeProgramacao', logicaDeProgramacao, name='logicaDeProgramacao'),
    path('novoCurso/', novoCurso, name='novoCurso'),
    path('novaDisciplina/', novaDisciplina, name='novaDisciplina'),
]
