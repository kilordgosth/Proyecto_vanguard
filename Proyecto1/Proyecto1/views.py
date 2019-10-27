from django.http import HttpResponse
import datetime
from django.template import Template,Context#todo lo que este en el modulo aparesca en el menu intelisence



#clases del proyecto 
#clasificar por herencias 

class Persona():

    #edad="edades entre 18-99" #propiedades de la clase 
    def __init__(self, documento, nombre, apellido, edad, fecha_nacimiento, nacionalidad, genero, lugar_recidencia, direccion):#este es el constructor
        #dentro del constructor
        self.documento=documento
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.fecha_nacimiento=fecha_nacimiento
        self.nacionalidad=nacionalidad
        self.genero=genero
        self.lugar_recidencia=lugar_recidencia
        self.direccion=direccion
        
    def descripcion(self):
        print("\nDocumeto: ",self.documento,"\nNombre:",self.nombre,"\nApellido: ",self.apellido,"\nEdad: ",self.edad,"\nF.Nacimiento: ",self.fecha_nacimiento,"\nNacionalidad: ",self.nacionalidad,"\nGenero: ",self.genero,"\nL.Recidencia: ",self.lugar_residencia,"\nDirección: ",self.direccion)
        
class Empleado(Persona):
    def __init__(self, salario, antiguedad, telefono, contraseña, documento_E, nombre_E, apellido_E, edad_E, fecha_nacimiento_E, nacionalidad_E, genero_E, lugar_recidencia_E, direccion_E):#este es el constructor
        super().__init__(documento_E, nombre_E, apellido_E, edad_E, fecha_nacimiento_E, nacionalidad_E, genero_E, lugar_recidencia_E, direccion_E)
        #dentro del constructor
        self.salario=salario
        self.antiguedad=antiguedad
        self.telefono=telefono
        self.contraseña=contraseña

    def descripcion(self):
        super().descripcion()
        print("\nSalario: ",self.salario,"\nAntiguedad: ",self.antiguedad,"\nTelefono: ",self.telefono,"\nContraseña: ",self.contraseña)

class Alumno(Persona):
    nombreh="arturo"#de la case
    def __init__(self, matricula, trimestre, clavecarrera, calificaciones, documento_A, nombre_A, apellido_A, edad_A, fecha_nacimiento_A, nacionalidad_A, genero_A, lugar_recidencia_A, direccion_A):
        super().__init__(documento_A, nombre_A, apellido_A, edad_A, fecha_nacimiento_A, nacionalidad_A, genero_A, lugar_recidencia_A, direccion_A)
        #adentro de alumno
        #tiene la llave primaria que en este caso es la llave primaria 
        #con su llave foranea que es la clave de la carrera
        self.matricula =matricula
        self.trimestre=trimestre
        self.clavecarrera=clavecarrera
        self.calificaciones=calificaciones
    
    def descripcion(self):
        super().descripcion()
        print("\nMatricula: ",self.matricula,"\nTrimestre: ",self.trimestre,"\nClave de carrera: ",self.clavecarrera,"\nCalificaciones: ",self.calificaciones)
        



#recibe un request como primera funcion de argumento 
#funcion python
def saludo(request):
#debuelve la respuesta 
    return HttpResponse("<html><body><h1><center> Hola a todos los que esten viendo esta vista</h1></body></html>")
#cada funcion en views es una vista 
#en las vistas se puede agregar codigo html
#................
#ahora se enlaza la url es el achivo que es

def despedida(request):

    #la mejor forma de pasar la cadena de texto es atravez de una variable
    #documento="todos los domingos soy el pibe de mi barrio"

    p2=Persona(121212121," Profesor Juan","robles",28, "23/10/1990", "colombiano", "masculino", "Bogota", "cll 130 sur 100")
   
    print ("con rango edad:",p2.edad)

    doc_externo=open("/home/heisei/Escritorio/ProyectoDjango/Proyecto1/Proyecto1/Plantillas/plantilla1.html")
    
    plt=Template(doc_externo.read())#importar la clase template y la clase contexto

    doc_externo.close()

    ctx=Context({"Nombreclas":p2.nombre , "Apellidoclas":p2.apellido, "rangoedad":p2.edad})

    documento=plt.render(ctx)#para reenderizar el documento almacenado en plt

   

    # metodo open para cargar documentos externos 
    #especificar la ruta donde esta el documento externo
    #tambien se puede utilizar cargadores
    
    return HttpResponse(documento)

def contenido(request):
    #otra forma para agregar contenido es atravez de triple comilla
    #para que python lo asuma como una unica cadena de caracteres

    documentoI="""
    <html>
    <body>
    <h3><center>Contenido de este documento</h3>
    </body>
    </html>
    """
    return HttpResponse(documentoI)


    #esto es contenido estatico
    #un ejemplo de contenido dinamico es: en este caso la fecha

def damefecha(request):
    
    fecha_actual=datetime.datetime.now()#estas son clases del modulo de pyton  
    documento="""
    <html>
    <body>
    <h1><center>Fecha y Hora Actuales <BR><BR>%s</h1>
    </body>
    </html>
    """% fecha_actual#con marcador de posicion
    return HttpResponse(documento)

