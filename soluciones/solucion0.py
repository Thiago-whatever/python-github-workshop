# Solución al Ejercicio 0: Suma de dos números
# ---------------------------------------------

# Solicitar el primer número al usuario
while True:
    try:
        num1 = int(input("Ingrese el primer número entero: "))
        break
    except ValueError:
        print("Por favor, ingrese un número válido.")

# Solicitar el segundo número al usuario
while True:
    try:
        num2 = int(input("Ingrese el segundo número entero: "))
        break
    except ValueError:
        print("Por favor, ingrese un número válido.")

# Calcular la suma
resultado = num1 + num2

# Imprimir el resultado
print(f"La suma de {num1} y {num2} es: {resultado}")
