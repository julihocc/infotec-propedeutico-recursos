# Sesión 3: Distribuciones y visualización de datos con Matplotlib (2 horas)

## 3.1 Introducción a las distribuciones

### 3.1.1 Distribuciones discretas: binomial, geométrica, Poisson

Las **distribuciones discretas** describen la probabilidad de eventos discretos en un experimento. Ejemplos de distribuciones discretas son:

- **Distribución binomial**: describe la probabilidad de obtener un número específico de éxitos en un número fijo de ensayos independientes de Bernoulli.
- **Distribución geométrica**: describe la probabilidad de la cantidad de ensayos necesarios para obtener el primer éxito en una secuencia de ensayos independientes de Bernoulli.
- **Distribución de Poisson**: describe la probabilidad de un número específico de eventos que ocurren en un intervalo fijo de tiempo o espacio.

### 3.1.2 Distribuciones continuas: uniforme, normal, exponencial

Las **distribuciones continuas** describen la probabilidad de eventos continuos en un experimento. Ejemplos de distribuciones continuas son:

- **Distribución uniforme**: describe una distribución de probabilidad continua donde todos los valores en un intervalo tienen la misma probabilidad.
- **Distribución normal**: describe una distribución de probabilidad continua en forma de campana, donde los valores cercanos a la media tienen mayor probabilidad.
- **Distribución exponencial**: describe la distribución de tiempos entre eventos en un proceso de Poisson.

## 3.2 Estimación de parámetros

### 3.2.1 Método de los momentos

El **método de los momentos** es una técnica de estimación de parámetros que consiste en igualar los momentos de una distribución teórica a los momentos de una distribución empírica, basada en datos observados.

### 3.2.2 Método de máxima verosimilitud

El **método de máxima verosimilitud** es una técnica de estimación de parámetros que maximiza la función de verosimilitud, que es una medida de cuán probable es observar los datos dados los parámetros de la distribución.

## 3.3 Visualización de distribuciones con Matplotlib

### 3.3.1 Gráficos de función de probabilidad y función de densidad

Utilice `plt.plot` para crear gráficos de función de probabilidad (PMF) para distribuciones discretas y función de densidad (PDF) para distribuciones continuas.

```python
from scipy.stats import binom, norm

# Gráfico de función de probabilidad (PMF) para distribución binomial
n = 10
p = 0.5
x_binom = np.arange(binom.ppf(0.01, n, p), binom.ppf(0.99, n, p))
pmf_binom = binom.pmf(x_binom, n, p)

plt.plot(x_binom, pmf_binom, "bo", ms=8)
plt.title("Función de probabilidad (PMF) - Distribución binomial")
plt.xlabel("Valores")
plt.ylabel("Probabilidad")
plt.show()

# Gráfico de función de densidad (PDF) para distribución normal
mu = 0
sigma = 1
x_norm = np.linspace(norm.ppf(0.01, mu, sigma), norm.ppf(0.99, mu, sigma), 100)
pdf_norm = norm.pdf(x_norm, mu, sigma)

plt.plot(x_norm, pdf_norm, "r-", lw=5)
plt.title("Función de densidad (PDF) - Distribución normal")
plt.xlabel("Valores")
plt.ylabel("Densidad")
plt.show()
```

### 3.3.2 Gráficos de función de distribución acumulativa

Utilice `plt.plot` para crear gráficos de función de distribución acumulativa (CDF) tanto para distribuciones discretas como continuas.

```python
# Gráfico de función de distribución acumulativa (CDF) para distribución binomial
cdf_binom = binom.cdf(x_binom, n, p)

plt.plot(x_binom, cdf_binom, "bo", ms=8)
plt.title("Función de distribución acumulativa (CDF) - Distribución binomial")
plt.xlabel("Valores")
plt.ylabel("Probabilidad acumulada")
plt.show()

# Gráfico de función de distribución acumulativa (CDF) para distribución normal
cdf_norm = norm.cdf(x_norm, mu, sigma)

plt.plot(x_norm, cdf_norm, "r-", lw=5)
plt.title("Función de distribución acumulativa (CDF) - Distribución normal")
plt.xlabel("Valores")
plt.ylabel("Probabilidad acumulada")
plt.show()
```

### 3.3.3 Comparación de distribuciones y ajuste de datos

Utilice las funciones de scipy.stats para ajustar los parámetros de una distribución teórica a los datos observados y comparar las distribuciones utilizando gráficos y medidas de bondad de ajuste.

```python
from scipy.stats import kstest

# Generar datos aleatorios y ajustar a una distribución normal
data = np.random.normal(loc=5, scale=2, size=1000)
mu_fit, sigma_fit = norm.fit(data)

# Comparar la distribución empírica con la distribución teórica
x_empirical = np.sort(data)
cdf_empirical = np.arange(1, len(x_empirical) + 1) / len(x_empirical)
cdf_theoretical = norm.cdf(x_empirical, mu_fit, sigma_fit)

plt.plot(x_empirical, cdf_empirical, label="Empírica")
plt.plot(x_empirical, cdf_theoretical, label="Teórica")
plt.title("Comparación de distribuciones")
plt.xlabel("Valores")
plt.ylabel("Probabilidad acumulada")
plt.legend()
plt.show()

# Prueba de bondad de ajuste (Kolmogorov-Smirnov)
statistic, p_value = kstest(data, "norm", args=(mu_fit, sigma_fit))
print("Estadístico de prueba:", statistic)
print("Valor p:", p_value)
```

El resultado del test Kolmogorov-Smirnov (estadístico de prueba y valor p) nos ayuda a evaluar qué tan bien se ajusta la distribución teórica a los datos observados.

## 3.4 Ejercicios prácticos con Python y Matplotlib

1. Genere un conjunto de datos aleatorios siguiendo una distribución binomial con `n = 20` y `p = 0.3`. Grafique la función de probabilidad y la función de distribución acumulativa utilizando Matplotlib.
2. A partir de un conjunto de datos de edades de un grupo de personas, calcule las medidas de tendencia central (media, mediana, moda) y las medidas de dispersión (rango, varianza, desviación estándar). Visualice estos datos utilizando un histograma y un gráfico de caja y bigotes.
3. Genere un conjunto de datos aleatorios siguiendo una distribución exponencial con una tasa de `lambda = 0.5`. Ajuste los datos a una distribución exponencial y compare la distribución empírica con la distribución teórica utilizando un gráfico de función de distribución acumulativa y la prueba Kolmogorov-Smirnov.
