"""Problema 6.1: Gestor CRUD usando diccionarios y/o listas con funciones.

He elegido la opción A: un diccionario donde la clave es el
`item_id` y el valor es otro diccionario con los datos del ítem.

Razón: buscar, actualizar y eliminar por id es O(1) en promedio,
mientras que con una lista tendría que recorrerla completa para
encontrar un elemento.
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
	opcion = input("Selecciona una opción (0-5): ").strip()
	if opcion not in {"0", "1", "2", "3", "4", "5"}:
		print("Error: invalid input")
		return None
	return opcion


def leer_id():
	item_id = input("Ingresa el id del item: ").strip()
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

	name = input("Ingresa el nombre del item: ").strip()
	if not name:
		print("Error: invalid input")
		return None

	try:
		price_str = input("Ingresa el precio (>= 0.0): ").strip()
		price = float(price_str)
		quantity_str = input("Ingresa la cantidad (>= 0): ").strip()
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
			print("Saliendo del programa...")
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

