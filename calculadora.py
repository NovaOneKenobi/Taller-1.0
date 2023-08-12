def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b



while True:
    print("Opciones:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("5. Salir")

    opcion = input("Ingrese el número de la operación que desea realizar: ")

    if opcion == '5':
        print("Saliendo de la calculadora...")
        break

    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    if opcion == '1':
        print("Resultado:", sumar(num1, num2))

    elif opcion == '2':
        print("Resultado:", restar(num1, num2))

    elif opcion == '3':
        print("Resultado:", multiplicar(num1, num2))

    else:
        print("Opción inválida")


