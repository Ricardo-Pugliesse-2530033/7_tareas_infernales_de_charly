


# Problem 1: Temperature converter and range flag

"""
Descripción:
Convierte una temperatura en grados Celsius (float) a Fahrenheit y Kelvin. 
Además, determina un valor booleano is_high_temperature que sea true si la temperatura en 
Celsius es mayor o igual que 30.0 y false en caso contrario.

Entradas:
- temp_c (float; temperatura en °C).

Salidas:
- "Fahrenheit:" <temp_f>
- "Kelvin:" <temp_k>

- "High temperature:" true|false

Validaciones:
- Verificar que temp_c pueda convertirse a float.
- No permitir temperaturas físicas imposibles en Kelvin (por ejemplo, temp_k < 0.0).

Operaciones clave sugeridas:
- Conversión: temp_f = temp_c * 9 / 5 + 32
- Conversión: temp_k = temp_c + 273.15
- Comparación: is_high_temperature = (temp_c >= 30.0)
"""

from curses.ascii import isdigit


temp_c_s = (input("Writte tmeperature:   "))
temp_c = float(temp_c_s)


temp_f = temp_c * 9 / 5 + 32
temp_k = temp_c + 273.15
is_high_temperature = (temp_c >= 30.0)

if temp_k < 0:
    print("Error No es psoible")
    exit()
print(f"High temperature: {is_high_temperature}")
    



print( f"In Celsius:  {temp_c_s} ") 
print(f" Fahrenheit: {temp_f}") 
print(f" Kelvin: {temp_k}") 



# Problem 2: Work hours and overtime payment

"""
Descripción:
Calcula el pago total semanal de un trabajador.
Hasta 40 horas se pagan a hourly_rate (float).
Las horas extra (> 40) se pagan al 150% de la tarifa normal.
Además, genera un booleano has_overtime que indique si el trabajador hizo horas extra.

Entradas:
- hours_worked (float; horas trabajadas en la semana).
- hourly_rate (float; pago por hora).

Salidas:
- "Regular pay:" <regular_pay>
- "Overtime pay:" <overtime_pay>
- "Total pay:" <total_pay>
- "Has overtime:" true|false

Validaciones:
- hours_worked >= 0
- hourly_rate > 0
- Si alguno no cumple, mostrar "Error: invalid input".

Operaciones clave sugeridas:
- Uso de min() y max() para separar horas regulares y extra.
- Cálculo: overtime_pay = overtime_hours * hourly_rate * 1.5
- Booleano: has_overtime = (hours_worked > 40)
"""

hours_worked_s = float(input("Ingresa horas trabajadas: "))
hourly_rate = float(input("Ingreesa la tarifa por hr:  "))

has_overtime = (hours_worked_s > 40.0)


if hours_worked_s < 40.0:
    total_pay = hours_worked_s * hourly_rate
    print(f"The total pay is: {total_pay}")
    print(f"Has overtime:  {has_overtime}")
else:
    hours_worked_extar = 0.0
    hours_worked_extar = hours_worked_s - 40 
    regular_pay = hours_worked_s * hourly_rate
    overtime_pay = hours_worked_extar * (hourly_rate * 1.5)
    print(f"The regular pay is: {regular_pay}")
    print(f"The overtime pay is: {overtime_pay}")
    total_pay = regular_pay + overtime_pay
    print(f"The total pay is: {total_pay}")
    print(f"Has overtime:  {has_overtime}")



# Problem 3: Discount eligibility with booleans

"""
Descripción:
Determina si un cliente obtiene un descuento en su compra. La regla es:
- Tiene descuento si:
  - is_student es true OR
  - is_senior es true OR
  - purchase_total >= 1000.0
Calcula también el total a pagar aplicando un 10% de descuento cuando sea elegible.

Entradas:
- purchase_total (float; total de la compra).
- is_student_text (string; "YES" o "NO").
- is_senior_text (string; "YES" o "NO").

Salidas:
- "Discount eligible:" true|false
- "Final total:" <final_total>

Validaciones:
- purchase_total >= 0.0
- Normalizar is_student_text e is_senior_text a mayúsculas y convertir a booleanos is_student, is_senior.
- Si el texto no es "YES" ni "NO", mostrar "Error: invalid input".

Operaciones clave sugeridas:
- Conversión a bool por comparación de strings.
- Booleanos: discount_eligible = is_student or is_senior or (purchase_total >= 1000.0)
- Cálculo: final_total = purchase_total * 0.9 si discount_eligible es true, si no, el mismo purchase_total.
"""

purchase_total = 0.0
is_student_text = None
is_senior_text = None
Discount_eligible = None



purchase_total = float(input("Enter your purchase amount:  "))

if purchase_total <= 0.0:
    print("Error Invalid quantity error")
    exit()
