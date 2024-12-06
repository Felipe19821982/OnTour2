from django.shortcuts import render, redirect
from .models import Album, Musician, Postulante, Genero 
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def index(request):
    context={"clase": "inicio"}
    return render(request, 'demo/index.html', context)


def galeria(request):
    users=get_current_users()
    context={"clase": "galeria", "users":users}
    return render(request, 'demo/galeria.html', context)

@login_required
def perfil(request):
    context={"clase": "perfil"}
    return render(request, 'demo/perfil.html', context)

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

def registro(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        # Validación básica (puedes agregar más validaciones según tus requisitos)
        if not nombre or not email or not password:
            context = {"clase": "registro", "error": "Por favor completa todos los campos."}
            return render(request, 'demo/registro.html', context)
        
        try:
            # Crear usuario con contraseña encriptada
            user = User.objects.create_user(username=nombre, email=email, password=password)
            context = {"clase": "registro", "mensaje": "Los datos fueron registrados"}
            return render(request, 'demo/registro.html', context)
        
        except Exception as e:
            # Capturar errores específicos, como IntegrityError si el nombre de usuario ya existe
            context = {"clase": "registro", "error": f"No se pudo registrar: {str(e)}"}
            return render(request, 'demo/registro.html', context)
    
    else:
        context = {"clase": "registro"}
        return render(request, 'demo/registro.html', context)


def get_current_users():
    active_sessions = Session.objects.filter(expire_date__gte=timezone.now())
    user_id_list = []
    for session in active_sessions:
        data = session.get_decoded()
        user_id_list.append(data.get('_auth_user_id', None))
    # Query all logged in users based on id list
    return User.objects.filter(id__in=user_id_list)

def vinilo(request):
    context={"clase": "vinilo"}
    return render(request, 'demo/vinilo.html', context)

def contactanos(request):
    context={}
    return render(request, 'demo/contactanos.html', context)

def cassette(request):
    context={}
    return render(request, 'demo/cassette.html', context)

def cd(request):
    context={}
    return render(request, 'demo/cd.html', context)

def comprar(request):
    context={}
    return render(request, 'demo/comprar.html', context)

def trabaja(request):
    context={}
    return render(request, 'demo/trabaja.html', context)

# ingresar



def cassette(request):
    context={}
    return render(request, 'demo/cassette.html', context)

def cd(request):
    context={}
    return render(request, 'demo/cd.html', context)

def comprar(request):
    context={}
    return render(request, 'demo/comprar.html', context)

def pagar(request):
    context={}
    return render(request, 'demo/pagar.html', context)


def pagoexitoso(request):
    context={}
    return render(request, 'demo/pagoexitoso.html', context)

def saldoinsuficiente(request):
    context={}
    return render(request, 'demo/saldoinsuficiente.html', context)
# ingresar

def listadoSQL(request):
    # demo=Album.objects.raw('SELECT * FROM demo_Album')
    demo = Postulante.objects.all()
    print(demo)
    context={"demo": demo}
    return render(request, 'demo/listadoSQL.html', context)

#def crud(request):
    #demo = Postulante.objects.all()
    #context={"demo": demo}
    #return render(request, 'demo/alumnos_list.html', context)

def crud(request):
    postulantes = Postulante.objects.all()  # Obtén todos los postulantes
    
    # Paginar los datos
    paginator = Paginator(postulantes, 5)  # Mostrar 5 postulantes por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'demo': page_obj,  # Pasar el objeto de paginación a la plantilla
    }
    return render(request, 'demo/alumnos_list.html', context)



def alumnosAdd(request):
    if request.method != "POST":
        generos = Genero.objects.all()
        context = {"generos": generos}
        return render(request, 'demo/alumnos_add.html', context)
    else:
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        aPaterno = request.POST["paterno"]
        aMaterno = request.POST["materno"]
        fechaNac = request.POST["fechaNac"]
        genero = request.POST["genero"]
        telefono = request.POST["telefono"]
        email = request.POST["email"]
        direccion = request.POST["direccion"]
        activo = "1"

        objGenero = Genero.objects.get(id_genero=genero)
        obj = Postulante.objects.create(
            rut=rut,
            nombre=nombre,
            apellido_paterno=aPaterno,
            apellido_materno=aMaterno,
            fecha_nacimiento=fechaNac,
            id_genero=objGenero,  # Asociar el genero correctamente
            telefono=telefono,
            email=email,
            direccion=direccion,
            activo=activo
        )
        obj.save()
        context = {'mensaje': "OK, datos grabados..."}
        return render(request, 'demo/alumnos_add.html', context)
    
def alumnos_del(request, pk):
    context={}
    try:
        postulante = Postulante.objects.get(rut=pk)
        postulante.delete()
        mensaje ="Bien, datos eliminados..."
        postulantes = Postulante.objects.all()
        context = {'postulantes': postulantes, 'mensaje': mensaje}
        return render(request, 'demo/alumnos_list.html', context)
    except:
        mensaje = "Error, rut no existe..."
        alumnos = Postulante.objects.all()
        context = {'postulantes': postulante, 'mensaje': mensaje}
        return render(request, 'demo/alumnos_list.html', context)
        
