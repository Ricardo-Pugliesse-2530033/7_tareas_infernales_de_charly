

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