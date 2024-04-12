# Conceptos básicos de Python

## Variables

# Una variable es un espacio en memoria que se utiliza para almacenar un valor.
# En Python, las variables no necesitan ser declaradas con un tipo específico
# y pueden incluso cambiar de tipo después de haber sido creadas.

# Para asignar un valor a una variable, se utiliza el operador de asignación `=`.
# Por ejemplo, para asignar el valor `5` a la variable `x`, se escribe `x = 5`.
from re import T


x = 5

# Para imprimir el valor de una variable, se utiliza la función `print`.
print(x)  # Imprime `5`

# Para cambiar el valor de una variable, simplemente se asigna un nuevo valor.
x = 10
print(x)  # Imprime `10`

# Las variables pueden ser de cualquier tipo, incluyendo números, cadenas de texto,
# listas, diccionarios, etc.
y = "Hola, mundo!"
print(y)  # Imprime `Hola, mundo!`

# Python es un lenguaje de tipado dinámico, lo que significa que el tipo de una
# variable es inferido automáticamente en tiempo de ejecución. Por ejemplo, si
# se asigna un número entero a una variable, el tipo de la variable será `int`.
# Si se asigna una cadena de texto, el tipo será `str`.
print(type(x))  # Imprime `<class 'int'>`
print(type(y))  # Imprime `<class 'str'>`

# Las variables también pueden ser asignadas a expresiones más complejas.
z = x + 3
print(z)  # Imprime `13`

# Python también soporta múltiples asignaciones en una sola línea.
a, b = 3, 4
print(a)  # Imprime `3`
print(b)  # Imprime `4`

# Las variables pueden ser reasignadas a cualquier tipo de valor, incluso a
# valores de tipos diferentes.
a = "Hola"
print(a)  # Imprime `Hola`
a = 5
print(a)  # Imprime `5`

# Las variables también pueden ser eliminadas utilizando la instrucción `del`.
del a
# print(a)  # Genera un error `NameError: name 'a' is not defined`
try:
    print(a)
except NameError as e:
    print(e)

## Booleanos

# Los booleanos son un tipo de dato que puede tener uno de dos valores: `True` o `False`.
# En Python, los booleanos se utilizan para evaluar condiciones y controlar el flujo de
# un programa.

# Los operadores de comparación se utilizan para comparar dos valores y devolver un booleano.
# Por ejemplo, el operador `==` compara si dos valores son iguales.
x = 5
y = 10
print(x == y)  # Imprime `False`

# Otros operadores de comparación son `!=` (diferente), `<` (menor que), `>` (mayor que),
print(x != y)  # Imprime `True`
print(x < y)  # Imprime `True`
print(x > y)  # Imprime `False`
print(x <= y)  # Imprime `True`
print(x >= y)  # Imprime `False`

# Los operadores lógicos se utilizan para combinar expresiones booleanas. Los operadores
# lógicos más comunes son `and` (y), `or` (o) y `not` (no).
a = True
b = False
print(a and b)  # Imprime `False`
print(a or b)  # Imprime `True`
print(not a)  # Imprime `False`

## Funciones

# Una función es un bloque de código que realiza una tarea específica. En Python,
# las funciones se definen utilizando la palabra clave `def`, seguida del nombre
# de la función y una lista de parámetros entre paréntesis. El cuerpo de la función
# está indentado y contiene las instrucciones que se ejecutarán cuando la función
# sea llamada.

# Por ejemplo, la siguiente función `saludar` imprime un mensaje de saludo.
def saludar():
    print("¡Hola, mundo!")

# Para llamar a una función, se utiliza su nombre seguido de paréntesis.
saludar()  # Imprime `¡Hola, mundo!`

# Las funciones pueden tener parámetros, que son valores que se pasan a la función
# cuando es llamada. Los parámetros se colocan entre los paréntesis de la definición
# de la función.
def saludar_a(nombre):
    print(f"¡Hola, {nombre}!")

# Al llamar a la función `saludar_a`, se debe pasar un valor para el parámetro `nombre`.
saludar_a("Juan")  # Imprime `¡Hola, Juan!`

# Las funciones pueden devolver un valor utilizando la instrucción `return`. El valor
# devuelto puede ser utilizado en otras partes del programa.
def sumar(a, b):
    return a + b

# Al llamar a la función `sumar`, se obtiene el valor devuelto por la función.
resultado = sumar(3, 4)
print(resultado)  # Imprime `7`

# Las funciones también pueden devolver múltiples valores, que se empaquetan en una tupla.
def operaciones(a, b):
    suma = a + b
    resta = a - b
    return suma, resta

# Al llamar a la función `operaciones`, se obtiene una tupla con los valores devueltos.
suma, resta = operaciones(5, 3)
print(suma)  # Imprime `8`
print(resta)  # Imprime `2`

# Las funciones pueden tener valores por defecto para sus parámetros, lo que permite
# llamar a la función sin pasar valores para esos parámetros. Si no se proporciona un
# valor para un parámetro, se utilizará el valor por defecto.
def saludar_defecto(nombre="mundo"):
    print(f"¡Hola, {nombre}!")

# Al llamar a la función `saludar_defecto` sin pasar un valor para `nombre`, se utiliza
# el valor por defecto.
saludar_defecto()  # Imprime `¡Hola, mundo!`
saludar_defecto("Juan")  # Imprime `¡Hola, Juan!`

