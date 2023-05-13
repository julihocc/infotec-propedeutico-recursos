# Sesión 1: Probabilidad (2 horas)

## 1.1 Introducción a la probabilidad

### 1.1.1 Conceptos básicos: eventos, espacio muestral, probabilidad

La **probabilidad** es una medida de la incertidumbre asociada a un evento o suceso. Se utiliza para cuantificar qué tan probable es que ocurra un evento en un conjunto de posibles resultados. En términos matemáticos, un **evento** es un subconjunto del **espacio muestral**, el cual contiene todos los posibles resultados de un experimento aleatorio. La probabilidad de un evento se representa como $P(A)$, donde $A$ es el evento de interés.

```python
# Ejemplo: lanzar una moneda
espacio_muestral = {"cara", "cruz"}

evento_A = {"cara"}

P_A = 1 / len(espacio_muestral)
print("Probabilidad de que salga cara:", P_A)
```

### 1.1.2 Axiomas de probabilidad

Los axiomas de probabilidad son tres reglas fundamentales que deben cumplir las medidas de probabilidad:

1. La probabilidad de cualquier evento $A$ es un número no negativo: $P(A) \ge 0$.
2. La probabilidad del espacio muestral es igual a 1: $P(S) = 1$, donde $S$ es el espacio muestral.
3. Si $A_1, A_2, A_3, ...$ son eventos mutuamente excluyentes (no pueden ocurrir al mismo tiempo), entonces la probabilidad de que ocurra al menos uno de ellos es igual a la suma de sus probabilidades individuales: $P(A_1 \cup A_2 \cup A_3 \cup ...) = P(A_1) + P(A_2) + P(A_3) + ...$

### 1.1.3 Probabilidad condicional e independencia

La **probabilidad condicional** es la probabilidad de que ocurra un evento $A$ dado que otro evento $B$ ha ocurrido. Se representa como $P(A|B)$, y se calcula de la siguiente manera:

$$
P(A|B) = \frac{P(A \cap B)}{P(B)}
$$

Dos eventos $A$ y $B$ son **independientes** si la ocurrencia de uno de ellos no afecta la probabilidad del otro. En términos matemáticos, $A$ y $B$ son independientes si:

$$
P(A|B) = P(A) \text{ o } P(B|A) = P(B)
$$

## 1.2 Teorema de Bayes

El teorema de Bayes es una fórmula que relaciona la probabilidad condicional de dos eventos. Es especialmente útil cuando se busca actualizar una probabilidad inicial (a priori) con nueva información (evidencia). El teorema de Bayes se expresa como:

$$
P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}
$$

## 1.3 Variables aleatorias

Una **variable aleatoria** es una función que asigna un valor numérico a cada resultado en el espacio muestral. Las variables aleatorias pueden ser **discretas** (valores contables) o **continuas** (valores en un intervalo).

### 1.3.1 Variables aleatorias discretas y continuas

- **Variables aleatorias discretas**: son aquellas cuyos valores posibles forman un conjunto finito o contable. Ejemplo: número de caras al lanzar dos monedas.
- **Variables aleatorias continuas**: son aquellas cuyos valores posibles están en un intervalo continuo (infinitos). Ejemplo: tiempo que tarda en llegar un autobús.

### 1.3.2 Función de probabilidad y función de densidad

- **Función de probabilidad (PMF)**: se aplica a variables aleatorias discretas y asigna una probabilidad a cada valor posible de la variable. La suma de todas las probabilidades es igual a 1.

- **Función de densidad (PDF)**: se aplica a variables aleatorias continuas y describe la probabilidad relativa de cada valor en el intervalo continuo. La integral de la función de densidad sobre todo el intervalo es igual a 1.

### 1.3.3 Función de distribución acumulativa (CDF)

La **función de distribución acumulativa (CDF)** es una función que describe la probabilidad de que una variable aleatoria tome un valor menor o igual a un valor específico. Para variables aleatorias discretas, se calcula como la suma de las probabilidades de todos los valores menores o iguales al valor específico. Para variables aleatorias continuas, se calcula como la integral de la función de densidad hasta el valor específico.

## 1.4 Esperanza matemática y varianza

La **esperanza matemática** (también conocida como valor esperado o media) es una medida de tendencia central que representa el valor promedio de una variable aleatoria. Se calcula como la suma ponderada de los valores posibles, donde los pesos son las probabilidades de los valores.

$$
E(X) = \sum_{i} x_i \cdot P(x_i)
$$

La **varianza** es una medida de dispersión que representa la variabilidad de una variable aleatoria. Se calcula como el promedio de las diferencias al cuadrado entre los valores posibles y la media.

$$
Var(X) = E((X - E(X))^2) = \sum_{i} (x_i - E(X))^2 \cdot P(x_i)
$$

## 1.5 Ejercicios prácticos propuestos

1. Considere un experimento donde se lanza un dado equilibrado de 6 caras. Calcule la función de probabilidad (PMF), la función de distribución acumulativa (CDF), la esperanza y la varianza para la variable aleatoria que representa el número que aparece en el dado.

2. Imagine que la altura de los estudiantes en una universidad sigue una distribución normal con una media de 170 cm y una desviación estándar de 10 cm. Utilice la función de densidad (PDF) y la función de distribución acumulativa (CDF) para responder las siguientes preguntas:

   a. ¿Cuál es la probabilidad de que un estudiante tenga una altura de exactamente 180 cm?
   
   b. ¿Cuál es la probabilidad de que un estudiante tenga una altura menor o igual a 160 cm?
   
   c. ¿Cuál es la probabilidad de que un estudiante tenga una altura entre 150 cm y 190 cm?

3. Suponga que la cantidad de mensajes de texto enviados por una persona en un día sigue una distribución de Poisson con una tasa promedio de 10 mensajes por día. Calcule la función de probabilidad (PMF), la función de distribución acumulativa (CDF), la esperanza y la varianza para la variable aleatoria que representa la cantidad de mensajes enviados en un día.