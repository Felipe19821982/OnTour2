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



from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Colegio, Curso, Alumno
from django.contrib.auth.models import User
from django.contrib import messages

def registro(request):
    colegios = Colegio.objects.all()

    if request.method == "POST":
        nombre = request.POST.get("nombre")
        email = request.POST.get("email")
        password = request.POST.get("password")
        colegio_id = request.POST.get("colegio")
        curso_id = request.POST.get("curso")

        # Validaciones
        if not nombre or not email or not password or not colegio_id or not curso_id:
            messages.error(request, "Todos los campos son obligatorios.")
            return render(request, 'demo/registro.html', {'colegios': colegios})

        try:
            # Crear usuario
            user = User.objects.create_user(username=nombre, email=email, password=password)

            # Asociar curso y alumnos
            curso = Curso.objects.get(id=curso_id)
            for i in range(1, 5):
                alumno_nombre = request.POST.get(f"alumno_{i}")
                if alumno_nombre:
                    Alumno.objects.create(nombre=alumno_nombre, curso=curso, apoderado=user)

            messages.success(request, "Registro completado con éxito.")
            return redirect('registro')

        except Exception as e:
            messages.error(request, f"Error durante el registro: {e}")

    return render(request, 'demo/registro.html', {'colegios': colegios})


def get_cursos(request, colegio_id):
    try:
        cursos = Curso.objects.filter(colegio_id=colegio_id)
        cursos_data = [{"id": curso.id, "nombre": curso.nombre} for curso in cursos]
        return JsonResponse({"cursos": cursos_data})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)



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








@login_required
def estado_cuenta(request):
    # Obtener depósitos del usuario
    depositos = Deposito.objects.filter(apoderado=request.user)
    total_apoderado = sum([deposito.monto for deposito in depositos])

    # Calcular el total colectivo para los cursos del usuario
    cursos = {deposito.curso for deposito in depositos}
    total_colectivo = sum([curso.fondo.total_colectivo for curso in cursos])

    # Definir metas
    meta_curso = 11250000
    meta_individual = 450000

    # Calcular saldos
    saldo_curso = meta_curso - total_colectivo
    saldo_individual = meta_individual - total_apoderado

    context = {
        'depositos': depositos,
        'total_apoderado': total_apoderado,
        'total_colectivo': total_colectivo,
        'meta_curso': meta_curso,
        'meta_individual': meta_individual,
        'saldo_curso': saldo_curso,
        'saldo_individual': saldo_individual,
    }
    return render(request, 'panel/apoderados/estado_cuenta.html', context)







from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Seguro
from .forms import SeguroForm

# Verificar si el usuario es administrador
def is_admin(user):
    return user.is_superuser

@login_required
def listar_seguros(request):
    seguros = Seguro.objects.all()
    return render(request, 'panel/apoderados/seguros.html', {'seguros': seguros})

@user_passes_test(is_admin)
@login_required
def agregar_seguro(request):
    if request.method == 'POST':
        form = SeguroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_seguros')
    else:
        form = SeguroForm()
    return render(request, 'panel/administradores/agregar_seguro.html', {'form': form})





from django.shortcuts import render, redirect
from .models import Mensaje  # Modelo para almacenar mensajes
from django.utils.timezone import now

@login_required
def comunicacion_ejecutivo(request):
    if request.method == "POST":
        asunto = request.POST.get("asunto")
        contenido = request.POST.get("mensaje")
        
        # Guardar mensaje en la base de datos
        Mensaje.objects.create(
            asunto=asunto,
            contenido=contenido,
            usuario=request.user,
            fecha=now()
        )
        return redirect('comunicacion_ejecutivo')
    
    # Obtener historial de mensajes
    mensajes = Mensaje.objects.filter(usuario=request.user).order_by('-fecha')
    return render(request, 'panel/curso/comunicacion.html', {'mensajes': mensajes})



from django.contrib import messages

@login_required
def deposito_colectivo(request):
    if request.method == "POST":
        colegio_id = request.POST.get("colegio")
        curso_id = request.POST.get("curso")
        monto = request.POST.get("monto")
        descripcion = request.POST.get("descripcion")

        try:
            curso = Curso.objects.get(id=curso_id, colegio_id=colegio_id)
            Deposito.objects.create(curso=curso, monto=monto, descripcion=descripcion or "")
            messages.success(request, "Depósito registrado exitosamente.")
        except Curso.DoesNotExist:
            messages.error(request, "El curso seleccionado no existe.")
        except Exception as e:
            messages.error(request, f"Error al registrar el depósito: {str(e)}")
        return redirect('deposito_colectivo')

    colegios = Colegio.objects.all()
    depositos = Deposito.objects.filter(curso__isnull=False).order_by('-fecha')
    return render(request, 'panel/curso/deposito_colectivo.html', {
        'colegios': colegios,
        'depositos': depositos
    })



from django.shortcuts import render

def reporte_financiero(request):
    total_recaudado = 7500000  # Ejemplo, ajusta según los datos reales
    meta_curso = 11250000
    saldo_pendiente = meta_curso - total_recaudado

    context = {
        'total_recaudado': total_recaudado,
        'meta_curso': meta_curso,
        'saldo_pendiente': saldo_pendiente,
    }
    return render(request, 'panel/curso/reporte_financiero.html', context)