#ahora pasar parametros a atravez de la url

def calculaEdad(request,edad,agno):#se modifica para que pase 2 parametros
    ##edadActual=18
    periodo=agno-2019
    edadFutura=edad+periodo#se remplaza la variable
    

    documento="<html><body><h2>En el año %s tendras %s años" %(agno, edadFutura)
    #para comentar varias lineas ctrl+k y ctrl+c
    #inversa = ctrl+u
        
    return HttpResponse(documento)
    #para ver la ejecucion sin error hay que poner un año en la url

def trasladar(request):

    nombre=" Juan"#para utilizar el valor de la variabre en la plantilla usamos context
    #para que se vea en la pajina web

    #ahora con varos valores en un diccionario
    apellido=" Diaz"

    p1=Persona(121212121," Profesor Arnoldo","castro",15, "23/10/1990", "colombiano", "masculino", "Bogota", "cll 130 sur 100")

    ahora=datetime.datetime.now()#pasar datos de la libreria a la plantilla 

    doc_externo=open("/home/heisei/Escritorio/ProyectoDjango/Proyecto1/Proyecto1/Plantillas/plantilla2.html")
    
    plt=Template(doc_externo.read())#importar la clase template y la clase contexto

    doc_externo.close()

    temas=["Administracion","Resepcion","ventas","operario tecnico","lavanderias","guia_turistico","camareros","gastronomia","gestion de servicios al turista","servicios turisticos"]
    temas2=[]
    #facturacion
    #factura electronica
     #firma digital

    ctx=Context({"nombre_persona":nombre, "apellido_persona":apellido, "hora_actual":ahora, "Nombreclas":p1.nombre , "Apellidoclas":p1.apellido,
     "temas":temas, "temas2":temas2})#en este caso se utiliza context para llevar la infomacion a la plantilla 2
    #tambien se puede colocar se se quiere solo el valor ejemplo "Juan" y "Diaz"

    #para organizar mejor la lista en el contexto se agrega la lista en una variable que posteriormente se usa en contexto 
    
    documento=plt.render(ctx)
    return HttpResponse(documento)

def opciondehtml(request):

    E1=Empleado (900.000,"3 años ", 6825459, "pw0xk5", 156546000, "Mariana", "Paez", 17, "2002", "Ecuatoriana", "femenino", "yurupary", "avenida siempre viva")
    ahora=datetime.datetime.now()
    doc_externo=open("/home/heisei/Escritorio/ProyectoDjango/Proyecto1/Proyecto1/Plantillas/Plantilla3.html")
    
    plt=Template(doc_externo.read())#importar la clase template y la clase contexto

    doc_externo.close()

    temas=["Plantillas","Modelos","Formularios","Vistas","Despliege"]
    temas2=[]

    ctx=Context({ "hora_actual":ahora, "Nombreclas":E1.nombre , "Apellidoclas":E1.apellido,"documentoC":E1.documento,"NacionalidadC":E1.nacionalidad,
     "temas":temas, "temas2":temas2})#en este caso se utiliza context para llevar la infomacion a la plantilla 2
    #tambien se puede colocar se se quiere solo el valor ejemplo "Juan" y "Diaz"

    #para organizar mejor la lista en el contexto se agrega la lista en una variable que posteriormente se usa en contexto 
    
    documento=plt.render(ctx)
    return HttpResponse(documento)

def interUsuario(request):

   #matricula, nombre, edad, trimestre, genero, clavecarrera 
   # A1=Alumno(1563487,"heisei arturo velasquez martinez",26 ,"Primero", "Masculino", 11115)
    A1=Alumno(1000000000,"trimestre 2",1563487,8.5,"TI:93082304981","artur","velasquez",40,"15/09/1997","colombiano","masculino","tabogo","calle falsa 123")
    
  
    doc_externo=open("/home/heisei/Escritorio/ProyectoDjango/Proyecto1/Proyecto1/Plantillas/Plantilla3.html")
    
    plt=Template(doc_externo.read())#importar la clase template y la clase contexto

    doc_externo.close()

    temas=["Plantillas","Modelos","Formularios","Vistas","Despliege"]
    temas2=[]

    ctx=Context({"matricula_usuario":A1.matricula,"nombre_usuario":A1.nombre,"edad_usuario":A1.edad,"genero_usuario":A1.genero,"numero_usuario":A1.documento,"carrera_usuario":A1.clavecarrera,"trimestre_usuario":A1.trimestre,"temas":temas, "temas2":temas2,"nombrera":A1.nombreh,})#en este caso se utiliza context para llevar la infomacion a la plantilla 2
    #tambien se puede colocar se se quiere solo el valor ejemplo "Juan" y "Diaz"

    #para organizar mejor la lista en el contexto se agrega la lista en una variable que posteriormente se usa en contexto 
    
    documento=plt.render(ctx)
    return HttpResponse(documento)

 



