

# Fibonacci series up to n terms


"""
Descripción:
Implementa un programa que calcule y muestre la serie de Fibonacci hasta n términos, 
donde n es ingresado por el usuario. La serie debe comenzar en 0 y 1, por lo que:

- Si n = 1 → salida: 0  
- Si n = 2 → salida: 0, 1  
- Si n = 7 → salida: 0, 1, 1, 2, 3, 5, 8  

El programa debe:
1) Leer n desde la entrada estándar.  
2) Validar n.  
3) Generar la serie de Fibonacci con un bucle (for o while).  
4) Imprimir los términos en una sola línea, separados por espacios o comas.

Entradas:
- n (int; número de términos de la serie a generar).

Salidas:
- "Number of terms:" <n> (opcional)
- "Fibonacci series:" <term_1> <term_2> ... <term_n>

Validaciones:
- n debe poder convertirse a entero.
- n >= 1.
- (Opcional) n <= 50 para evitar series demasiado grandes; si no se cumple, mostrar "Error: invalid input".
- Si la validación falla, NO calcular la serie.

Ejemplo de comportamiento esperado (no pegues el código completo, solo úsalo como referencia lógica):
- Entrada: n = 5
- Salida:
  - Fibonacci series: 0 1 1 2 3
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
    

print(f"Fibonacci series: {fibonacci_series}")