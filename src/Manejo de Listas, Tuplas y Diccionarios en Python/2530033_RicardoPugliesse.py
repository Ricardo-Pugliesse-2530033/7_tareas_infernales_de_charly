
"""
PORTADA

Nombre: Ricardo Martin Pugliesse Macías
Matrícula             : 2530033
Grupo                 : IM 1-2


RESUMEN EJECUTIVO

En Python, las listas, tuplas y diccionarios son
estructuras fundamentales para trabajar con
colecciones de datos. Las listas son ordenadas y
mutables, por lo que permiten agregar, eliminar o
modificar elementos con facilidad. Las tuplas son
ordenadas pero inmutables, ideales para datos fijos
como coordenadas o configuraciones. Los diccionarios
almacenan pares clave-valor y permiten búsquedas
rápidas por clave, lo que resulta muy útil en
catálogos y registros. Este documento presenta seis
problemas prácticos con descripción, entradas,
salidas, validaciones y casos de prueba, mostrando
el uso de listas, tuplas y diccionarios en contextos
reales.


PRINCIPIOS Y BUENAS PRÁCTICAS

- Usar listas cuando se necesite agregar o eliminar
    elementos con frecuencia.
- Usar tuplas para datos que no deben cambiar, como
    coordenadas, fechas o configuraciones fijas.
- Usar diccionarios cuando se requiera buscar
    información por una clave (por ejemplo, nombre,
    id o código).
- Evitar modificar una lista mientras se recorre con
    un for, a menos que se tenga claro el efecto.
- Usar nombres de claves descriptivos en los
    diccionarios (por ejemplo, "name", "age",
    "price").
- Escribir código legible y mensajes claros para el
    usuario, manteniendo las variables y salidas en
    inglés según la consigna.
"""

# Problem 1: Shopping list basics (list operations)
"""
Descripción:
Trabaja con una lista de productos (strings). El
programa: 1) crea una lista inicial de productos,
2) permite agregar un nuevo producto al final,
3) muestra la cantidad total de elementos en la
lista y 4) verifica si un producto específico está
en la lista mediante un booleano is_in_list.

Entradas:
- initial_items_text (string; por ejemplo,
    "apple,banana,orange").
- new_item (string; producto a agregar).
- search_item (string; producto a buscar).

Salidas:
- "Items list:" <items_list>.
- "Total items:" <len_list>.
- "Found item:" true|false.

Validaciones:
- initial_items_text no debe estar vacío después de
    strip().
- Separar la cadena por comas y eliminar espacios
    extra en cada elemento.
- new_item y search_item no deben estar vacíos.
- Se puede manejar el caso de lista inicial vacía
    (como se documenta en el código).

Casos de prueba:
1) Normal: initial_items_text="apple,banana,orange",
     new_item="grape", search_item="banana" ->
     Items list: ['apple', 'banana', 'orange',
     'grape'], Total items: 4, Found item: true.
2) Borde: initial_items_text="", new_item="apple",
     search_item="apple" -> Items list: ['apple'],
     Total items: 1, Found item: true.
3) Error: initial_items_text="apple,banana",
     new_item="", search_item="banana" ->
     Error: invalid input.
"""
def problem1():
    print("--- Problem 1: Shopping list basics (list operations) ---")
    initial_items_text = input("Enter initial items (comma separated): ").strip()
    new_item = input("Enter new item to add: ").strip()
    search_item = input("Enter item to search: ").strip()

    if new_item == "" or search_item == "":
        print("Error: invalid input")
        return

    items_list = [item.strip() for item in initial_items_text.split(",") if item.strip()] if initial_items_text else []
    items_list.append(new_item)
    len_list = len(items_list)
    is_in_list = search_item in items_list

    print(f"Items list: {items_list}")
    print(f"Total items: {len_list}")
    print(f"Found item: {str(is_in_list).lower()}")

problem1()

# Problem 2: Points and distances with tuples
"""
Descripción:
Usa tuplas para representar dos puntos en un plano
2D: (x1, y1) y (x2, y2). El programa calcula la
distancia euclidiana entre ambos puntos y el punto
medio (midpoint) entre ellos.

Entradas:
- x1, y1, x2, y2 (float; coordenadas de los
  puntos).

Salidas:
- "Point A:" (x1, y1).
- "Point B:" (x2, y2).
- "Distance:" <distance>.
- "Midpoint:" (mx, my).

Validaciones:
- Las cuatro entradas deben poder convertirse a
  float.

Casos de prueba:
1) Normal: x1=0, y1=0, x2=3, y2=4 -> Point A:
    (0.0, 0.0), Point B: (3.0, 4.0), Distance:
    5.0, Midpoint: (1.5, 2.0).
2) Borde: x1=1, y1=1, x2=1, y2=1 -> Distance:
    0.0, Midpoint: (1.0, 1.0).
3) Error: x1="a", y1=0, x2=3, y2=4 ->
    Error: invalid input.
"""
def problem2():
    print("\n--- Problem 2: Points and distances with tuples ---")
    try:
        x1 = float(input("Enter x1: "))
        y1 = float(input("Enter y1: "))
        x2 = float(input("Enter x2: "))
        y2 = float(input("Enter y2: "))
    except ValueError:
        print("Error: invalid input")
        return

    point_a = (x1, y1)
    point_b = (x2, y2)
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    midpoint = ((x1 + x2)/2, (y1 + y2)/2)

    print(f"Point A: {point_a}")
    print(f"Point B: {point_b}")
    print(f"Distance: {distance}")
    print(f"Midpoint: {midpoint}")

