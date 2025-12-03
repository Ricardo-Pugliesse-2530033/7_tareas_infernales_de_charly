"""
Nombre del estudiante : Ricardo Martin Pugliesse Macías
Matrícula             : 2530033
Grupo                 : IM 1-2


RESUMEN EJECUTIVO

En Python, los tipos int y float se utilizan para
representar cantidades numéricas: int para valores
enteros y float para valores con decimales. Los
booleanos (True y False) se obtienen a partir de
comparaciones y expresan condiciones lógicas que se
usan en estructuras de decisión como if, and, or y
not. Es importante validar rangos (por ejemplo,
evitar edades negativas o divisiones entre cero)
para prevenir errores de ejecución y resultados
ilógicos. Este documento presenta seis problemas que
usan enteros, flotantes y booleanos para convertir
temperaturas, calcular pagos, decidir descuentos,
obtener estadísticas, evaluar elegibilidad para
préstamos y clasificar el índice de masa corporal,
incluyendo validaciones y casos de prueba.


PRINCIPIOS Y BUENAS PRÁCTICAS

- Usar tipos apropiados: int para contadores y
    cantidades discretas, float para valores con
    decimales como salarios o promedios.
- Evitar duplicar expresiones complejas guardando
    resultados intermedios en variables claras.
- Validar datos antes de operar: no permitir horas,
    salarios o ingresos negativos y evitar divisiones
    entre cero.
- Usar nombres de variables descriptivos y mensajes
    en pantalla claros para el usuario, siempre en
    inglés según la convención.
- Documentar qué significa true y false en cada
    contexto para que el código sea fácil de entender.


Problem 1: Temperature converter and range flag

Descripción:
Convierte una temperatura en grados Celsius (float) a Fahrenheit y Kelvin.
Además, determina un valor booleano is_high_temperature que sea true si la
temperatura en Celsius es mayor o igual que 30.0 y false en caso contrario.

Entradas:
- temp_c (float; temperatura en °C).

Salidas:
- "Fahrenheit:" <temp_f>
- "Kelvin:" <temp_k>
- "High temperature:" true|false

Validaciones:
- Verificar que temp_c pueda convertirse a float.
- No permitir temperaturas físicas imposibles en Kelvin (por ejemplo, temp_k < 0.0).

Casos de prueba:
1) Normal: temp_c = 25.0 -> Fahrenheit: 77.0, Kelvin: 298.15, High temperature: false.
2) Borde: temp_c = 30.0 -> High temperature: true.
3) Error: temp_c que produzca Kelvin < 0.0 -> mensaje de error.
"""

temp_c_text = input("Write temperature in Celsius: ")

try:
        temp_c = float(temp_c_text)
except ValueError:
        print("Error: invalid input")
else:
        temp_f = temp_c * 9 / 5 + 32
        temp_k = temp_c + 273.15
        is_high_temperature = temp_c >= 30.0

        if temp_k < 0.0:
                print("Error: invalid temperature (Kelvin below 0)")
        else:
                print(f"In Celsius: {temp_c}")
                print(f"Fahrenheit: {temp_f}")
                print(f"Kelvin: {temp_k}")
                print(f"High temperature: {is_high_temperature}")



# Problem 2: Work hours and overtime payment

"""
Problem 2: Work hours and overtime payment

Descripción:
Calcula el pago total semanal de un trabajador. Hasta 40 horas se pagan a
hourly_rate (float). Las horas extra (> 40) se pagan al 150% de la tarifa
normal. Además, genera un booleano has_overtime que indique si el trabajador
hizo horas extra.

Entradas:
- hours_worked (float; horas trabajadas en la semana).
- hourly_rate (float; pago por hora).

Salidas:
- "Regular pay:" <regular_pay>
- "Overtime pay:" <overtime_pay>
- "Total pay:" <total_pay>
- "Has overtime:" true|false

Validaciones:
- hours_worked >= 0.
- hourly_rate > 0.
- Si alguno no cumple, mostrar "Error: invalid input".

Casos de prueba:
1) Normal: hours_worked = 38, hourly_rate = 100 -> solo pago regular.
2) Borde: hours_worked = 40, hourly_rate = 100 -> sin horas extra.
3) Error: hours_worked = -5 o hourly_rate = 0 -> mensaje de error.
"""

hours_worked_text = input("Enter hours worked: ")
hourly_rate_text = input("Enter hourly rate: ")

try:
    hours_worked = float(hours_worked_text)
    hourly_rate = float(hourly_rate_text)
