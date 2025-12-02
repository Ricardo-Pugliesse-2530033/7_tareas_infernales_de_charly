

# Problem 1: Full name formatter (name + initials)

"""
Descripción:
Dado el nombre completo de una persona en una sola cadena (por ejemplo: "juan carlos tovar"), el programa debe:
1) Normalizar el texto (strip, espacios extra, mayúsculas/minúsculas).
2) Mostrar el nombre formateado en Title Case y las iniciales (por ejemplo: J.C.T.).
"""

full_name = ''


full_name = input("Enter your full name: ")
# Normalizar el texto
full_name = full_name.strip()

if full_name == '':
    print("Error: No name provided.")

words = full_name.split()


# Validad cantidad de Palabras
if len(words) < 2:
    print("Error: Please enter at least a first name and a last name.")
    exit()

formatted_name = full_name.title()


initials = ""
for word in words:
    initials += word[0].upper() + "."


print("Formatted name:", formatted_name)
print("Initials:", initials)




# Problem 2: Simple email validator (structure + domain) 


"""
Descripción:
Valida si una dirección de correo tiene un formato básico correcto:
- Contiene exactamente un '@'.
- Después del '@' debe haber al menos un '.'.
- No contiene espacios en blanco.
Si el correo es válido, también muestra el dominio (la parte después de '@').

Entradas:
- email_text (string).

Salidas:
- "Valid email: true" o "Valid email: false"
- Si es válido: "Domain: <domain_part>"

Validaciones:
- email_text no vacío tras strip().
- Contar cuántas veces aparece '@'.
- Verificar que no haya espacios (no debe haber " " en email_text).

Operaciones clave sugeridas: strip(), count(), find(), slicing, in, not in.
"""

user_email = input("Enter your email address: ")

# Validación: no debe quedar vacío
user_email = user_email.strip()

if user_email == "":
    print("Valid email: false")
else:
    # Validar estructura del correo
    if user_email.count("@") != 1 or " " in user_email:
        print("Valid email: false")
    else:
        at_index = user_email.find("@")
        domain = user_email[at_index + 1:]
        
        if "." in domain:
            print("Valid email: true")
            print("Domain:", domain)
        else:
            print("Valid email: false")
 


# 3. CONVENCIONES (NAMING Y OUTPUT EN INGLÉS)

"""
Descripción:
Determina si una frase es un palíndromo, es decir, se lee igual de izquierda a derecha y de derecha a izquierda, ignorando espacios y mayúsculas/minúsculas.

Ejemplos:
- "Anita lava la tina" -> palíndromo.
- "Hola mundo" -> no palíndromo.

Entradas:
- phrase (string).

Salidas:
- "Is palindrome: true" o "Is palindrome: false"
- (Opcional) Mostrar también la versión normalizada de la frase.

Validaciones:
- phrase no vacía tras strip().
- Longitud mínima razonable después de limpiar espacios (por ejemplo, al menos 3 caracteres).

Operaciones clave sugeridas: lower(), replace(" ", ""), slicing inverso text[::-1], comparación ==.
"""

phrase = input("Enter a phrase: ")
# Normalizar la frase
normalized_phrase = phrase.strip().lower().replace(" ", "")
if len(normalized_phrase) < 3:
    print("Is palindrome: false")
else:
    if normalized_phrase == normalized_phrase[::-1]:
        print("Is palindrome: true")
    else:
        print("Is palindrome: false")
    print("Normalized phrase:", normalized_phrase)

# Problem 4: Sentence word stats (lengths and first/last word)

"""

--------------------------------------------------

Descripción:
Dada una oración, el programa debe:
1) Normalizar espacios (quitar espacios al principio y al final).
2) Separar las palabras por espacios.
3) Mostrar:
   - Número total de palabras.
   - Primera palabra.
   - Última palabra.
   - Palabra más corta y más larga (por longitud).

Entradas:
- sentence (string).

Salidas:
- "Word count: <n>"
- "First word: <...>"
- "Last word: <...>"
- "Shortest word: <...>"
- "Longest word: <...>"

Validaciones:
- Oración no vacía tras strip().
- Debe contener al menos una palabra válida después de split().

Operaciones clave sugeridas: strip(), split(), len(), recorrer la lista de palabras para encontrar mínima y máxima longitud.

"""

sentence = input("Enter a sentence: ")
# Normalizar la oración
sentence = sentence.strip()
words = sentence.split()

if len(words) == 0:
    print("Error: No valid words entered.")
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

#  Problem 5: Password strength classifier

"""
Descripción:
Clasifica una contraseña como "weak", "medium" o "strong" según reglas mínimas (puedes afinarlas, pero documéntalas en los comentarios).

Ejemplo de reglas:
- Weak: longitud < 8 o todo en minúsculas o muy simple.
- Medium: longitud >= 8 y mezcla de letras (mayúsculas/minúsculas) o dígitos.
- Strong: longitud >= 8 y contiene al menos:
  - una letra mayúscula,
  - una letra minúscula,
  - un dígito,
  - un símbolo no alfanumérico (por ejemplo, !, @, #, etc.).

Entradas:
- password_input (string).

Salidas:
- "Password strength: weak"
- "Password strength: medium"
- "Password strength: strong"

Validaciones:
- No aceptar contraseña vacía.
- Verificar longitud con len().

Operaciones clave sugeridas:
- Recorrer carácter por carácter.
- Métodos: isupper(), islower(), isdigit(), isalnum().
- Uso de banderas booleanas (has_upper, has_lower, etc.).

"""

password_input = input("Enter your password: ")
password_input = password_input.strip()
if password_input == "":
    print("Error: Password cannot be empty.")
else:
    length = len(password_input)
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    for char in password_input:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif not char.isalnum():
            has_symbol = True

    if length < 8 or (not has_upper and not has_digit and not has_symbol):
        strength = "weak"
    elif length >= 8 and ((has_upper and has_lower) or (has_lower and has_digit) or (has_upper and has_digit)):
        strength = "medium"
    elif length >= 8 and has_upper and has_lower and has_digit and has_symbol:
        strength = "strong"
    else:
        strength = "weak"

    print("Password strength:", strength)



# Problem 6: Product label formatter (fixed-width text)

"""
Descripción:
Dado el nombre de un producto y su precio, genera una etiqueta en una sola línea con el siguiente formato:

Product: <NAME> | Price: $<PRICE>

La cadena completa debe tener exactamente 30 caracteres:
- Si es más corta, rellena con espacios al final.
- Si es más larga, recorta hasta 30 caracteres.

Entradas:
- product_name (string).
- price_value (puede leerse como string o número; conviértelo a string para mostrarlo).

Salidas:
- "Label: <exactly 30 characters>"
(Puedes mostrar la etiqueta entre comillas para que se vean los espacios.)

Validaciones:
- product_name no vacío tras strip().
- price_value debe poder convertirse a un número positivo.

Operaciones clave sugeridas:
- Uso de f-strings o concatenación para formar la etiqueta base.
- len() para medir la longitud.
- slicing para recortar: label[:30].
- Relleno con espacios hasta alcanzar 30 caracteres.
"""

product_name = input("Enter product name: ").strip()
price_value = input("Enter product price: ").strip()

try:
    price_float = float(price_value)
    if price_float < 0:
        raise ValueError("Price must be positive.")
except ValueError as e:
    print("Error:", e)

label = f"Product: {product_name} | Price: ${price_float:.2f}"
if len(label) < 30:
    label = label.ljust(30)
else:
    label = label[:30]
print(f'Label: "{label}"')


