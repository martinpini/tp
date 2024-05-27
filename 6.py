# . Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los
# siguientes métodos para la clase:
#  Un constructor, donde los datos pueden estar vacíos.
#  Los setters y getters para cada uno de los atributos. Hay que validar las entradas de
# datos.
#  mostrar(): Muestra los datos de la persona.
#  Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.

class Persona:
    """
    Clase Persona para representar a una persona con sus datos básicos.

    Atributos:
        nombre (str): El nombre de la persona.
        edad (int): La edad de la persona.
        dni (str): El DNI de la persona.
    """

    def __init__(self, nombre="", edad=0, dni=""):
        """
        Constructor de la clase Persona.

        Parámetros:
            nombre (str, opcional): El nombre de la persona (por defecto "").
            edad (int, opcional): La edad de la persona (por defecto 0).
            dni (str, opcional): El DNI de la persona (por defecto "").
        """
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

        # Validar los datos al crear la instancia
        self.validar_datos()

    def validar_datos(self):
        """
        Valida los datos de la persona (nombre, edad y DNI).

        Si algún dato no cumple las condiciones, se solicita al usuario que lo ingrese nuevamente.
        """
        self.validar_nombre()
        self.validar_edad()
        self.validar_dni()

    def validar_nombre(self):
        """
        Función auxiliar para validar el nombre (interna).
        """
        while True:
            nombre = input("Ingrese el nombre de la persona: ").strip()
            if not nombre or not nombre.isalpha() or len(nombre) > 35:
                print("El nombre no puede estar vacío, debe contener solo letras y tener máximo 35 caracteres.")
            else:
                self.nombre = nombre
                break

    def validar_edad(self):
        """
        Función auxiliar para validar la edad (interna).
        """
        while True:
            try:
                edad = int(input("Ingrese la edad de la persona: "))
                if 1 <= edad <= 100:
                    self.edad = edad
                    break
                else:
                    print("La edad debe estar en el rango de 1 a 100.")
            except ValueError:
                print("Error: La edad debe ser un número entero.")

    def validar_dni(self):
        """
        Función auxiliar para validar el DNI (interna).
        """
        while True:
            dni = input("Ingrese el DNI de la persona: ").strip()
            if not dni.isdigit() or len(dni) != 8:
                print("El DNI debe contener exactamente 8 dígitos.")
            else:
                self.dni = dni
                break

    def mostrar(self):
        """
        Muestra los datos de la persona.
        """
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"DNI: {self.dni}")

    def es_mayor_de_edad(self):
        """
        Devuelve un valor lógico indicando si es mayor de edad.

        Retorno:
            bool: True si es mayor de edad, False en caso contrario.
        """
        return self.edad >= 18

def realizar_otra_carga():
    """
    Pregunta al usuario si desea realizar otra carga de datos.

    Retorno:
        bool: True si el usuario desea realizar otra carga, False en caso contrario.
    """
    respuesta = input("¿Desea realizar otra carga de datos? (si/no): ").lower()
    return respuesta == "si"

def main():
    """
    Función principal para interactuar con el usuario.
    """
    while True:
        persona = Persona()

        persona.mostrar()

        if persona.es_mayor_de_edad():
            print("Es mayor de edad.")
        else:
            print("Es menor de edad.")

        if not realizar_otra_carga():
            print("Gracias por usar el programa. ¡Hasta la próxima!")
            break

if __name__ == "__main__":
    main()