def alumnos_finEdit(request,pk):
    if  pk != "":
        postulante = Postulante.objects.get(rut=pk)
        generos = Genero.objects.all()
            
        print(type(postulante.id_genero.genero))
            
        context={'postulante':postulante, 'generos': generos}
    if postulante:
        return render(request, 'demo/alumnos_edit.html', context)
    else:
        context={'mensaje':"Error, rut no existe..."}
        return render(request, 'demo/alumnos_list.html', context)
            
def alumnosUpdate(request):
    if request.method == "POST":
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        apaterno = request.POST["paterno"]
        amaterno = request.POST["materno"]
        fechaNac = request.POST["fechaNac"]
        genero = request.POST["genero"]
        telefono = request.POST["telefono"]
        email = request.POST["email"]
        direccion = request.POST["direccion"]
        activo = "1"

        objGenero = Genero.objects.get(id_genero=genero)
        postulante = Postulante()
        postulante.rut = rut
        postulante.nombre = nombre
        postulante.apellido_paterno = apaterno
        postulante.apellido_materno = amaterno
        postulante.fecha_nacimiento = fechaNac
        postulante.id_genero = objGenero  # Asociar el genero correctamente
        postulante.telefono = telefono
        postulante.email = email
        postulante.direccion = direccion
        postulante.activo = activo
        postulante.save()

        generos = Genero.objects.all()
        context = {
            'mensaje': "Datos actualizados",
            'generos': generos,
            'postulante': postulante
        }
        return render(request, 'demo/alumnos_edit.html', context)
    else:
        postulantes = Postulante.objects.all()
        context = {'postulantes': postulantes}
        return render(request, 'demo/alumnos_list.html', context)
    


    # Nuevas vistas del Panel de Usuario
@login_required
def estado_cuenta_apoderado(request):
    context = {"clase": "estado_cuenta_apoderado"}
    return render(request, 'panel/apoderados/estado_cuenta.html', context)

@login_required
def deposito_individual(request):
    context = {"clase": "deposito_individual"}
    return render(request, 'panel/apoderados/deposito_individual.html', context)

@login_required
def seguros_apoderado(request):
    context = {"clase": "seguros_apoderado"}
    return render(request, 'panel/apoderados/seguros.html', context)

@login_required
def progreso_meta(request):
    context = {"clase": "progreso_meta"}
    return render(request, 'panel/apoderados/progreso_meta.html', context)

@login_required
def deposito_colectivo(request):
    context = {"clase": "deposito_colectivo"}
    return render(request, 'panel/curso/deposito_colectivo.html', context)

@login_required
def reporte_financiero_curso(request):
    context = {"clase": "reporte_financiero_curso"}
    return render(request, 'panel/curso/reporte_financiero.html', context)

@login_required
def comunicacion_ejecutivo(request):
    context = {"clase": "comunicacion_ejecutivo"}
    return render(request, 'panel/curso/comunicacion.html', context)

@login_required
def gestion_contratos(request):
    context = {"clase": "gestion_contratos"}
    return render(request, 'panel/ejecutivos/gestion_contratos.html', context)

@login_required
def seguimiento_depositos(request):
    context = {"clase": "seguimiento_depositos"}
    return render(request, 'panel/ejecutivos/seguimiento_depositos.html', context)

@login_required
def informacion_seguros(request):
    context = {"clase": "informacion_seguros"}
    return render(request, 'panel/ejecutivos/informacion_seguros.html', context)



from django.shortcuts import render
from demo.models import Colegio, Curso, Alumno
from django.contrib.auth.models import User