except ValueError:
    print("Error: invalid input")
else:
    if hours_worked < 0.0 or hourly_rate <= 0.0:
        print("Error: invalid input")
    else:
        has_overtime = hours_worked > 40.0
        regular_hours = min(hours_worked, 40.0)
        overtime_hours = max(hours_worked - 40.0, 0.0)

        regular_pay = regular_hours * hourly_rate
        overtime_pay = overtime_hours * hourly_rate * 1.5
        total_pay = regular_pay + overtime_pay

        print(f"Regular pay: {regular_pay}")
        print(f"Overtime pay: {overtime_pay}")
        print(f"Total pay: {total_pay}")
        print(f"Has overtime: {has_overtime}")



# Problem 3: Discount eligibility with booleans

"""
Problem 3: Discount eligibility with booleans

Descripción:
Determina si un cliente obtiene un descuento en su compra. La regla es:
hay descuento si is_student es true o is_senior es true o si purchase_total
es mayor o igual a 1000.0. Cuando aplica descuento, se reduce 10% el total.

Entradas:
- purchase_total (float; total de la compra).
- is_student_text (string; "YES" o "NO").
- is_senior_text (string; "YES" o "NO").

Salidas:
- "Discount eligible:" true|false.
- "Final total:" <final_total>.

Validaciones:
- purchase_total >= 0.0.
- Normalizar is_student_text e is_senior_text a mayúsculas y convertir a
    booleanos is_student, is_senior.
- Si el texto no es "YES" ni "NO", mostrar "Error: invalid input".

Casos de prueba:
1) Normal: purchase_total = 1200, NO estudiante, NO senior -> descuento.
2) Borde: purchase_total = 1000, estudiante = NO, senior = NO -> descuento.
3) Error: texto distinto de YES/NO -> mensaje de error.
"""

purchase_total_text = input("Enter your purchase amount: ")

try:
    purchase_total = float(purchase_total_text)
except ValueError:
    print("Error: invalid input")
else:
    if purchase_total < 0.0:
        print("Error: invalid input")
    else:
        print("Answer the following questions with YES or NO")
        is_student_text = input("Are you a student? ")
        is_senior_text = input("Are you a senior? ")

        is_student_text = is_student_text.strip().upper()
        is_senior_text = is_senior_text.strip().upper()

        if is_student_text not in ("YES", "NO") or is_senior_text not in ("YES", "NO"):
            print("Error: invalid input")
        else:
            is_student = is_student_text == "YES"
            is_senior = is_senior_text == "YES"
            discount_eligible = is_student or is_senior or (purchase_total >= 1000.0)

            if discount_eligible:
                final_total = purchase_total * 0.9
            else:
                final_total = purchase_total

            print(f"Discount eligible: {discount_eligible}")
            print(f"Final total: {final_total}")




# Problem 4: Basic statistics of three integers


"""
Problem 4: Basic statistics of three integers

Descripción:
Lee tres números enteros y calcula: suma, promedio (float), valor máximo,
valor mínimo y un booleano all_even que indique si los tres números son
pares.

Entradas:
- n1 (int).
- n2 (int).
- n3 (int).

Salidas:
- "Sum:" <sum_value>.
- "Average:" <average_value>.
- "Max:" <max_value>.
- "Min:" <min_value>.
- "All even:" true|false.

Validaciones:
- Verificar que los tres valores se puedan convertir a int.
- Se permiten valores negativos.

Casos de prueba:
1) Normal: 2, 4, 6 -> Sum: 12, Average: 4.0, Max: 6, Min: 2, All even: true.
2) Borde: 1, 2, 3 -> All even: false.
3) Error: entrada no numérica -> mensaje de error.
"""

try:
    n1 = int(input("Enter first integer: "))
    n2 = int(input("Enter second integer: "))
    n3 = int(input("Enter third integer: "))
except ValueError:
    print("Error: invalid input")
else:
    sum_value = n1 + n2 + n3
    average_value = sum_value / 3.0
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)
    all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)

    print(f"Sum: {sum_value}")
    print(f"Average: {average_value}")
    print(f"Max: {max_value}")
    print(f"Min: {min_value}")
    print(f"All even: {all_even}")

#  Problem 5: Loan eligibility (income and debt ratio)