else:
    print("Answer the following question with a YES or a NO")
    is_student_text = input("Are you a student?")
    is_senior_text = input("Are you a senior?")
    is_student_text = is_student_text.strip().upper()
    is_senior_text = is_senior_text.strip().upper()
    if is_senior_text == "YES"  or is_student_text == "YES" or purchase_total >= 1000.0:
        Discount_eligible = (is_senior_text == "YES"  or is_student_text == "YES" or purchase_total >= 1000.0)

        print(f"Congratulations on receiving a discount! Your total is {purchase_total * 0.9}")
        print(Discount_eligible)
    else:
        Discount_eligible = (is_senior_text == "YES"  or is_student_text == "YES" or purchase_total >= 1000.0)
        print(f"Your total is: {purchase_total}")
        print(Discount_eligible)




# Problem 4: Basic statistics of three integers


"""
Descripción:
Lee tres números enteros y calcula: suma, promedio (float), valor máximo, valor mínimo y un booleano all_even que indique si los tres números son pares.

Entradas:
- n1 (int)
- n2 (int)
- n3 (int)

Salidas:
- "Sum:" <sum_value>
- "Average:" <average_value>
- "Max:" <max_value>
- "Min:" <min_value>
- "All even:" true|false

Validaciones:
- Verificar que los tres valores se puedan convertir a int.
- No se requieren restricciones adicionales (se permiten negativos).

Operaciones clave sugeridas:
- sum_value = n1 + n2 + n3
- average_value = sum_value / 3
- max(), min()
- all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)

"""

n1 = 0
n2 = 0
n3 = 0

n1 = int(input("Enter first integer: "))
n2 = int(input("Enter second integer: "))
n3 = int(input("Enter third integer: "))

if  isdigit(n1) or  isdigit(n2) or  isdigit(n3):
    sum_value_entero = n1 + n2 + n3
    sum_value_flotante = float(sum_value_entero)
    average_value = sum_value_flotante / 3
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)
    all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)

    print(f"Sum: {sum_value_entero}")
    print(f"Average: {average_value}")
    print(f"Max: {max_value}")
    print(f"Min: {min_value}")
    print(f"All even: {all_even}")
else:
    print("Error Invalid input")
    exit()

#  Problem 5: Loan eligibility (income and debt ratio)

"""

Descripción:
Determina si una persona es elegible para un préstamo con base en:
- monthly_income (float)
- monthly_debt (float)
- credit_score (int)
La regla es:
- debt_ratio = monthly_debt / monthly_income
- eligible es true si:
  - monthly_income >= 8000.0 AND
  - debt_ratio <= 0.4 AND
  - credit_score >= 650

Entradas:
- monthly_income (float; ingreso mensual).
- monthly_debt (float; pagos mensuales de deuda).
- credit_score (int; puntaje de crédito).

Salidas:
- "Debt ratio:" <debt_ratio>
- "Eligible:" true|false

Validaciones:
- monthly_income > 0.0 (evitar división entre cero).
- monthly_debt >= 0.0
- credit_score >= 0
- Si no se cumple, mostrar "Error: invalid input".

Operaciones clave sugeridas:
- Cálculo de deuda relativa: debt_ratio = monthly_debt / monthly_income
- Booleano: eligible = (monthly_income >= 8000.0 and debt_ratio <= 0.4 and credit_score >= 650)
"""

monthly_income = float(input("Enter your monthly income: "))
monthly_debt = float(input("Enter your monthly debt payments: "))
credit_score = int(input("Enter your credit score: "))

if monthly_income <= 0.0 or monthly_debt < 0.0 or credit_score < 0:
    print("Error: invalid input")
    exit()
else:
    debt_ratio = monthly_debt / monthly_income
    eligible = (monthly_income >= 8000.0 and debt_ratio <= 0.4 and credit_score >= 650)
    print(f"Debt ratio: {debt_ratio}")
    print(f"Eligible: {eligible}")



# Problem 6: Body Mass Index (BMI) and category flag

"""
Descripción:
Calcula el índice de masa corporal (BMI) de una persona con la fórmula:
- bmi = weight_kg / (height_m * height_m)
Además, genera booleanos para indicar:
- is_underweight (bmi < 18.5)
- is_normal (18.5 <= bmi < 25.0)
- is_overweight (bmi >= 25.0)

Entradas:
- weight_kg (float; peso en kilogramos).
- height_m (float; estatura en metros).

Salidas:
- "BMI:" <bmi_redondeado>
- "Underweight:" true|false
- "Normal:" true|false
- "Overweight:" true|false

Validaciones:
- weight_kg > 0.0
- height_m > 0.0
- Si no se cumple, mostrar "Error: invalid input".

Operaciones clave sugeridas:
- Cálculo de bmi como float.
- Uso de round(bmi, 2) para mostrar 2 decimales.
- Evaluación de rangos con condiciones encadenadas.

"""
    
weight_kg = float(input("Enter your weight in kg: "))
height_m = float(input("Enter your height in meters: "))

if weight_kg <= 0.0 or height_m <= 0.0:
    print("Error: invalid input")
    exit()
else:
    bmi = weight_kg / (height_m * height_m)
    bmi_redondeado = round(bmi, 2)
    is_underweight = (bmi < 18.5)
    is_normal = (18.5 <= bmi < 25.0)
    is_overweight = (bmi >= 25.0)

    print(f"BMI: {bmi_redondeado}")
    print(f"Underweight: {is_underweight}")
    print(f"Normal: {is_normal}")
    print(f"Overweight: {is_overweight}")


