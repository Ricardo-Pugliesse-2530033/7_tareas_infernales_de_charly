
"""

Nombre del estudiante : Ricardo Martin Pugliesse Macías
Matrícula             : 2530033
Grupo                 : IM 1-2 
Nombre del archivo    : 2530033_PugliesseRicardo_t_strings.py


RESUMEN EJECUTIVO

En Python, un string es una secuencia inmutable de
caracteres Unicode que se usa para representar texto.
Al ser inmutables, cada operación de modificación
(como replace o strip) devuelve una nueva cadena en
lugar de cambiar la original. Entre las operaciones
más comunes se encuentran la concatenación, el cálculo
de longitud, la extracción de subcadenas con slicing,
la búsqueda de patrones y el reemplazo o formato de
texto. La validación y normalización de la entrada
del usuario (por ejemplo, nombres, correos y
contraseñas) es esencial para evitar errores,
problemas de seguridad y datos inconsistentes. Este
documento muestra seis programas que usan strings para
formatear nombres, validar correos, revisar
palíndromos, obtener estadísticas de oraciones,
clasificar contraseñas y dar formato a etiquetas de
producto.


PRINCIPIOS Y BUENAS PRÁCTICAS

- Los strings son inmutables, por lo que cada cambio
    genera una nueva cadena en lugar de modificar la
    original.
- Es buena práctica normalizar la entrada del usuario
    con strip() para eliminar espacios extra y lower()
    para ignorar mayúsculas/minúsculas al comparar.
- Se deben evitar los "números mágicos" en índices y
    explicar claramente qué extrae cada slice.
- Es mejor utilizar los métodos integrados de string
    (split, join, replace, startswith, endswith, find)
    que reescribir lógica básica desde cero.
- Las validaciones deben diseñarse en pasos claros:
    primero verificar que el texto no esté vacío y
    después revisar el formato esperado.
- El código debe ser legible, con nombres de
    variables descriptivos y mensajes de error
    comprensibles.


Problem 1: Full name formatter (name + initials)

Descripción:
Este problema lee el nombre completo de una persona
en una sola cadena, normaliza los espacios y las
mayúsculas/minúsculas y luego imprime el nombre
formateado en Title Case junto con sus iniciales en
forma X.X.X.

Entradas:
- full_name (string): nombre completo de la persona,
    con posible mezcla de mayúsculas/minúsculas y
    espacios extra.

Salidas:
- "Formatted name: <Name In Title Case>".
- "Initials: <X.X.X.>".

Validaciones:
- full_name no debe quedar vacío después de usar
    strip().
- Debe contener al menos dos palabras (nombre y
    apellido).
- No se aceptan cadenas que solo contengan espacios.

Casos de prueba:
1) Normal: "juan carlos tovar" ->
     Formatted name: "Juan Carlos Tovar",
     Initials: "J.C.T.".
2) Borde: "  aNA   pEREz  " ->
     Formatted name: "Ana Perez",
     Initials: "A.P.".
3) Error: "   " -> mensaje de error por nombre
     vacío.
"""

full_name = input("Enter your full name: ")
full_name = full_name.strip()

if full_name == "":
    print("Error: invalid input (empty name)")
else:
    words = full_name.split()

    if len(words) < 2:
        print(
            "Error: please enter at least a first name "
            "and a last name"
        )
    else:
        formatted_name = full_name.title()
        initials = ""
        for word in words:
            initials += word[0].upper() + "."

        print("Formatted name:", formatted_name)
        print("Initials:", initials)


"""

Problem 2: Simple email validator (structure + domain)

Descripción:
Este problema valida si una dirección de correo tiene
una estructura básica correcta: exactamente un '@',
al menos un punto después del '@' y que no contenga
espacios en blanco. Si el correo es válido, también
se muestra el dominio (la parte después de '@').

Entradas:
- email_text (string): dirección de correo del
  usuario.

Salidas:
- "Valid email: true" o "Valid email: false".
- Si es válido: "Domain: <domain_part>".

Validaciones:
- email_text no debe estar vacío después de strip().
- Se debe contar cuántas veces aparece '@'.
- Se verifica que no existan espacios en blanco en
  email_text.

Casos de prueba:
1) Normal: "user@example.com" ->
    Valid email: true, Domain: "example.com".
2) Borde: " user.name@test.co  " ->
    Valid email: true, Domain: "test.co".
3) Error: "invalid@@mail" o "noatsymbol.com" ->
    Valid email: false.
"""
# Email validator

