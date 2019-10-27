"""Proyecto1 URL Configuration

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
from Proyecto1.views import saludo,trasladar
from Proyecto1.views import despedida,contenido,damefecha,calculaEdad
from Proyecto1.views import opciondehtml,interUsuario



urlpatterns = [#esto es una lista
    path('admin/', admin.site.urls),
    path('principal_saludo/', saludo),
    path('despedida_general/', despedida),
    path('html_contenido/', contenido),
    path('fechaA_html/', damefecha),
    #path('capturaycalcula/<int:agno>', calculaEdad) ak solo se pasa un parametro
    path('capturaycalcula/<int:edad>/<int:agno>', calculaEdad),#2 parametros "sin cerrar el ultimo"
    path('trasladarinfo/', trasladar),
    path('Plantilla3/', opciondehtml),
    path('Plantillax/', interUsuario),
]
#antes no se usaba path era url y era confuso por expresiones regulares
#aun se puede usar URL
