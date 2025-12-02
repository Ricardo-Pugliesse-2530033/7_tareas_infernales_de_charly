# Portada
# Name: Ricardo Pugliesse
# Student ID: 2530033
# Group: GDS0352

# Executive Summary
"""
Lists, tuples, and dictionaries are fundamental collection types in Python. Lists are ordered and mutable, allowing elements to be added, removed, or changed. Tuples are ordered and immutable, ideal for fixed data like coordinates or dates. Dictionaries store key-value pairs, enabling fast lookups and flexible data association. This document covers six practical problems, each with a description, inputs, outputs, validations, and test cases, demonstrating the use of lists, tuples, and dictionaries for cataloging, searching, updating, and aggregating data in real-world scenarios.
"""

# Principles and Best Practices
"""
- Use lists when you need to frequently add or remove elements.
- Use tuples for data that should not change (e.g., coordinates, fixed settings).
- Use dictionaries for fast lookups by key (e.g., name, id, code).
- Avoid modifying a list while iterating over it unless you know exactly what you are doing.
- Use descriptive key names in dictionaries (e.g., "name", "age", "price").
- Write readable code and clear messages for the user.
"""

# Problem 1: Shopping list basics (list operations)
"""
Description:
Works with a list of products (strings). The program:
1) Creates an initial list of products.
2) Allows adding a new product to the end.
3) Shows the total number of items in the list.
4) Checks if a specific product is in the list (boolean is_in_list).

Inputs:
- initial_items_text (string; e.g., "apple,banana,orange").
- new_item (string; product to add).
- search_item (string; product to search).

Outputs:
- "Items list:" <items_list>
- "Total items:" <len_list>
- "Found item:" true|false

Validations:
- initial_items_text not empty after strip().
- Split the string by commas and strip spaces from each element.
- new_item and search_item not empty.
- Handle empty initial list if decided (documented below).

Test cases:
1) Normal: initial_items_text="apple,banana,orange", new_item="grape", search_item="banana" -> Items list: ['apple', 'banana', 'orange', 'grape'], Total items: 4, Found item: true
2) Border: initial_items_text="", new_item="apple", search_item="apple" -> Items list: ['apple'], Total items: 1, Found item: true
3) Error: initial_items_text="apple,banana", new_item="", search_item="banana" -> Error: invalid input
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
Description:
Uses tuples to represent two points in 2D: (x1, y1) and (x2, y2). Calculates the Euclidean distance and the midpoint.

Inputs:
- x1, y1, x2, y2 (float; coordinates).

Outputs:
- "Point A:" (x1, y1)
- "Point B:" (x2, y2)
- "Distance:" <distance>
- "Midpoint:" (mx, my)

Validations:
- All four inputs can be converted to float.

Test cases:
1) Normal: x1=0, y1=0, x2=3, y2=4 -> Point A: (0.0, 0.0), Point B: (3.0, 4.0), Distance: 5.0, Midpoint: (1.5, 2.0)
2) Border: x1=1, y1=1, x2=1, y2=1 -> Point A: (1.0, 1.0), Point B: (1.0, 1.0), Distance: 0.0, Midpoint: (1.0, 1.0)
3) Error: x1="a", y1=0, x2=3, y2=4 -> Error: invalid input
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
Description:
Manages a product catalog using a dictionary (product name -> unit price). Calculates total price for a given product and quantity.

Inputs:
- product_name (string).
- quantity (int).

Outputs:
- If product exists:
  - "Unit price:" <unit_price>
  - "Quantity:" <quantity>
  - "Total:" <total_price>
- If not:
  - "Error: product not found"

Validations:
- quantity > 0
- product_name not empty after strip()
- Check if product_name is in the dictionary.

Test cases:
1) Normal: product_name="apple", quantity=2 -> Unit price: 10.0, Quantity: 2, Total: 20.0
2) Border: product_name="banana", quantity=1 -> Unit price: 5.0, Quantity: 1, Total: 5.0
3) Error: product_name="pear", quantity=2 -> Error: product not found
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
Description:
Manages student grades using a dictionary (student name -> list of grades). Calculates average and pass status.

Inputs:
- student_name (string).

Outputs:
- If student exists:
  - "Grades:" <grades_list>
  - "Average:" <average>
  - "Passed:" true|false
- If not:
  - "Error: student not found"

Validations:
- student_name not empty after strip().
- Check if student_name is a key in the dictionary.
- Check that the grades list is not empty before calculating average.

Test cases:
1) Normal: student_name="Alice" -> Grades: [90, 85, 80], Average: 85.0, Passed: true
2) Border: student_name="Bob" -> Grades: [70], Average: 70.0, Passed: true
3) Error: student_name="Eve" -> Error: student not found
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
Description:
Counts the frequency of each word in a sentence using a list and a dictionary. Shows the frequency dictionary and the most common word.

Inputs:
- sentence (string).

Outputs:
- "Words list:" <words_list>
- "Frequencies:" <freq_dict>
- "Most common word:" <word>

Validations:
- sentence not empty after strip().
- Handle simple punctuation by replacing commas and periods with spaces.
- Check that the words list is not empty.

Test cases:
1) Normal: sentence="apple banana apple orange" -> Words list: ['apple', 'banana', 'apple', 'orange'], Frequencies: {'apple': 2, 'banana': 1, 'orange': 1}, Most common word: apple
2) Border: sentence="apple" -> Words list: ['apple'], Frequencies: {'apple': 1}, Most common word: apple
3) Error: sentence="" -> Error: invalid input
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
Description:
Implements a mini contact book using a dictionary (name -> phone). Supports ADD, SEARCH, and DELETE actions.

Inputs:
- action_text (string; "ADD", "SEARCH", "DELETE").
- name (string; depends on action).
- phone (string; only for "ADD").

Outputs:
- For "ADD":
  - "Contact saved:" name, phone
- For "SEARCH":
  - If exists: "Phone:" <phone>
  - If not: "Error: contact not found"
- For "DELETE":
  - If exists: "Contact deleted:" name
  - If not: "Error: contact not found"

Validations:
- Normalize action_text to uppercase.
- Check that action_text is one of the three valid options.
- name not empty after strip().
- For "ADD": phone not empty after strip().

Test cases:
1) Normal: action_text="ADD", name="Alice", phone="123" -> Contact saved: Alice, 123
2) Border: action_text="SEARCH", name="Bob" -> Phone: 456
3) Error: action_text="DELETE", name="Eve" -> Error: contact not found
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