email_text = input("Enter your email address: ")
email_text = email_text.strip()

if email_text == "":
    print("Valid email: false")
    exit()
else:
    if email_text.count("@") != 1 or " " in email_text:
        print("Valid email: false")
    else:
        at_index = email_text.find("@")
        domain_part = email_text[at_index + 1 :]

        if "." in domain_part and domain_part != "":
            print("Valid email: true")
            print("Domain:", domain_part)
        else:
            print("Valid email: false")


"""

Problem 3: Palindrome checker (ignoring spaces and case)

Descripción:
Este problema lee una frase de texto y determina si es
un palíndromo, es decir, si se lee igual de izquierda
a derecha y de derecha a izquierda cuando se ignoran
los espacios y las mayúsculas/minúsculas.

Entradas:
- phrase (string): oración o palabra a evaluar.

Salidas:
- "Is palindrome: true" o "Is palindrome: false".
- Opcionalmente, la versión normalizada de la frase.

Validaciones:
- phrase no debe estar vacía después de strip().
- Después de quitar espacios, la longitud debe ser
  de al menos 3 caracteres.

Casos de prueba:
1) Normal: "Anita lava la tina" -> Is palindrome: true.
2) Borde: "aa a" -> normalizado "aaa" ->
    Is palindrome: true.
3) Error: "  " o solo dos letras ->
    Is palindrome: false por ser demasiado corta.
"""
# palindrome
phrase = input("Enter a phrase: ")
normalized_phrase = phrase.strip().lower().replace(" ", "")

if len(normalized_phrase) < 3:
    print("Is palindrome: false")
    exit()
else:
    is_palindrome = normalized_phrase == normalized_phrase[::-1]
    print("Is palindrome:", str(is_palindrome).lower())
    print("Normalized phrase:", normalized_phrase)


"""

Problem 4: Sentence word stats (lengths and first/last word)

Descripción:
Este problema lee una oración, elimina espacios al
inicio y al final, separa el texto en palabras y
muestra estadísticas como el número total de
palabras, la primera, la última, la más corta y la
más larga.

Entradas:
- sentence (string): oración con una o más palabras
  separadas por espacios.

Salidas:
- "Word count: <n>".
- "First word: <...>".
- "Last word: <...>".
- "Shortest word: <...>".
- "Longest word: <...>".

Validaciones:
- sentence no debe estar vacía después de strip().
- Tras el split debe existir al menos una palabra
  válida.

Casos de prueba:
1) Normal: "This is a simple test" ->
    Word count: 5, First word: "This",
    Last word: "test", Shortest word: "a",
    Longest word: "simple".
2) Borde: "   onlyOneWord   " ->
    Word count: 1 y la misma palabra como primera,
    última, más corta y más larga.
3) Error: "   " -> mensaje de error por no tener
    palabras válidas.
"""

sentence = input("Enter a sentence: ")
sentence = sentence.strip()
words = sentence.split()

if len(words) == 0:
    print("Error: no valid words entered")
    exit()
else:
    word_count = len(words)
    first_word = words[0]
    last_word = words[-1]
    shortest_word = min(words, key=len)
    longest_word = max(words, key=len)

    print("Word count:", word_count)
    print("First word:", first_word)
    print("Last word:", last_word)
    print("Shortest word:", shortest_word)
    print("Longest word:", longest_word)


"""

Problem 5: Password strength classifier

Descripción:
Este problema lee una contraseña y la clasifica como
"weak", "medium" o "strong" según reglas que
combinan la longitud y la presencia de diferentes
tipos de caracteres.

Reglas de clasificación usadas en el programa:
- Weak: longitud < 8, o no contiene ningún dígito,
    mayúscula ni símbolo (muy simple).
- Medium: longitud >= 8 y contiene al menos dos de
    estos grupos: minúsculas + mayúsculas, minúsculas
    + dígitos, mayúsculas + dígitos.
- Strong: longitud >= 8 y contiene al menos una
    letra mayúscula, una minúscula, un dígito y un
    símbolo no alfanumérico.

Entradas:
- password_input (string): contraseña ingresada por
    el usuario.

Salidas:
- "Password strength: weak".
- "Password strength: medium".
- "Password strength: strong".

Validaciones:
- La contraseña no puede estar vacía después de
    strip().
- La longitud se verifica con len().

Casos de prueba:
1) Normal: "Abc12345" -> Password strength: medium.
2) Borde: "Abc12345!" -> Password strength: strong.
3) Error: "     " o "aaaaaaa" -> contraseña vacía o
     demasiado simple -> weak / mensaje de error.
"""
# Calificar contraseña
password_input = input("Enter your password: ")
password_input = password_input.strip()

