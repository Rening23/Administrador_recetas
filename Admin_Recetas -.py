'''Codigo básico para crear un administrador de recetas, buscara una ruta guardada en la computadora (Windows)
leera las recetas que esten, podra crear nuevas recetas, modificar y eliminar. Parte de formaciones realizadas
en mi proceso de aprendizaje de programación usando el lenguaje Python'''

#Administrador de recetas
import os
from pathlib import Path
from os import system

ruta_principal=Path(Path.home(),"Recetas")

def Bienvenida():
    system("cls")
    print("Hola Bienvenido al administrador de recetas")

def Ruta_acceso():

    print("La ruta de acceso de las recetas es: ", ruta_principal)
def cantidad_recetas(ruta):
    contador=0
    for txt in Path(ruta).glob("**/*.txt"):
        contador+=1
    return print("La cantidad de recetas disponibles es: ", contador)
Bienvenida()
Ruta_acceso()
cantidad_recetas(ruta=ruta_principal)



def inicio():
    menu_eleccion = "x"
    while not menu_eleccion.isnumeric() or int(menu_eleccion) not in range(1, 7):
        print(""" ******Escoge una opción******
        Menu
        1) Leer recetas por categorias
        2) Crear nueva receta por categoría
        3) Crear una nueva categoría de recetas
        4) Eliminar receta por categoría
        5) Eliminar categoría de recetas
        6) Salir""")
        menu_eleccion = input("Opcion: ")
    return int(menu_eleccion)


def mostrar_categorias(ruta):
    print("Categorias: ")
    ruta_categorias= Path(ruta)
    lista_categorias=[]
    contador_categorias=1

    #se usa un metodo que se llama iterdir para que itere en cada carpeta
    for carpeta in ruta_categorias.iterdir():
        #se coloca string para que me muestre los nombres de las carpetas
        carpeta_str=str(carpeta.name)
        print(f"[{contador_categorias} - {carpeta_str}]")
        lista_categorias.append(carpeta)
        contador_categorias+=2
    return lista_categorias

def elegir_categorias(lista):
    eleccion_correcta="x"
    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1, len(lista)+1):
        eleccion_correcta= input("\n Elige una categoría: ")
    return lista[int(eleccion_correcta)-1]

def mostrar_recetas(ruta):
    print("Recetas")
    ruta_recetas=Path(ruta)
    lista_recetas=[]
    contador=1
    for receta in ruta_recetas.glob("*.txt"):
        receta_str=str(receta.name)
        print(f"[{contador}] - {receta_str}")
        lista_recetas.append(receta)
        contador+=1
    return lista_recetas

def elegir_recetas(lista):
    eleccion_receta="x"

    while not eleccion_receta.isnumeric() or int(eleccion_receta) not in range(1,len(lista)+1):
        eleccion_receta= input("\n Elije una receta: ")
    return lista[int(eleccion_receta)-1]

def leer_receta(receta):
    print(Path.read_text(receta))

def crear_receta(ruta):
    existe=False

    while not existe:
        print("Escribe el nombre de tu receta: ")
        nombre_receta= input() + ".txt"
        print("Escribe tu nueva receta: ")
        contenido_receta = input()
        ruta_nueva=Path(ruta , nombre_receta)

        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva,contenido_receta)
            print(f"Tu receta {nombre_receta} ha sido creada")
            existe=True
        else:
            print("Lo siento, esa receta ya existe")

def crear_categoria(ruta):
    existe=False

    while not existe:
        print("Escribe el nombre de la nueva categoria: ")
        nombre_categoria= input()
        ruta_nueva=Path(ruta , nombre_categoria)

        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f"Tu rnueva categoria {nombre_categoria} ha sido creada")
            existe=True
        else:
            print("Lo siento, esa categioria ya existe")

def eliminar_receta(receta):
    Path(receta).unlink()
    print(f"La receta {receta.name} ha sido eliminda")

def eliminar_categoria(categoria):
    Path(categoria).rmdir()
    print(f"La categoria {categoria.name} ha sido eliminada")

def volver_inicio():
    eleccion_regresar="x"

    while eleccion_regresar.lower() != "v":
        eleccion_regresar=input("\n Presiones V para volver al menu: ")


finalizar_programa= False
while not finalizar_programa:
    menu = inicio()
    if menu == 1:
        mis_categorias = mostrar_categorias(ruta_principal)
        mi_categoria = elegir_categorias(mis_categorias)
        mis_recetas = mostrar_recetas(mi_categoria)
        mi_receta = elegir_recetas(mis_recetas)
        leer_receta(mi_receta)
        volver_inicio()


    elif menu == 2:
        mis_categorias = mostrar_categorias(ruta_principal)
        mi_categoria = elegir_categorias(mis_categorias)
        crear_receta(mi_categoria)
        volver_inicio()

    elif menu == 3:
        crear_categoria(ruta_principal)
        volver_inicio()

    elif menu == 4:
        mis_categorias = mostrar_categorias(ruta_principal)
        mi_categoria = elegir_categorias(mis_categorias)
        mis_recetas = mostrar_recetas(mi_categoria)
        mi_receta = elegir_recetas(mis_recetas)
        eliminar_receta(mi_receta)
        volver_inicio()

    elif menu == 5:
        mis_categorias = mostrar_categorias(ruta_principal)
        mi_categoria = elegir_categorias(mis_categorias)
        eliminar_categoria(mi_categoria)
        volver_inicio()


    elif menu == 6:
        finalizar_programa = True