def registro(request):
    colegios = Colegio.objects.all()
    cursos = Curso.objects.all()

    if request.method == "POST":
        # Datos básicos
        nombre = request.POST.get("nombre")
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Colegio y curso
        colegio_id = request.POST.get("colegio")
        curso_id = request.POST.get("curso")
        nuevo_colegio = request.POST.get("nuevo_colegio")

        # Alumnos
        alumnos = [
            request.POST.get("alumno_1"),
            request.POST.get("alumno_2"),
            request.POST.get("alumno_3"),
            request.POST.get("alumno_4"),
        ]
        alumnos = [alumno for alumno in alumnos if alumno]  # Filtrar nombres vacíos

        # Validaciones
        if not alumnos:
            return render(request, 'demo/registro.html', {
                'mensaje': "Debes registrar al menos un pupilo.",
                'colegios': colegios,
                'cursos': cursos
            })

        if colegio_id and nuevo_colegio:
            return render(request, 'demo/registro.html', {
                'mensaje': "Selecciona un colegio existente o agrega uno nuevo, no ambos.",
                'colegios': colegios,
                'cursos': cursos
            })

        if not colegio_id and not nuevo_colegio:
            return render(request, 'demo/registro.html', {
                'mensaje': "Selecciona un colegio existente o agrega uno nuevo.",
                'colegios': colegios,
                'cursos': cursos
            })

        # Manejo del colegio
        if nuevo_colegio:
            colegio = Colegio.objects.create(nombre=nuevo_colegio)
        else:
            try:
                colegio = Colegio.objects.get(id=colegio_id)
            except Colegio.DoesNotExist:
                return render(request, 'demo/registro.html', {
                    'mensaje': "El colegio seleccionado no existe.",
                    'colegios': colegios,
                    'cursos': cursos
                })

        # Manejo del curso
        if not curso_id:
            return render(request, 'demo/registro.html', {
                'mensaje': "Selecciona un curso.",
                'colegios': colegios,
                'cursos': cursos
            })

        try:
            curso = Curso.objects.get(id=curso_id)
        except Curso.DoesNotExist:
            return render(request, 'demo/registro.html', {
                'mensaje': "El curso seleccionado no existe.",
                'colegios': colegios,
                'cursos': cursos
            })

        # Crear usuario
        user = User.objects.create_user(username=nombre, email=email, password=password)

        # Crear alumnos
        for alumno_nombre in alumnos:
            Alumno.objects.create(nombre=alumno_nombre, curso=curso, apoderado=user)

        return render(request, 'demo/registro.html', {
            'mensaje': f"Usuario {nombre} registrado con éxito. Pupilos registrados: {len(alumnos)}.",
            'colegios': colegios,
            'cursos': cursos
        })

    return render(request, 'demo/registro.html', {'colegios': colegios, 'cursos': cursos})





from django.http import JsonResponse
from .models import Curso

def get_cursos(request, colegio_id):
    cursos = Curso.objects.filter(colegio_id=colegio_id)
    cursos_data = [{"id": curso.id, "nombre": curso.nombre} for curso in cursos]
    return JsonResponse({"cursos": cursos_data})





from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Deposito, Fondo

@login_required
def estado_cuenta(request):
    # Obtener depósitos del usuario
    depositos = Deposito.objects.filter(apoderado=request.user)
    total_apoderado = sum([deposito.monto for deposito in depositos])

    # Calcular el total colectivo para los cursos del usuario
    cursos = {deposito.curso for deposito in depositos}
    total_colectivo = sum([curso.fondo.total_colectivo for curso in cursos])

    context = {
        'depositos': depositos,
        'total_apoderado': total_apoderado,
        'total_colectivo': total_colectivo
    }
    return render(request, 'panel/apoderados/estado_cuenta.html', context)



from django.shortcuts import render, redirect
from .models import Deposito, Fondo, Curso

@login_required
def registrar_deposito(request):
    # Obtener los alumnos asociados al apoderado
    alumnos = request.user.alumnos.all()

    if not alumnos.exists():
        return render(request, 'panel/apoderados/deposito_individual.html', {'mensaje': 'No tienes alumnos registrados.'})

    if request.method == "POST":
        alumno_id = request.POST.get("alumno")
        monto = request.POST.get("monto")

        # Validar que el alumno seleccionado pertenece al apoderado
        try:
            alumno = alumnos.get(id=alumno_id)
        except Alumno.DoesNotExist:
            return render(request, 'panel/apoderados/deposito_individual.html', {
                'alumnos': alumnos,
                'mensaje': 'El alumno seleccionado no es válido.'
            })

        # Validar que el monto sea un número válido
        try:
            monto = float(monto)
        except ValueError:
            return render(request, 'panel/apoderados/deposito_individual.html', {
                'alumnos': alumnos,
                'mensaje': 'Por favor, ingresa un monto válido.'
            })

        # Obtener el curso del alumno y su fondo colectivo
        curso = alumno.curso
        fondo, created = Fondo.objects.get_or_create(curso=curso)

        # Crear el depósito
        Deposito.objects.create(apoderado=request.user, monto=monto, curso=curso)

        # Actualizar el fondo colectivo
        fondo.total_colectivo += monto
        fondo.save()

        # Redirigir con mensaje de éxito
        return redirect('estado_cuenta')

    # Renderizar el formulario con la lista de alumnos
    return render(request, 'panel/apoderados/deposito_individual.html', {'alumnos': alumnos})



@login_required
def progreso_financiero(request):
    depositos = Deposito.objects.filter(apoderado=request.user)
    total_apoderado = sum([deposito.monto for deposito in depositos])

    cursos = {deposito.curso for deposito in depositos}
    total_colectivo = sum([curso.fondo.total_colectivo for curso in cursos])

    context = {
        'total_apoderado': total_apoderado,
        'total_colectivo': total_colectivo,
    }
    return render(request, 'panel/apoderados/progreso_meta.html', context)


@login_required
def seguros_contratados(request):
    seguros = Seguro.objects.filter(apoderado=request.user)
    context = {'seguros': seguros}
    return render(request, 'panel/apoderados/seguros.html', context)