"""
Descripción:
Dado el nombre completo de una persona en una sola cadena (por ejemplo: "juan carlos tovar"), el programa debe:
1) Normalizar el texto (strip, espacios extra, mayúsculas/minúsculas).
2) Mostrar el nombre formateado en Title Case y las iniciales (por ejemplo: J.C.T.).
"""


full_name = input("Escribe tu full name pls")

full_name.strip

if full_name == '':
    print('Error ingresa nombre valiod plebe')

full_name = full_name.lower()
words = full_name.split()
if len(words) < 2:
    print('Error ingresa al menos nombre y apellido plebe')


formatted_name = full_name.title()
Iniciales = ''
for word in words:
    Iniciales += word[0].upper() + '.'

print('Formated name:', formatted_name)
print('Iniciales:', Iniciales) 

# # Problem 2: Simple email validator (structure + domain) 


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

User_email = input("Ingresa un correo:  ").strip()

if User_email == '':
    print('Error: correo vacio')
    exit()

if User_email.count('@') != 1 or ' ' in User_email:
    print('Valid email: false')
    exit()

at_index = User_email.find('@')
domain = User_email[at_index + 1:]
if '.' in domain:
    print('Valid email: true')
    print('Domain:', domain)
else:
    print('Valid email: false')


# 3

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

frase = input("Enter a phrase: ").strip()
if frase == '':
    print('Error: empty phrase')
    exit()

normalized_phrase = frase.replace(" ", "").lower()
if len(normalized_phrase) < 3:
    print('Error: phrase too short')
    exit()

if normalized_phrase == normalized_phrase[::-1]:
    print("Es un pharaser:") 
else:
    print("No es un pharaser")

