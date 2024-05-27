# Sabiendo que ValueError es la excepción que se lanza cuando 
# no podemos convertir una cadena de texto en su valor 
# numérico, escriba una función get_int() que lea un valor
# entero del usuario y lo devuelva, iterando mientras el 
# valor no sea correcto. Intente resolver el ejercicio 
# tanto de manera iterativa como recursiva.

def get_int_iterative():
    """
    Lee un valor entero del usuario y lo devuelve, iterando mientras el valor no sea correcto.

    Retorno:
        int: El valor entero ingresado por el usuario.
    """
    while True:
        try:
            num = int(input("Ingrese un número entero: "))
            return num
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")

def get_int_recursive():
    """
    Lee un valor entero del usuario y lo devuelve, iterando mientras el valor no sea correcto.

    Retorno:
        int: El valor entero ingresado por el usuario.
    """
    try:
        num = int(input("Ingrese un número entero: "))
        return num
    except ValueError:
        print("Error: Debe ingresar un número entero válido.")
        return get_int_recursive()

def main():
    # Pedir al usuario que elija una opción
    print("Elija una opción:")
    print("1. Función iterativa")
    print("2. Función recursiva")
    print("3. Salir")
    option = int(input("Ingrese un número: "))

    # Mostrar la función elegida y su explicación
    if option == 1:
        print("Función iterativa:")
        print("Esta función utiliza un bucle while para iterar mientras el valor ingresado por el usuario no sea un número entero válido.")
        print("Si el usuario ingresa un valor no numérico o un número decimal, la función muestra un mensaje de error y pide al usuario que ingrese un número entero válido de nuevo.")
        print("La función devuelve el valor entero ingresado por el usuario cuando este es válido.")
        num = get_int_iterative()
    elif option == 2:
        print("Función recursiva:")
        print("Esta función utiliza una llamada recursiva a sí misma para pedir al usuario que ingrese un número entero válido de nuevo en caso de que el valor ingresado no sea válido.")
        print("La función devuelve el valor entero ingresado por el usuario cuando este es válido.")
        num = get_int_recursive()
    elif option == 3:
        print("Saliendo del programa...")
        exit()
    else:
        print("Opción inválida. Por favor, elija una opción válida.")

    # Mostrar el resultado
    print(f"El número entero ingresado es: {num}")

    # Preguntar si desea continuar
    continuar = input("¿Desea continuar? (si/no): ").lower()
    if continuar == "si":
        main()
    elif continuar == "no":
        print("Saliendo del programa...")
        exit()
    else:
        print("Opción inválida. Por favor, elija una opción válida.")

if __name__ == "__main__":
    main()