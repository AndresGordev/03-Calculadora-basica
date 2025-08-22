"""Programa que ejecuta una calculadora con las operaciones basicas entre los numeros enteros que elija el usuario."""

import os

#**** Bloque de verificaciones independientes *****

# Función que verifica si el dato ingresado por el usuario es igual a una cadena vacia.
# Esta función verifica que el usuario no haya dejado el campo vacio.
def campo_vacio(numero):
    if numero.strip() == "":
        return True
# Función que verifica  que el dato ingresado por el usuario sea un digito y no una letra o caracter.
# Esta función utiliza el metodo isdigit() para devolver un valor booleano verdadero si esta condicion de cumple.
def numero_digito(numero):
    if numero.isdigit():
        return True
# Función que verifica si el dato ingresado por el usuario se encuentra dentro del rango de opciones del menú.
# Esta función verifica que, el dato ingresado no sea menor que 0 o mayor que 4.
def fuera_rango(numero):
    if int(numero) <= 0 or int(numero) > 4:
        return True 
# Función que verifica que el dato ingresado por el usuario sea mayor que cero para su posterior proceso en el programa.
def menor_que_cero(numero):
    if int(numero) <= 0:
        return True
# ----------------------------------------------------------------------------------------------------------------------

#***** Bloque de separadores visuales para el programa ******

def espacio():
    print("\n")

def separador():
    print("-" * 60)
# --------------------------------------------------------------

#***** Bloque de mensajes correspondientes que mostrara el programa ******

def mensaje_campo_vacio():
    print("No se debe dejar el campo vacio. Intentalo de nuevo...")

def mensaje_no_digito():
    print("Debes ingrear solo números enteros. Intentalo de nuevo...")

def mensaje_fuera_rango():
    print("Número no valido. Intentalo de nuevo...")
# ------------------------------------------------------------------------

#***** Encabezados correspondientes que mostrara el programa *****

def mensaje_suma():
    print("*" * 60)
    print("                         SUMA          ")
    print("*" * 60)

def mensaje_resta():
    print("*" * 60)
    print("                         RESTA           ")
    print("*" * 60)

def mensaje_multiplicacion():
    print("*" * 60)
    print("                         MULTIPLICACIÓN          ")
    print("*" * 60)

def mensaje_division():
    print("*" * 60)
    print("                         DIVISIÓN           ")
    print("*" * 60)

def encabezado():
    print("*" * 60)
    print("                         Calculadora           ")
    print("*" * 60)
# -------------------------------------------------------------------------

#****** Mensajes que componen al menu *****

def mensaje_menu():
    print("Lee con atencion las siguientes opciones: \n")

def opcion():
    return input("Selecciona una opcion: ")

def menu():
    mensaje_menu()    
    print("""                [1] Sumar 
                [2] Restar
                [3] Multiplicar
                [4] Dividir\n""")
# ------------------------------------------

#***** Funciones que solicitan el primero y segundo numero ******

def primer_numero():
    return input("Ingresa un primer numero entero: ")

def segundo_numero():
    return input("Ingresa un segundo numero entero: ")
#-----------------------------------------------------------------

    
#***** Bloque de funciones que realizan las operaciones basicas de la calculadora. *****

