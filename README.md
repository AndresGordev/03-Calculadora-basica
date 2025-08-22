# Calculadora que resuelve operaciones basicas entre dos números que el usuario elija.

Programa realizado en Python que resuelve las operaciones basicas mediante los dos numeros que el usuario ingresa, a traves de las indicaciones que se le muestran.
Desarrollado como proyecto sencillo pero funcional, con enfoque en la validacion de entradas, operaciones aritmeticas de los numeros ingresados, asi como en la claridad del codigo.

------

## ¿Que hace?

- Le muestra al usuario un menú con las cuatro opciones que representan las operaciones basicas.
- Una vez que el usuario haya elegido una operacion, se le solicita un primer número.
- Se le solicita al usuario un segundo número.
- Para cada número solicitado, se verifica que el campo no se deje vacio.
- Para cada número ingresado, se verifica que sea un digito y no un caracter o letra.
- Se verifica que el número ingresado se encuentre dentro del rango establecido por su respectiva indicación (1-4 para el menu).
- Se verifica que el número ingresado sea positivo asegurando su uso correcto en las operaciones aritmeticas.
- Se muestra el resultado de la operacion aritmetica elegida.
- Se muestra la indicacion para volver al menu principal y poder elegir una nueva operacion.

El desarrollo del programa esta enfocado en un flujo robusto, anticipando los errores comunes del usuario.

## Ejemplo de salida

""" ************************************************************
                        MULTIPLICACIÓN
************************************************************
Ingresa un primer número entero: 60
Ingresa un segundo número entero: 35
------------------------------------------------------------


** La multiplicación de 60 * 35 es: 2100 ** 

Presiona Enter para volver al menú: """

## Tecnologia Usada

- Python 3.
- Programacion orientada a procedimientos. 
- Validacion de entrada de usuario.
- Operaciones aritmeticas basicas.
- Flujo controlado por funciones.

## Estructura del codigo

- Descripcion del programa.
- Bloque de verificaciones independientes iniciales.
- Bloque de separadores visuales del programa.
- Bloque de mensajes que el programa mostrara.
- Bloque de encabezados para cada operacion.
- Bloque de mensajes que conforman al menu.
- Funciones que solicitan el primero y segundo numero.
- Bloque de funciones que realizan las operaciones aritmeticas basicas.
- Bloque de funciones que verifican al primero y segundo numero ingresado.
- Funcion que verifica el numero de opcion elegida en el menu.
- Funcion que asigna este numero a cada operacion aritmetica correspondiente.
- Bloque de la logica principal, en la que se llama a las funciones previamente mencionadas para el desarrollo del programa.
