"""
PORTADA

Nombre del estudiante : Ricardo Martin Pugliesse Macías
Matrícula             : 2530033
Grupo                 : IM 1-2

RESUMEN EJECUTIVO

En este documento se resuelven seis problemas
relacionados con el uso de bucles en Python, tanto
for como while. Se aplica for cuando se conoce el
número de iteraciones (por ejemplo, recorridos de
rangos y patrones) y while cuando la repetición
depende de una condición (por ejemplo, menús e
intentos de contraseña). También se utilizan
contadores y acumuladores para sumar valores y
contar elementos, así como sentinelas para detener
la lectura repetida de datos. Cada problema incluye
descripción, entradas, salidas, validaciones y
casos de prueba, mostrando el uso seguro y
controlado de los bucles para evitar ciclos
infinitos.

PRINCIPIOS Y BUENAS PRÁCTICAS

- Usar bucles for cuando se conoce de antemano el
  número de iteraciones, como en range(1, n + 1).
- Usar bucles while cuando la cantidad de
  iteraciones depende de una condición, como leer
  hasta que el usuario escriba un sentinela o una
  opción de salida.
- Inicializar correctamente contadores y
  acumuladores antes de entrar al bucle.
- Actualizar siempre las variables de control
  dentro del while para evitar ciclos infinitos.
- Mantener el cuerpo de los bucles simple y claro;
  si la lógica es compleja, extraerla a funciones.
- Validar todas las entradas antes de procesarlas
  dentro del bucle.
"""

# Problem 1: Sum of range with for
"""
Descripción:
Calcula la suma de todos los enteros desde 1 hasta
n (incluyendo n). También calcula la suma solo de
los números pares en ese mismo rango usando un
bucle for.

Entradas:
- n (int; límite superior del rango).

Salidas:
- "Sum 1..n:" <total_sum>
- "Even sum 1..n:" <even_sum>.

Validaciones:
- Verificar que n pueda convertirse a int.
- n >= 1; de lo contrario, mostrar
	"Error: invalid input".

Casos de prueba:
1) Normal: n=5 -> Sum 1..n: 15,
	 Even sum 1..n: 6.
2) Borde: n=1 -> Sum 1..n: 1,
	 Even sum 1..n: 0.
3) Error: n=0 -> Error: invalid input.
"""
# Suma con rango
print("--- Problem 1: Sum of range with for ---")
n_text = input("Enter n (>=1): ").strip()

try:
	n = int(n_text)
except ValueError:
	print("Error: invalid input")
else:
	if n < 1:
		print("Error: invalid input")
	else:
		total_sum = 0
		even_sum = 0
		for number in range(1, n + 1):
			total_sum += number
			if number % 2 == 0:
				even_sum += number
		print(f"Sum 1..n: {total_sum}")
		print(f"Even sum 1..n: {even_sum}")


# Problem 2: Multiplication table with for
"""
Descripción:
Genera y muestra la tabla de multiplicar de un
número base desde 1 hasta m. Por ejemplo, si
base = 5 y m = 4, se imprime:
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20.

Entradas:
- base (int).
- m (int; límite de la tabla).

Salidas:
- Una línea por cada multiplicación, por ejemplo:
	- "5 x 1 = 5".
	- "5 x 2 = 10".

Validaciones:
- base y m deben poder convertirse a int.
- m >= 1; de lo contrario, mostrar
	"Error: invalid input".

Casos de prueba:
1) Normal: base=5, m=4 -> imprime 4 líneas desde
	 5 x 1 = 5 hasta 5 x 4 = 20.
2) Borde: base=3, m=1 -> imprime
	 "3 x 1 = 3".
3) Error: base=2, m=0 -> Error: invalid input.
"""
# Tabla de Multiplicar
print("\n--- Problem 2: Multiplication table with for ---")
base_text = input("Enter base: ").strip()
m_text = input("Enter table limit m (>=1): ").strip()

try:
	base = int(base_text)
	m = int(m_text)
except ValueError:
	print("Error: invalid input")
else:
	if m < 1:
		print("Error: invalid input")
	else:
		for i in range(1, m + 1):
			product = base * i
			print(f"{base} x {i} = {product}")


# Problem 3: Average of numbers with while and sentinel
"""
Descripción:
Lee números uno por uno hasta que el usuario
ingresa un valor sentinela (por ejemplo, -1).
Calcula el promedio de los números válidos
ingresados y la cantidad de datos leídos. Si el
usuario solo ingresa el sentinela, muestra un
mensaje de error.

Entradas:
- number (float; se lee repetidamente).
- sentinel_value (fijo en el código, -1.0).

Salidas:
- "Count:" <count>.
- "Average:" <average_value>.
- Si no hay datos válidos:
	- "Error: no data".

Validaciones:
- Cada lectura debe poder convertirse a float.
- Ignorar el sentinela en los cálculos.

Casos de prueba:
1) Normal: entradas 2, 4, 6, -1 -> Count: 3,
	 Average: 4.0.
2) Borde: entradas 5, -1 -> Count: 1,
	 Average: 5.0.
3) Error: solo entrada -1 -> Error: no data.
"""
# Numero sentinel 
print("\n--- Problem 3: Average of numbers with while and sentinel ---")
SENTINEL_VALUE = -1.0
total_sum = 0.0
count = 0

while True:
	number_text = input("Enter a number or -1 to finish: ").strip()
	try:
		number = float(number_text)
	except ValueError:
		print("Error: invalid input")
		continue
	if number == SENTINEL_VALUE:
		break
	total_sum += number
	count += 1

if count == 0:
	print("Error: no data")
else:
	average_value = total_sum / count
	print(f"Count: {count}")
	print(f"Average: {average_value}")