"""
Problem 5: Loan eligibility (income and debt ratio)

Descripción:
Determina si una persona es elegible para un préstamo con base en su ingreso
mensual, su deuda mensual y su puntaje de crédito. Se calcula debt_ratio como
monthly_debt / monthly_income y se considera elegible si se cumplen
condiciones mínimas.

Entradas:
- monthly_income (float; ingreso mensual).
- monthly_debt (float; pagos mensuales de deuda).
- credit_score (int; puntaje de crédito).

Salidas:
- "Debt ratio:" <debt_ratio>.
- "Eligible:" true|false.

Validaciones:
- monthly_income > 0.0 (evitar división entre cero).
- monthly_debt >= 0.0.
- credit_score >= 0.

Casos de prueba:
1) Normal: income = 9000, debt = 3000, score = 700 -> elegible.
2) Borde: income = 8000, debt = 3200, score = 650 -> debt_ratio = 0.4.
3) Error: income = 0 o debt < 0 -> mensaje de error.
"""

monthly_income_text = input("Enter your monthly income: ")
monthly_debt_text = input("Enter your monthly debt payments: ")
credit_score_text = input("Enter your credit score: ")

try:
    monthly_income = float(monthly_income_text)
    monthly_debt = float(monthly_debt_text)
    credit_score = int(credit_score_text)
except ValueError:
    print("Error: invalid input")
else:
    if monthly_income <= 0.0 or monthly_debt < 0.0 or credit_score < 0:
        print("Error: invalid input")
    else:
        debt_ratio = monthly_debt / monthly_income
        eligible = (
            monthly_income >= 8000.0
            and debt_ratio <= 0.4
            and credit_score >= 650
        )
        print(f"Debt ratio: {debt_ratio}")
        print(f"Eligible: {eligible}")



# Problem 6: Body Mass Index (BMI) and category flag

"""
Problem 6: Body Mass Index (BMI) and category flag

Descripción:
Calcula el índice de masa corporal (BMI) de una persona con la fórmula
bmi = weight_kg / (height_m * height_m). Además, genera booleanos que
indican si la persona está por debajo del peso, en rango normal o con
sobrepeso.

Entradas:
- weight_kg (float; peso en kilogramos).
- height_m (float; estatura en metros).

Salidas:
- "BMI:" <bmi_redondeado>.
- "Underweight:" true|false.
- "Normal:" true|false.
- "Overweight:" true|false.

Validaciones:
- weight_kg > 0.0.
- height_m > 0.0.

Casos de prueba:
1) Normal: weight_kg = 70, height_m = 1.75 -> BMI ~ 22.86, Normal: true.
2) Borde: BMI exactamente 18.5 o 25.0 -> cambio de categoría.
3) Error: weight_kg <= 0 o height_m <= 0 -> mensaje de error.
"""

weight_kg_text = input("Enter your weight in kg: ")
height_m_text = input("Enter your height in meters: ")

try:
    weight_kg = float(weight_kg_text)
    height_m = float(height_m_text)
except ValueError:
    print("Error: invalid input")
else:
    if weight_kg <= 0.0 or height_m <= 0.0:
        print("Error: invalid input")
    else:
        bmi = weight_kg / (height_m * height_m)
        bmi_rounded = round(bmi, 2)
        is_underweight = bmi < 18.5
        is_normal = 18.5 <= bmi < 25.0
        is_overweight = bmi >= 25.0

        print(f"BMI: {bmi_rounded}")
        print(f"Underweight: {is_underweight}")
        print(f"Normal: {is_normal}")
        print(f"Overweight: {is_overweight}")


"""
CONCLUSIONES

Los tipos int y float permiten modelar cantidades
reales de muchos problemas cotidianos, desde
temperaturas hasta salarios y deudas. Las
comparaciones generan valores booleanos que hacen
posible tomar decisiones con sentencias if y
combinaciones de and, or y not. Validar rangos y
evitar divisiones entre cero es fundamental para
prevenir errores de ejecución y resultados
inconsistentes. El diseño de condiciones compuestas
permite expresar reglas de negocio reales como las
que se usan en nómina, descuentos o préstamos.
Estos patrones se repiten en muchos programas y son
la base para resolver problemas más complejos.


REFERENCIAS

1) Python documentation - Built-in Types:
   Numeric Types — int, float, complex.
2) Python documentation - Boolean type — bool.
3) Python Tutorial - Numbers and Booleans,
   docs.python.org.
4) Sweigart, A. "Automate the Boring Stuff with
   Python", capítulos de operadores y lógica.
5) Tutoriales y apuntes de clase sobre validación
   de datos numéricos y estructuras de decisión.


REPOSITORIO DE GITHUB

URL del repositorio:
https://github.com/Ricardo-Pugliesse-2530033/7_tareas_infernales_de_charly


"""