problem2()

# Problem 3: Product catalog with dictionary
"""
Descripción:
Administra un catálogo de productos usando un
diccionario (nombre del producto -> precio por
unidad). Calcula el precio total para un producto
determinado y una cantidad dada.

Entradas:
- product_name (string).
- quantity (int).

Salidas:
- Si el producto existe:
    - "Unit price:" <unit_price>
    - "Quantity:" <quantity>
    - "Total:" <total_price>
- Si no existe:
    - "Error: product not found".

Validaciones:
- quantity > 0.
- product_name no debe estar vacío después de
    aplicar strip().
- Verificar que product_name esté en el
    diccionario.

Casos de prueba:
1) Normal: product_name="apple", quantity=2 ->
     Unit price: 10.0, Quantity: 2, Total: 20.0.
2) Borde: product_name="banana", quantity=1 ->
     Unit price: 5.0, Quantity: 1, Total: 5.0.
3) Error: product_name="pear", quantity=2 ->
     Error: product not found.
"""
def problem3():
    print("\n--- Problem 3: Product catalog with dictionary ---")
    product_prices = {"apple": 10.0, "banana": 5.0, "orange": 8.0}
    product_name = input("Enter product name: ").strip()
    quantity_str = input("Enter quantity: ").strip()

    if product_name == "":
        print("Error: invalid input")
        return
    try:
        quantity = int(quantity_str)
    except ValueError:
        print("Error: invalid input")
        return
    if quantity <= 0:
        print("Error: invalid input")
        return
    if product_name not in product_prices:
        print("Error: product not found")
        return
    unit_price = product_prices[product_name]
    total_price = unit_price * quantity
    print(f"Unit price: {unit_price}")
    print(f"Quantity: {quantity}")
    print(f"Total: {total_price}")

problem3()

# Problem 4: Student grades with dict and list
"""
Descripción:
Administra calificaciones de estudiantes usando un
diccionario (student name -> lista de calificaciones).
Calcula el promedio y el estado de aprobación.

Entradas:
- student_name (string).

Salidas:
- Si el estudiante existe:
    - "Grades:" <grades_list>.
    - "Average:" <average>.
    - "Passed:" true|false.
- Si no existe:
    - "Error: student not found".

Validaciones:
- student_name no debe estar vacío después de
    aplicar strip().
- Verificar que student_name sea una clave en el
    diccionario.
- Verificar que la lista de calificaciones no esté
    vacía antes de calcular el promedio.

Casos de prueba:
1) Normal: student_name="Alice" -> Grades:
     [90, 85, 80], Average: 85.0, Passed: true.
2) Borde: student_name="Bob" -> Grades: [70],
     Average: 70.0, Passed: true.
3) Error: student_name="Eve" ->
     Error: student not found.
"""
def problem4():
    print("\n--- Problem 4: Student grades with dict and list ---")
    grades = {"Alice": [90, 85, 80], "Bob": [70], "Charlie": [60, 65, 68]}
    student_name = input("Enter student name: ").strip()
    if student_name == "":
        print("Error: invalid input")
        return
    if student_name not in grades:
        print("Error: student not found")
        return
    grades_list = grades[student_name]
    if not grades_list:
        print("Error: no grades available")
        return
    average = sum(grades_list) / len(grades_list)
    is_passed = average >= 70.0
    print(f"Grades: {grades_list}")
    print(f"Average: {average}")
    print(f"Passed: {str(is_passed).lower()}")

problem4()

