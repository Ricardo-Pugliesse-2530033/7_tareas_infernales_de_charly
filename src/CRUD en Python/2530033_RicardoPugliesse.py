"""


Nombre del estudiante : Ricardo Martin Pugliesse Macías
Matrícula             : 2530033
Grupo                 : IM 1-2



RESUMEN EJECUTIVO

Este programa implementa un gestor CRUD (Create, Read, Update,
Delete) en memoria para manejar items de inventario usando
Python. Un CRUD permite crear, leer, actualizar y eliminar
registros de manera organizada. En este caso, cada item tiene
id, name, price y quantity, y se maneja mediante funciones
separadas para cada operación. El usuario interactúa a través de
un menú de texto que llama a estas funciones, lo que hace que el
código sea más modular, legible y fácil de mantener. Se incluye
validación de entradas y mensajes claros para cada operación.

PROBLEMA ÚNICO: CRUD CON FUNCIONES

Problem: In-memory CRUD manager with functions

Descripción:
Programa que implementa un CRUD (Crear, Leer, Actualizar,
Eliminar) simple para elementos almacenados en memoria,
utilizando funciones para cada operación y un menú de texto para
interactuar con el usuario.

Inputs:
- User menu options (string/int).
- For CREATE/UPDATE: item_id, name, price, quantity.
- For READ/DELETE: item_id.

Outputs:
- Mensajes que indican el resultado de cada operación:
	- "Item created", "Item updated", "Item deleted",
		"Item not found", "Items list:", etc.

Validations:
- Menu option must be valid (0..5).
- item_id must not be empty.
- price y quantity deben ser números válidos:
	- price >= 0.0
	- quantity >= 0
- No permitir crear un item con id duplicado.
- Para READ/UPDATE/DELETE, si el id no existe, mostrar
	"Item not found".

Test cases:
1) Normal: crear un item, leerlo, actualizarlo y eliminarlo
	 → se muestran los mensajes esperados y el estado final es
	 coherente.
2) Borde: crear un item con quantity = 0 pero price >= 0.0
	 → se acepta como caso válido.
3) Error: usar opción de menú inválida, id vacío o price
	 no numérico → se muestran mensajes "Error: invalid input".

DECISIÓN DE ESTRUCTURA DE DATOS

He elegido la opción A: un diccionario donde la clave es el
item_id y el valor es otro diccionario con los datos del item.

Razón: buscar, actualizar y eliminar por id tiene un costo
promedio O(1), mientras que con una lista tendría que recorrerla
completa para encontrar un elemento y la actualización sería más
costosa. Además, el código queda más directo al trabajar con
keys y values.
"""


def create_item(items, item_id, name, price, quantity):
	"""Crea un ítem nuevo.

	items: dict principal
	item_id: clave única (string o int)

	Política para ids duplicados: **no se permiten duplicados**.
	Si el id ya existe, no se crea el ítem y se devuelve False.
	"""

	if item_id in items:
		return False

	items[item_id] = {
		"id": item_id,
		"name": name,
		"price": price,
		"quantity": quantity,
	}
	return True


def read_item(items, item_id):
	"""Devuelve el diccionario del ítem si existe, o None si no."""

	return items.get(item_id)


def update_item(items, item_id, new_name, new_price, new_quantity):
	"""Actualiza un ítem existente. Devuelve True si se actualiza, False si no existe."""

	if item_id not in items:
		return False

	items[item_id]["name"] = new_name
	items[item_id]["price"] = new_price
	items[item_id]["quantity"] = new_quantity
	return True


def delete_item(items, item_id):
	"""Elimina un ítem por id. Devuelve True si se elimina, False si no existe."""

	if item_id not in items:
		return False

	del items[item_id]
	return True


def list_items(items):
	"""Imprime la lista de ítems en un formato legible."""

	if not items:
		print("Items list: (vacía)")
		return

	print("Items list:")
	print("-" * 40)
	for item in items.values():
		print(
			f"ID: {item['id']} | Name: {item['name']} | "
			f"Price: {item['price']:.2f} | Quantity: {item['quantity']}"
		)
	print("-" * 40)


def mostrar_menu():
	print("\nGESTOR CRUD DE ITEMS")
	print("1) Create item")
	print("2) Read item by id")
	print("3) Update item by id")
	print("4) Delete item by id")
	print("5) List all items")
	print("0) Exit")


