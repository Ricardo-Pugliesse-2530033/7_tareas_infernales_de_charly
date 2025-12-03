
"""


Nombre del estudiante : Ricardo Martin Pugliesse Macías
Matrícula             : 2530033
Grupo                 : IM 1-2

RESUMEN EJECUTIVO

Este documento presenta un programa en Python que
calcula y muestra la serie de Fibonacci hasta n
términos. La serie inicia con 0 y 1, y cada número
posterior es la suma de los dos anteriores. El
objetivo es practicar el uso de variables,
validación de entradas y bucles para generar una
secuencia numérica clásica. Se valida que n sea un
entero dentro de un rango razonable y se muestra la
serie completa en una sola línea. El programa
incluye descripción, entradas, salidas,
validaciones y casos de prueba.

PRINCIPIOS Y BUENAS PRÁCTICAS

- Validar siempre las entradas antes de usarlas en
    cálculos o bucles.
- Usar nombres de variables en inglés y claros,
    como n_terms, fibonacci_series, a, b.
- Evitar bucles infinitos controlando bien las
    condiciones de parada.
- Mantener el código legible con sangría y
    comentarios breves donde sea necesario.
- Probar el programa con varios casos de prueba,
    incluyendo valores de borde y entradas inválidas.
"""

# Problem: Fibonacci series up to n terms
"""
Description:
Implementa un programa que calcula e imprime
la serie de Fibonacci hasta n términos, donde n es
proporcionado por el usuario. La serie comienza en 0 y 1.

Inputs:
- n (int; number of terms to generate).

Outputs:
- "Fibonacci series:" <term_1> <term_2> ... <term_n>

Validations:
- n must be convertible to int.
- 1 <= n <= 50; otherwise print
    "Error: invalid input" and do not compute.

Test cases:
1) Normal: n = 5 -> Fibonacci series: 0 1 1 2 3
2) Border: n = 1 -> Fibonacci series: 0
3) Error: n = 0 or n = 60 or n = "abc" ->
     Error: invalid input
"""

n_terms_input = input("Enter the number of terms: ")
try:
	n_terms = int(n_terms_input)
	if n_terms < 1 or n_terms > 50:
		print("Error: invalid input")
		exit()
except ValueError:
	print("Error: invalid input")
	exit()

fibonacci_series = []
a = 0
b = 1
for i in range(n_terms):
	fibonacci_series.append(a)
	a, b = b, a + b

print(f"Fibonacci series: {' '.join(map(str, fibonacci_series))}")


# CONCLUSIONES
"""
Con este ejercicio practiqué cómo generar la serie
de Fibonacci usando un bucle y variables para
almacenar los términos anteriores. Validar la
entrada ayudó a evitar errores como valores
negativos o demasiado grandes. El uso de nombres en
inglés hace que el código sea más consistente con
las convenciones de programación. Además, comprobar
casos de prueba normales, de borde y de error
permite tener mayor confianza en el resultado del
programa.
"""

# REFERENCES
"""
References:
1) Python documentation - for Statements:
     https://docs.python.org/3/tutorial/controlflow.html#for-statements
2) Real Python - "Fibonacci Sequence in Python":
     https://realpython.com/fibonacci-sequence-python/
3) W3Schools - Python Loops:
     https://www.w3schools.com/python/python_for_loops.asp
4) Programiz - Python for Loop:
     https://www.programiz.com/python-programming/for-loop
5) GeeksforGeeks - Fibonacci Series in Python:
     https://www.geeksforgeeks.org/python-program-for-program-for-fibonacci-numbers/
"""

# GITHUB REPOSITORY
"""
https://github.com/Ricardo-Pugliesse-2530033/7_tareas_infernales_de_charly
"""