# Problem 4: Password attempts with while
"""
Descripción:
Implementa un sistema sencillo de intento de
contraseña. La contraseña correcta se define en el
código (por ejemplo, "admin123"). El usuario tiene
un número máximo de intentos para introducirla. Si
acierta dentro del límite, se muestra un mensaje de
éxito; si agota los intentos, se muestra un mensaje
de bloqueo.

Entradas:
- user_password (string; se lee en cada intento).

Salidas:
- Si acierta dentro del límite:
  - "Login success".
- Si falla todos los intentos:
  - "Account locked".

Validaciones:
- MAX_ATTEMPTS > 0 (definida como constante, 3).
- Contar correctamente los intentos.

Casos de prueba:
1) Normal: contraseña correcta en el 2.º intento ->
	Login success.
2) Borde: contraseña correcta en el 3.er intento ->
	Login success.
3) Error: todos los intentos incorrectos ->
	Account locked.
"""
# Introducir contraña
print("\n--- Problem 4: Password attempts with while ---")
CORRECT_PASSWORD = "admin123"
MAX_ATTEMPTS = 3
attempts = 0
login_success = False

while attempts < MAX_ATTEMPTS:
	user_password = input("Enter password: ")
	attempts += 1
	if user_password == CORRECT_PASSWORD:
		login_success = True
		break

if login_success:
	print("Login success")
else:
	print("Account locked")


# Problem 5: Simple menu with while
"""
Descripción:
Implementa un menú de texto sencillo que se repite
hasta que el usuario selecciona la opción de salir.
El menú es:
1) Show greeting
2) Show current counter value
3) Increment counter
0) Exit
El programa ejecuta la acción correspondiente a cada
opción y vuelve a mostrar el menú hasta que el
usuario elige 0.

Entradas:
- option (string; elección del usuario).

Salidas:
- "Hello!" para mostrar un saludo.
- "Counter:" <counter_value> para mostrar el
	contador.
- "Counter incremented" cuando se incrementa el
	contador.
- "Bye!" al salir.
- Para opciones inválidas:
	- "Error: invalid option".

Validaciones:
- Normalizar option usando strip() y conversión a
	int con manejo de error.
- Aceptar solo las opciones 0, 1, 2, 3 como
	válidas.

Casos de prueba:
1) Normal: 1, 3, 2, 0 -> muestra saludo, incrementa
	 el contador, muestra el valor y luego sale.
2) Borde: 0 -> sale inmediatamente con "Bye!".
3) Error: option = 9 -> Error: invalid option.
"""
# Simple menu While
print("\n--- Problem 5: Simple menu with while ---")

counter = 0

while True:
	print("\nMenu:")
	print("1) Show greeting")
	print("2) Show current counter value")
	print("3) Increment counter")
	print("0) Exit")
	option_text = input("Enter option: ").strip()

	try:
		option = int(option_text)
	except ValueError:
		print("Error: invalid option")
		continue

	if option == 0:
		print("Bye!")
		break
	elif option == 1:
		print("Hello!")
	elif option == 2:
		print(f"Counter: {counter}")
	elif option == 3:
		counter += 1
		print("Counter incremented")
	else:
		print("Error: invalid option")


# Problem 6: Pattern printing with nested loops
"""
Descripción:
Usa bucles for anidados para imprimir un patrón de
asteriscos en forma de triángulo rectángulo. Por
ejemplo, para n = 4:
*
**
***
****
Además, imprime un segundo patrón invertido del
mismo tamaño.

Entradas:
- n (int; número de filas del patrón).

Salidas:
- Patrón de triángulo línea por línea.
- Patrón de triángulo invertido línea por línea.

Validaciones:
- n debe poder convertirse a int.
- n >= 1; de lo contrario, mostrar
  "Error: invalid input".

Casos de prueba:
1) Normal: n=4 -> imprime 4 líneas del triángulo y
	4 líneas del triángulo invertido.
2) Borde: n=1 -> imprime "*" y luego "*" de nuevo
	invertido.
3) Error: n=0 -> Error: invalid input.
"""
# patron Astericos 
print("\n--- Problem 6: Pattern printing with nested loops ---")
n_pattern_text = input("Enter n for pattern (>=1): ").strip()

try:
	n_pattern = int(n_pattern_text)
except ValueError:
	print("Error: invalid input")
else:
	if n_pattern < 1:
		print("Error: invalid input")
	else:
		print("Triangle pattern:")
		for i in range(1, n_pattern + 1):
			print("*" * i)

		print("Inverted pattern:")
		for i in range(n_pattern, 0, -1):
			print("*" * i)


# CONCLUSIONS
"""
In this activity I practiced different uses of for
and while loops to solve real problems. The for
loop was useful when the number of iterations was
known in advance, such as summing ranges,
generating tables and printing patterns. The while
loop was more natural when the repetition depended
on user input or on a condition, like menus,
password attempts and sentinel-controlled input.
Counters and accumulators helped me to keep track
of quantities and totals, while clear exit
conditions avoided infinite loops. Nested loops
also showed how to build more complex outputs, such
as text-based patterns.
"""

# REFERENCES
"""
References:
1) Python documentation - for statements and while
   statements: https://docs.python.org/3/reference/compound_stmts.html
2) Python Tutorial - for Loops:
   https://docs.python.org/3/tutorial/controlflow.html
3) W3Schools - Python For Loops and While Loops:
   https://www.w3schools.com/python/python_for_loops.asp
4) Real Python - "Python "for" Loops":
   https://realpython.com/python-for-loop/
5) Programiz - Python while Loop:
   https://www.programiz.com/python-programming/while-loop
"""

# GITHUB REPOSITORY
"""
https://github.com/Ricardo-Pugliesse-2530033/7_tareas_infernales_de_charly
"""