def leer_opcion():
	opcion = input("Please select an option (0-5): ").strip()
	if opcion not in {"0", "1", "2", "3", "4", "5"}:
		print("Error: invalid input")
		return None
	return opcion


def leer_id():
	item_id = input("Enter the item id: ").strip()
	if not item_id:
		print("Error: invalid input")
		return None
	return item_id


def leer_datos_item(include_id=True):
	"""Lee datos de un ítem desde teclado.

	Si include_id es True, también pide el id.
	Devuelve una tupla (id, name, price, quantity) o None si hay error.
	"""

	item_id = None
	if include_id:
		item_id = leer_id()
		if item_id is None:
			return None

	name = input("Enter the item name: ").strip()
	if not name:
		print("Error: invalid input")
		return None

	try:
		price_str = input("Enter the price (>= 0.0): ").strip()
		price = float(price_str)
		quantity_str = input("Enter the quantity (>= 0): ").strip()
		quantity = int(quantity_str)
	except ValueError:
		print("Error: invalid input")
		return None

	if price < 0.0 or quantity < 0:
		print("Error: invalid input")
		return None

	return (item_id, name, price, quantity)


def main():
	# Estructura de datos principal: diccionario id -> dict con los datos del ítem
	items = {}

	while True:
		mostrar_menu()
		opcion = leer_opcion()
		if opcion is None:
			# opción inválida, se vuelve a mostrar el menú
			continue

		if opcion == "0":
			print("Exiting the program...")
			break

		if opcion == "1":  # Create item
			datos = leer_datos_item(include_id=True)
			if datos is None:
				continue
			item_id, name, price, quantity = datos
			creado = create_item(items, item_id, name, price, quantity)
			if creado:
				print("Item created")
			else:
				print("Error: id already exists (no se permiten duplicados)")

		elif opcion == "2":  # Read item by id
			item_id = leer_id()
			if item_id is None:
				continue
			item = read_item(items, item_id)
			if item is None:
				print("Item not found")
			else:
				print("Item found:")
				print(
					f"ID: {item['id']} | Name: {item['name']} | "
					f"Price: {item['price']:.2f} | Quantity: {item['quantity']}"
				)

		elif opcion == "3":  # Update item by id
			item_id = leer_id()
			if item_id is None:
				continue
			if read_item(items, item_id) is None:
				print("Item not found")
				continue

			# Para actualizar, no pedimos de nuevo el id
			datos = leer_datos_item(include_id=False)
			if datos is None:
				continue
			_, new_name, new_price, new_quantity = datos
			actualizado = update_item(items, item_id, new_name, new_price, new_quantity)
			if actualizado:
				print("Item updated")
			else:
				print("Item not found")

		elif opcion == "4":  # Delete item by id
			item_id = leer_id()
			if item_id is None:
				continue
			eliminado = delete_item(items, item_id)
			if eliminado:
				print("Item deleted")
			else:
				print("Item not found")

		elif opcion == "5":  # List all items
			list_items(items)


if __name__ == "__main__":
	main()


# CONCLUSIONES
"""
El uso de funciones para cada operación del CRUD
facilita la organización del código, ya que separa
claramente la lógica de creación, lectura,
actualización, eliminación y listado de items.
Trabajar con un diccionario como estructura
principal simplifica las búsquedas por id y evita
recorridos innecesarios. Durante la validación de
entradas fue importante verificar ids vacíos,
valores numéricos negativos y opciones de menú
inválidas, mostrando siempre mensajes claros al
usuario. Este CRUD podría extenderse fácilmente a
un sistema más grande guardando los datos en
archivos o bases de datos, manteniendo la misma
interfaz de funciones.
"""

# REFERENCES
"""
References:
1) Python documentation - Data Structures (dict, list):
   https://docs.python.org/3/tutorial/datastructures.html
2) Python documentation - Defining Functions:
   https://docs.python.org/3/tutorial/controlflow.html#defining-functions
3) Real Python - Dictionaries in Python:
   https://realpython.com/python-dicts/
"""

# GITHUB REPOSITORY
"""
https://github.com/Ricardo-Pugliesse-2530033/7_tareas_infernales_de_charly
"""