# En cada una de las funciones, se ingresan los dos numeros que previamente se solicitaron.
# Según la operacion, el resultado se guarda en la variable llamada "Resultado".
# finalmente, esta variable, se retorna para su posterior uso.
def sumar(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

def restar(numero1, numero2):
    resultado = numero1 - numero2
    return resultado

def multiplicar(numero1, numero2):
    resultado = numero1 * numero2
    return resultado

def division(numero1, numero2):
    resultado = numero1 / numero2
    return resultado
# --------------------------------------------------------------------------------------

#***** Funciónes que realizan la verificación del primer y segundo número. ******

# Se verifica que el campo no se haya dejado vacio.
# Se verifica que el dato ingresado sea un digito y no una letra o caracter.
# Se verificaa que el dato ingresado se sea mayor que cero.
def verificacion_primer_numero():
    incorrecto = True
    while incorrecto:
        numero1 = primer_numero()
        if campo_vacio(numero1):
            mensaje_campo_vacio()
        elif not numero_digito(numero1):
            mensaje_no_digito()
        elif menor_que_cero(numero1):
            mensaje_fuera_rango()
        else:
            numero1 = int(numero1)
            incorrecto = False
    return numero1
# Se realizan las mismas verificaciones para el segundo número.
def verificacion_segundo_numero():
    incorrecto = True
    while incorrecto:
        numero2 = segundo_numero()
        if campo_vacio(numero2):
            mensaje_campo_vacio()
        elif not numero_digito(numero2):
            mensaje_no_digito()
        elif menor_que_cero(numero2):
            mensaje_fuera_rango()
        else:
            numero2 = int(numero2)
            incorrecto = False
    return numero2
# -------------------------------------------------------------------------------------

# ****** Funcion que verifica el numero ingresado por el usuario, pero ahora desde el menú ******

# Se verifica que el campo no se deje vacio.
# Se verifica que el numero ingresado sea un digito y no una letra o caracter.
# Se veerifica que el numero ingresado se encuentre dentro del rango de opciones del menu, es decir, del 1 al 4.
def verificacion_eleccion():
    incorrecto = True
    while incorrecto:
        opcion_elegida = opcion()
        if campo_vacio(opcion_elegida):
            mensaje_campo_vacio()
        elif not numero_digito(opcion_elegida):
            mensaje_no_digito()
        elif fuera_rango(opcion_elegida):
            mensaje_fuera_rango()
        else:
            incorrecto = False
            return opcion_elegida
# ----------------------------------------------------------------------------------------------

# ***** Funcion que asigna el numero ingresado del usuario a cada una de las opciones que muestra el menu. *****

# En cada una de las opciones, se realizan las siguientes acciones:
# Se limpia la pantalla.
# Se muestra el encabezado correspondiente a la operacion elegida.
# Se solicita el primer numero.
# Se solicita el segundo numero.
# Se almacena el resultado de la operacion.
# Se muestra un separador formado por guiones.
# Se realiza un salto de linea como espacio.
# Finalmente se muestra el resultado de la operacion mediante una cadena literal.
def eleccion_menu(opcion_elegida):
    opcion = int(opcion_elegida)
    if opcion == 1:
        os.system("cls")
        mensaje_suma()
        numero1 = verificacion_primer_numero()
        numero2 = verificacion_segundo_numero()
        resultado = sumar(numero1,numero2)   
        separador()
        espacio()
        print(f"** La suma de {numero1} + {numero2} es: {resultado} ** \n") 
    elif opcion == 2:
        os.system("cls")
        mensaje_resta()
        numero1 = verificacion_primer_numero()
        numero2 = verificacion_segundo_numero()
        resultado = restar(numero1, numero2)
        separador()
        espacio()
        print(f"** La resta de {numero1} - {numero2} es: {resultado} ** \n")   
    elif opcion == 3:
        os.system("cls")
        mensaje_multiplicacion()
        numero1 = verificacion_primer_numero()
        numero2 = verificacion_segundo_numero()
        resultado = multiplicar(numero1,numero2)
        separador()
        espacio()
        print(f"** La multiplicación de {numero1} * {numero2} es: {resultado} ** \n")
    elif opcion == 4:
        os.system("cls")
        mensaje_division()
        numero1 = verificacion_primer_numero()
        numero2 = verificacion_segundo_numero()
        resultado = division(numero1, numero2)
        separador()
        espacio()
        print(f"** La división entre {numero1} / {numero2} es: {resultado} ** \n")
#----------------------------------------------------------------------------------------------------------------
        

# ***** Bloque de la logica principal *****

# Se muestra el encabezado descriptivo del programa.
# Se muestra el menu.
# Se almacena el numero ingresado y ya verificado.
# Se asigna el numero ingresado por el usuario a la opcion del menu correspondiente.
# Se le indica al usuario que presione "Enter" para volver al menu.
# Se limpia la pantalla para mostrar nuevamente el menu.
# Mediante el bucle while, siempre que se presione "Enter", el programa te llevara al menu principal.
volver = True
while volver:
    encabezado()
    menu()
    opcion_elegida = verificacion_eleccion()
    eleccion_menu(opcion_elegida)
    pregunta = input("Presiona Enter para volver al menú: ")
    os.system("cls")