if password_input == "":
    print("Error: password cannot be empty")
else:
    length = len(password_input)
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    for character in password_input:
        if character.isupper():
            has_upper = True
        elif character.islower():
            has_lower = True
        elif character.isdigit():
            has_digit = True
        elif not character.isalnum():
            has_symbol = True

    if length < 8 or (not has_upper and not has_digit and not has_symbol):
        strength = "weak"
    elif length >= 8 and (
        (has_upper and has_lower)
        or (has_lower and has_digit)
        or (has_upper and has_digit)
    ) and not (has_upper and has_lower and has_digit and has_symbol):
        strength = "medium"
    elif length >= 8 and has_upper and has_lower and has_digit and has_symbol:
        strength = "strong"
    else:
        strength = "weak"

    print("Password strength:", strength)


"""

Problem 6: Product label formatter (fixed-width text)

Descripción:
Este problema lee el nombre de un producto y su
precio y genera una etiqueta en una sola línea con
el formato "Product: <NAME> | Price: $<PRICE>". La
etiqueta final debe tener exactamente 30 caracteres:
si es más corta se rellena con espacios y si es más
larga se recorta.

Entradas:
- product_name (string): descripción del producto.
- price_value (string o número): precio del
    producto, convertido a un valor numérico
    positivo.

Salidas:
- "Label: <exactly 30 characters>" (normalmente
    mostrada entre comillas para observar los
    espacios).

Validaciones:
- product_name no puede quedar vacío después de
    strip().
- price_value debe poder convertirse a un número
    positivo.

Casos de prueba:
1) Normal: product_name="Notebook", price_value="89.9" ->
     etiqueta de exactamente 30 caracteres.
2) Borde: nombre de producto muy largo -> la
     etiqueta se recorta a 30 caracteres.
3) Error: price_value="-10" o "abc" -> mensaje de
     error y sin etiqueta válida.
"""
#Product label formatter
product_name = input("Enter product name: ").strip()
price_value = input("Enter product price: ").strip()

if product_name == "":
    print("Error: product name cannot be empty")
else:
    price_is_valid = True
    try:
        price_float = float(price_value)
        if price_float <= 0:
            price_is_valid = False
            print("Error: price must be positive")
    except ValueError:
        price_is_valid = False
        print("Error: invalid price format")

    if price_is_valid:
        base_label = f"Product: {product_name} | Price: ${price_float:.2f}"
        if len(base_label) < 30:
            base_label = base_label.ljust(30)
        else:
            base_label = base_label[:30]
        print(f'Label: "{base_label}"')


"""

CONCLUSIONES

El manejo de cadenas es esencial en casi todas las
operaciones de entrada y salida de datos, sobre todo
cuando se trabaja con nombres, correos electrónicos,
contraseñas o información de productos. Métodos como
lower(), upper(), strip(), split() y join() ayudan a
normalizar y estructurar el texto antes de
procesarlo o almacenarlo. Normalizar el texto antes
de compararlo evita errores provocados por espacios
extra o diferencias en mayúsculas y minúsculas y da
comportamientos más consistentes. Un buen diseño de
validaciones impide que datos inválidos o basura
entren al sistema y facilita mensajes de error más
claros para el usuario. Con estas actividades
reforcé la idea de que los strings son inmutables y
que los slices permiten extraer partes específicas de
un texto sin modificar el valor original.


REFERENCIAS

1) Documentación oficial de Python - Built-in Types:
   Text Sequence Type — str.
2) Tutorial de Python - Sección de Strings,
   docs.python.org.
3) Sweigart, A. "Automate the Boring Stuff with
   Python", No Starch Press.
4) TutorialsPoint - Tutorial de Python Strings.
5) Real Python - "Working with Strings in Python".


REPOSITORIO DE GITHUB

URL del repositorio:
https://github.com/Ricardo-Pugliesse-2530033/7_tareas_infernales_de_charly


"""