# Las funciones pueden tener un número variable de argumentos utilizando `*args` y `**kwargs`.
# Los argumentos variables se pueden utilizar para pasar un número variable de argumentos
# a la función.
def argumentos_variables(*args, **kwargs):
    print(args)
    print(kwargs)

# Al llamar a la función `argumentos_variables`, se pueden pasar diferentes números de argumentos.
argumentos_variables(1, 2, 3)  # Imprime `(1, 2, 3)` y `{}`
argumentos_variables(a=1, b=2, c=3)  # Imprime `()` y `{'a': 1, 'b': 2, 'c': 3}`
argumentos_variables(1, 2, 3, a=1, b=2, c=3)  # Imprime `(1, 2, 3)` y `{'a': 1, 'b': 2, 'c': 3}`
argumentos_variables()  # Imprime `()` y `{}`
# argumentos_variables(a=1, b=2, 3)  # Genera un error `SyntaxError: positional argument follows keyword argument`

## Condicionales

# Los condicionales se utilizan para ejecutar cierto bloque de código si se cumple una
# condición específica. En Python, los condicionales se definen utilizando las palabras
# clave `if`, `elif` (else if) y `else`.

# Por ejemplo, el siguiente condicional imprime un mensaje si el valor de `x` es mayor que 5.
x = 10
if x > 5:
    print("x es mayor que 5")

# Los condicionales pueden tener múltiples ramas utilizando `elif` y `else`.
y = 3
if y > 5:
    print("y es mayor que 5")
elif y == 5:
    print("y es igual a 5")
else:
    print("y es menor que 5")

# Los condicionales también pueden estar anidados, es decir, un condicional puede estar
# dentro de otro condicional.
z = 7
if z > 5:
    if z < 10:
        print("z es mayor que 5 y menor que 10")
    else:
        print("z es mayor que 5 pero no es menor que 10")
else:
    print("z es menor que 5")

## Bucles

# Los bucles se utilizan para repetir un bloque de código varias veces. En Python, los
# bucles más comunes son el bucle `for` y el bucle `while`.

# El bucle `for` se utiliza para iterar sobre una secuencia de elementos, como una lista
# o una tupla. Por ejemplo, el siguiente bucle imprime los números del 1 al 5.`
for i in range(1, 6):
    print(i)

# El bucle `while` se utiliza para repetir un bloque de código mientras se cumpla una
# condición específica. Por ejemplo, el siguiente bucle imprime los números del 1 al 5.
i = 1
while i < 6:
    print(i)
    i += 1

# Los bucles pueden tener instrucciones `break` y `continue`. La instrucción `break` se
# utiliza para salir del bucle, mientras que la instrucción `continue` se utiliza para
# pasar a la siguiente iteración del bucle.
for i in range(1, 11):
    if i == 5:
        break
    print(i)  # Imprime los números del 1 al 4

for i in range(1, 6):
    if i == 3:
        continue
    print(i)  # Imprime los números 1, 2, 4, 5

## Listas

# Una lista es una colección ordenada de elementos que pueden ser de diferentes tipos.
# En Python, las listas se definen utilizando corchetes `[]` y los elementos de la lista
# se separan por comas.

# Por ejemplo, la siguiente lista contiene los números del 1 al 5.
numeros = [1, 2, 3, 4, 5]

# Las listas pueden contener elementos de diferentes tipos.
lista_mixta = [1, "dos", 3.0, True]

# Las listas pueden ser anidadas, es decir, una lista puede contener otras listas.
lista_anidada = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Los elementos de una lista se pueden acceder utilizando su índice. El índice de un
# elemento en una lista comienza en 0.
print(numeros[0])  # Imprime `1`
print(numeros[1])  # Imprime `2`
print(numeros[2])  # Imprime `3`

# Los elementos de una lista también se pueden modificar asignando un nuevo valor al
# índice correspondiente.
numeros[0] = 10
print(numeros[0])  # Imprime `10`

# Las listas tienen una longitud, que es el número de elementos que contienen. La longitud
# de una lista se puede obtener utilizando la función `len`.
print(len(numeros))  # Imprime `5`

# Las listas también pueden ser rebanadas, es decir, se pueden obtener subconjuntos de
# elementos de una lista utilizando la notación `[inicio:fin]`.
print(numeros[1:4])  # Imprime `[2, 3, 4]`

# Las listas pueden ser extendidas utilizando el método `append`, que agrega un elemento al
# final de la lista.
numeros.append(6)
print(numeros)  # Imprime `[10, 2, 3, 4, 5, 6]`

# Las listas pueden ser concatenadas utilizando el operador `+`.
otra_lista = [7, 8, 9]
concatenacion = numeros + otra_lista
print(concatenacion)  # Imprime `[10, 2, 3, 4, 5, 6, 7, 8, 9]`

## Numpy

# NumPy es una biblioteca de Python que se utiliza para trabajar con arreglos numéricos.
# NumPy proporciona una gran cantidad de funciones y operaciones para trabajar con arreglos,
# lo que lo hace muy útil para el cómputo científico.

# Para utilizar NumPy, primero es necesario importar la biblioteca.
import numpy as np



