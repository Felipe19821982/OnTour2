from django.urls import path
from django.contrib.auth import views as auth_views
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('galeria', views.galeria, name='galeria'),
    path('registro', views.registro, name='registro'),
    path('perfil', views.perfil, name='perfil'),
    path('vinilo', views.vinilo, name='vinilo'),
    path('contactanos', views.contactanos, name='contactanos'),
    path('comprar', views.comprar, name='comprar'),  
    path('cassette', views.cassette, name='cassette'),   
    path('cd', views.cd, name='cd'),     
    path('pagar/', views.pagar, name='pagar'),
    path('pagoexitoso/', views.pagoexitoso, name='pagoexitoso'),      
    path('saldoinsuficiente/', views.saldoinsuficiente, name='saldoinsuficiente'), 
    path('trabaja/', views.trabaja, name='trabaja'),      
       # Ingresar
    path('listadoSQL', views.listadoSQL, name='listadoSQL'),
    path('crud/', views.crud, name='crud'),
    path('alumnosAdd/', views.alumnosAdd, name='alumnosAdd'),
    path('alumnos_del/<str:pk>/', views.alumnos_del, name='alumnos_del'),
    path('alumnos_findEdit/<str:pk>/', views.alumnos_finEdit, name='alumnos_findEdit'),
    path('alumnosUpdate/', views.alumnosUpdate, name='alumnosUpdate'),  
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

        # Nuevas páginas para el Panel de Usuario
    # Apoderados
    path('panel/apoderados/estado_cuenta/', views.estado_cuenta_apoderado, name='estado_cuenta_apoderado'),
    path('panel/apoderados/deposito_individual/', views.deposito_individual, name='deposito_individual'),
    path('panel/apoderados/seguros/', views.seguros_apoderado, name='seguros_apoderado'),
    path('panel/apoderados/progreso_meta/', views.progreso_meta, name='progreso_meta'),

    # Representantes del Curso
    path('panel/curso/deposito_colectivo/', views.deposito_colectivo, name='deposito_colectivo'),
    path('panel/curso/reporte_financiero/', views.reporte_financiero_curso, name='reporte_financiero_curso'),
    path('panel/curso/comunicacion/', views.comunicacion_ejecutivo, name='comunicacion_ejecutivo'),

    # Ejecutivos de la Agencia
    path('panel/ejecutivos/gestion_contratos/', views.gestion_contratos, name='gestion_contratos'),
    path('panel/ejecutivos/seguimiento_depositos/', views.seguimiento_depositos, name='seguimiento_depositos'),
    path('panel/ejecutivos/informacion_seguros/', views.informacion_seguros, name='informacion_seguros'),


    path('get-cursos/<int:colegio_id>/', views.get_cursos, name='get_cursos'),
]


