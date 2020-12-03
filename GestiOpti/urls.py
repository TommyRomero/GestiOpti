"""ProyectoFinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from users import views
from paciente import views as paciente
from GestionPedido import views as gestionPedido

urlpatterns = [
    path('', views.welcome),
    path('login', views.login_view,name="login"),
    path('logout', views.logout_view,name="logout"),
    path('admin/', admin.site.urls),
    path('paciente/', paciente.dashboard,name="paciente"),
    path('paciente/create', paciente.create,name="create"),
    path('turnos/', paciente.turnos,name="turnos"),
    path('turnos_create/', paciente.turnos_create,name="turnos_create"),
    path('turnos_edit/<int:id>', paciente.turnos_edit,name="turnos_edit"),
    path('turnos_delete/<int:id>', paciente.turnos_delete,name="turnos_delete"),
    path('info', paciente.info,name="info"),
    path('paciente/historial/<int:id>', paciente.historial,name="historial"),
    path('pedidos/', gestionPedido.dashboard,name="pedidos"),
    path('pedidos/create', gestionPedido.create,name="pedidos_create"),
]