# Problem 5: Word frequency counter (list + dict)
"""
Descripción:
Cuenta la frecuencia de cada palabra en una
oración usando una lista y un diccionario. Muestra
el diccionario de frecuencias y la palabra más
común.

Entradas:
- sentence (string).

Salidas:
- "Words list:" <words_list>.
- "Frequencies:" <freq_dict>.
- "Most common word:" <word>.

Validaciones:
- sentence no debe estar vacío después de
    aplicar strip().
- Manejar puntuación simple reemplazando comas y
    puntos por espacios.
- Verificar que la lista de palabras no esté
    vacía.

Casos de prueba:
1) Normal: sentence="apple banana apple orange" ->
     Words list: ['apple', 'banana', 'apple',
     'orange'], Frequencies: {'apple': 2,
     'banana': 1, 'orange': 1}, Most common word:
     apple.
2) Borde: sentence="apple" -> Words list:
     ['apple'], Frequencies: {'apple': 1},
     Most common word: apple.
3) Error: sentence="" -> Error: invalid input.
"""
def problem5():
    print("\n--- Problem 5: Word frequency counter (list + dict) ---")
    sentence = input("Enter a sentence: ").strip()
    if sentence == "":
        print("Error: invalid input")
        return
    # Handle simple punctuation
    sentence = sentence.replace(",", " ").replace(".", " ")
    words_list = [word for word in sentence.lower().split() if word]
    if not words_list:
        print("Error: invalid input")
        return
    freq_dict = {}
    for word in words_list:
        freq_dict[word] = freq_dict.get(word, 0) + 1
    most_common_word = max(freq_dict, key=freq_dict.get)
    print(f"Words list: {words_list}")
    print(f"Frequencies: {freq_dict}")
    print(f"Most common word: {most_common_word}")

problem5()

# Problem 6: Simple contact book (dictionary CRUD)
"""
Descripción:
Implementa una mini libreta de contactos usando un
diccionario (name -> phone). Soporta las acciones
ADD, SEARCH y DELETE.

Entradas:
- action_text (string; "ADD", "SEARCH", "DELETE").
- name (string; depende de la acción).
- phone (string; solo para "ADD").

Salidas:
- Para "ADD":
    - "Contact saved:" name, phone.
- Para "SEARCH":
    - Si existe: "Phone:" <phone>.
    - Si no: "Error: contact not found".
- Para "DELETE":
    - Si existe: "Contact deleted:" name.
    - Si no: "Error: contact not found".

Validaciones:
- Normalizar action_text a mayúsculas.
- Verificar que action_text sea una de las tres
    opciones válidas.
- name no debe estar vacío después de aplicar
    strip().
- Para "ADD": phone no debe estar vacío después
    de aplicar strip().

Casos de prueba:
1) Normal: action_text="ADD", name="Alice",
     phone="123" -> Contact saved: Alice, 123.
2) Borde: action_text="SEARCH", name="Bob" ->
     Phone: 456.
3) Error: action_text="DELETE", name="Eve" ->
     Error: contact not found.
"""
def problem6():
    print("\n--- Problem 6: Simple contact book (dictionary CRUD) ---")
    contacts = {"Alice": "123", "Bob": "456", "Charlie": "789"}
    action_text = input("Enter action (ADD, SEARCH, DELETE): ").strip().upper()
    if action_text not in ["ADD", "SEARCH", "DELETE"]:
        print("Error: invalid input")
        return
    name = input("Enter contact name: ").strip()
    if name == "":
        print("Error: invalid input")
        return
    if action_text == "ADD":
        phone = input("Enter phone number: ").strip()
        if phone == "":
            print("Error: invalid input")
            return
        contacts[name] = phone
        print(f"Contact saved: {name}, {phone}")
    elif action_text == "SEARCH":
        if name in contacts:
            print(f"Phone: {contacts[name]}")
        else:
            print("Error: contact not found")
    elif action_text == "DELETE":
        if name in contacts:
            contacts.pop(name)
            print(f"Contact deleted: {name}")
        else:
            print("Error: contact not found")

problem6()

# Conclusions
"""
Lists are best for flexible collections where elements are added or removed often. Tuples are ideal for fixed data that should not change, such as coordinates or settings. Dictionaries provide fast lookups and are perfect for associating keys with values, like catalogs or contact books. Combining these structures, such as using a dictionary of lists, enables powerful data modeling for practical applications. Understanding when and how to use each collection type is essential for writing efficient and maintainable Python code.
"""

# References
"""
References:
1) Python documentation - Built-in Types: list, tuple, dict: https://docs.python.org/3/library/stdtypes.html
2) W3Schools Python Lists, Tuples, Dictionaries: https://www.w3schools.com/python/python_lists.asp
3) Real Python - Dictionaries 101: https://realpython.com/python-dicts/
4) GeeksforGeeks - Python Tuples: https://www.geeksforgeeks.org/python-tuples/
5) Programiz - Python Data Structures: https://www.programiz.com/python-programming/list
6) Python Official Tutorial - Data Structures: https://docs.python.org/3/tutorial/datastructures.html
"""

# GitHub Repository
"""
https://github.com/Ricardo-Pugliesse-2530033/7_tareas_infernales_de_charly

"""
