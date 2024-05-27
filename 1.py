def mcd(a, b):
    """
    Calcula el Máximo Común Divisor (MCD) de dos números enteros.

    Parámetros:
        a (int): El primer número entero.
        b (int): El segundo número entero.

    Retorno:
        int: El MCD de 'a' y 'b'.

    Ejemplo:
        mcd(12, 15) == 3
        mcd(24, 30) == 6
        mcd(48, 60) == 12
    """
    while b:
        a, b = b, a % b
    return a

def main():
    while True:
        try:
            # Solicitar números al usuario
            num1 = int(input("Ingrese el primer número entero: "))
            num2 = int(input("Ingrese el segundo número entero: "))

            # Calcular el MCD
            mcd_resultado = mcd(num1, num2)

            # Mostrar el resultado con explicación
            print(f"El Máximo Común Divisor (MCD) de {num1} y {num2} es: {mcd_resultado}")
            print(f"Explicación:")
            print(f"Se utiliza el algoritmo de Euclides, que consiste en dividir el número mayor por el menor y usar el residuo como nuevo divisor.")
            print(f"En este caso, se dividen {num1} por {num2} y se utiliza el residuo como nuevo divisor.")
            print(f"Este proceso se repite hasta que el residuo sea 0, en cuyo caso el valor del divisor actual es el MCD.")

            # Mostrar el MCD hallado
            print(f"El MCD hallado es: {mcd_resultado}")

            # Preguntar si el usuario desea continuar
            opcion = input("¿Desea realizar otra operación? (si/no): ").lower()

            # Controlar la respuesta del usuario
            if opcion == "si":
                continue  # Continúa el bucle para realizar otra operación
            else:
                print("¡Gracias por usar la calculadora de MCD!")
                break  # Sale del bucle y termina el programa

        except ValueError:
            print("Error: Debe ingresar números enteros válidos.")

if __name__ == "__main__":
    main()
