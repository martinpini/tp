# 7. Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es
# opcional. Crear los siguientes métodos para la clase:
#  Un constructor, donde los datos pueden estar vacíos.
#  Los setters y getters para cada uno de los atributos. El atributo no se puede modificar
# directamente, sólo ingresando o retirando dinero.
#  mostrar(): Muestra los datos de la cuenta.
#  ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es
# negativa, no se hará nada.
#  retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números
# rojos.

def cargar_personas():
    personas = {}
    with open("personas.txt", "r") as file:
        for line in file:
            nombre, edad, saldo = line.strip().split(",")
            personas[nombre] = [int(edad), float(saldo)]
    return personas

def guardar_personas(personas):
    with open("personas.txt", "w") as file:
        for nombre, datos in personas.items():
            file.write(f"{nombre},{datos[0]},{datos[1]}\n")

def mostrar_menu():
    print("\nMenú:")
    print("1. Mostrar datos de las personas.")
    print("2. Modificar saldo de una persona.")
    print("3. Salir.")
    return input("Ingrese el número de la opción deseada: ")

def mostrar_datos(personas):
    print("\nDatos de las personas:")
    for nombre, datos in personas.items():
        print(f"{nombre} - Edad: {datos[0]}, Saldo: {datos[1]}")

def modificar_saldo(personas):
    nombre = input("Ingrese el nombre de la persona: ")
    if nombre in personas:
        print(f"Saldo actual de {nombre}: {personas[nombre][1]}")
        opcion = input("¿Desea ingresar (i) o retirar (r) saldo? ")
        cantidad = float(input("Ingrese la cantidad: "))
        if opcion.lower() == "i":
            personas[nombre][1] += cantidad
        elif opcion.lower() == "r":
            personas[nombre][1] -= cantidad
        else:
            print("Opción inválida.")
    else:
        print("Persona no encontrada.")

def main():
    personas = cargar_personas()
    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            mostrar_datos(personas)
        elif opcion == "2":
            modificar_saldo(personas)
        elif opcion == "3":
            guardar_personas(personas)
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
