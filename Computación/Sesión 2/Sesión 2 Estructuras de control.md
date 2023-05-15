# Notas para la Sesión 2: Estructuras de control

## 1. Condicionales

### Declaración if, elif y else

Las estructuras condicionales permiten ejecutar diferentes bloques de código dependiendo de si se cumple una o varias condiciones. La sintaxis básica de una estructura condicional en Python es utilizando las palabras clave `if`, `elif` y `else`.

- `if` es seguido de una condición que se evalúa como `True` o `False`. Si la condición es verdadera, se ejecuta el bloque de código que sigue al `if`.
- `elif` es una abreviatura de "else if" y se utiliza para evaluar condiciones adicionales si las condiciones anteriores no son verdaderas.
- `else` se utiliza para ejecutar un bloque de código cuando ninguna de las condiciones anteriores es verdadera.

Ejemplo:

```python
x = 42

if x > 50:
    print("x es mayor que 50")
elif x == 50:
    print("x es igual a 50")
else:
    print("x es menor que 50")
```

### Evaluación de condiciones

Las condiciones en las estructuras `if` y `elif` pueden ser cualquier expresión que se evalúe como un valor booleano (`True` o `False`). Las condiciones pueden incluir operadores relacionales (como `==`, `!=`, `<`, `>`, `<=`, `>=`) y operadores lógicos (como `and`, `or`, `not`).

Ejemplo:

```python
age = 18
is_adult = age >= 18

if is_adult:
    print("Eres adulto")
else:
    print("Eres menor de edad")
```

## 2. Bucles y loops

Los bucles permiten ejecutar un bloque de código repetidamente mientras se cumpla una condición.

### Bucle while

Un bucle `while` ejecuta un bloque de código mientras la condición especificada sea verdadera. La condición se verifica antes de cada iteración, y si la condición es falsa, el bucle no se ejecuta.

Ejemplo:

```python
i = 0

while i < 5:
    print(i)
    i += 1
```

### Bucle for

Un bucle `for` se utiliza para iterar sobre una secuencia (como una lista, una tupla o un objeto iterable). En cada iteración, el bucle asigna el siguiente valor de la secuencia a una variable.

Ejemplo:

```python
for i in range(5):
    print(i)
```

#### Iterando sobre una lista

También podemos utilizar un bucle `for` para iterar sobre los elementos de una lista.

Ejemplo:

```python
names = ["Alice", "Bob", "Charlie"]

for name in names:
    print(name)
```

### Control de flujo: break, continue y pass

- `break`: Interrumpe un bucle y sale de él. Se utiliza cuando queremos detener la ejecución del bucle antes de que se complete la secuencia.
- `continue`: Salta a la siguiente iteración del bucle sin ejecutar el resto del bloque de código. Se utiliza para omitir ciertos elementos de la secuencia.
- `pass`: No realiza ninguna acción y se utiliza como un marcador de posición cuando la sintaxis requiere una declaración, pero no queremos ejecutar ningún código.

Ejemplo:

```python
# break
for i in range(10):
    if i == 5:
        break
    print(i)

# continue
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# pass
for i in range(10):
    if i % 2 == 0:
        pass
    else:
        print(i)
```

## 3. Ejercicios prácticos de estructuras de control

1. Crear una función que reciba un número entero e imprima si es par o impar utilizando una estructura condicional.
2. Utilizar un bucle while para calcular e imprimir la suma de los primeros 10 números naturales.
3. Utilizar un bucle for para iterar sobre una lista de números e imprimir solo los números pares.
4. Crear una función que reciba un número entero e imprima todos los números primos menores o iguales a ese número utilizando bucles y condicionales.