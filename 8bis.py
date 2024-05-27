# Definición de las clases Persona, Cuenta y CuentaJoven

class Persona:
    """
    Clase Persona para representar a una persona con sus datos básicos.
    """

    def __init__(self, nombre="", edad=0, dni=""):
        """
        Constructor de la clase Persona.
        """
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def validar_nombre(self):
        """
        Valida si el nombre es válido (solo texto, entre 3 y 35 caracteres).
        """
        while True:
            nombre = input("Ingrese el nombre de la persona: ")
            if nombre.isalpha() and 3 <= len(nombre) <= 35:
                self.nombre = nombre
                break
            else:
                print("El nombre debe contener solo letras y tener entre 3 y 35 caracteres.")

    def validar_edad(self):
        """
        Valida si la edad es válida (entre 1 y 100).
        """
        while True:
            try:
                edad = int(input("Ingrese la edad de la persona: "))
                if 1 <= edad <= 100:
                    self.edad = edad
                    break
                else:
                    print("La edad debe estar entre 1 y 100 años.")
            except ValueError:
                print("Por favor, ingrese un número entero para la edad.")

    def validar_dni(self):
        """
        Valida si el DNI es válido (solo números, longitud 8).
        """
        while True:
            dni = input("Ingrese el DNI de la persona: ")
            if dni.isdigit() and len(dni) == 8:
                self.dni = dni
                break
            else:
                print("El DNI debe contener exactamente 8 dígitos numéricos.")

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
        """
        return self.edad >= 18

class Cuenta:
    """
    Clase Cuenta para representar una cuenta bancaria con un titular y una cantidad.
    """

    def __init__(self, titular=None, cantidad=0.0):
        """
        Constructor de la clase Cuenta.
        """
        self.titular = titular
        self.cantidad = cantidad

    def depositar(self, cantidad):
        """
        Deposita una cantidad de dinero en la cuenta.
        """
        self.cantidad += cantidad

    def retirar(self, cantidad):
        """
        Retira una cantidad de dinero de la cuenta.
        Retorna True si la retirada fue exitosa, False si no se pudo realizar.
        """
        if self.cantidad >= cantidad:
            self.cantidad -= cantidad
            return True
        else:
            print("Saldo insuficiente")
            return False

    def mostrar(self):
        """
        Muestra información sobre la cuenta.
        """
        print(f"Titular: {self.titular.nombre}")
        print(f"Cantidad disponible: {self.cantidad}")

class CuentaJoven(Cuenta):
    """
    Clase CuentaJoven que representa una cuenta bancaria para jóvenes.
    """

    def __init__(self, titular=None, cantidad=0.0, bonificacion=0.0):
        """
        Constructor de la clase CuentaJoven.
        """
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion

    def set_bonificacion(self, bonificacion):
        """
        Establece la bonificación de la cuenta.
        """
        self.bonificacion = bonificacion

    def get_bonificacion(self):
        """
        Obtiene la bonificación de la cuenta.
        """
        return self.bonificacion

    def es_titular_valido(self):
        """
        Verifica si el titular de la cuenta es mayor de edad pero menor de 25 años.
        """
        return self.titular.es_mayor_de_edad() and self.titular.edad < 25

    def retirar(self, cantidad):
        """
        Retira una cantidad de dinero de la cuenta, si el titular es válido.
        """
        if self.es_titular_valido():
            return super().retirar(cantidad)
        else:
            print("El titular no es válido para retirar dinero.")
            return False

    def mostrar(self):
        """
        Muestra información sobre la cuenta joven.
        """
        print(f"Cuenta Joven\nBonificación: {self.bonificacion}")


# Programa principal para interactuar con las clases

def cargar_persona():
    """
    Carga los datos de una persona y valida cada campo.
    """
    persona = Persona()
    persona.validar_nombre()
    persona.validar_edad()
    persona.validar_dni()
    return persona

def realizar_operaciones():
    """
    Realiza operaciones con cuentas hasta que el usuario decida salir.
    """
    while True:
        # Crear una instancia de Persona
        print("\nCargar datos de la persona:")
        persona = cargar_persona()

        # Crear una instancia de Cuenta
        cantidad_inicial = float(input("Ingrese la cantidad inicial de la cuenta: "))
        cuenta_normal = Cuenta(persona, cantidad_inicial)

        # Crear una instancia de CuentaJoven
        bonificacion_cuenta_joven = float(input("Ingrese la bonificación de la cuenta joven (%): "))
        cuenta_joven = CuentaJoven(persona, cantidad_inicial, bonificacion_cuenta_joven)

        # Interacción con las cuentas
        print("\nOperaciones con la cuenta normal:")
        cuenta_normal.mostrar()
        print("1. Depositar dinero")
        print("2. Retirar dinero")
        print("3. Mostrar información de la cuenta")
        opcion = int(input("Seleccione una opción (1/2/3): "))

        if opcion == 1:
            cantidad_deposito = float(input("Ingrese la cantidad a depositar: "))
            cuenta_normal.depositar(cantidad_deposito)
            print("Depósito realizado con éxito.")
        elif opcion == 2:
            cantidad_retiro = float(input("Ingrese la cantidad a retirar: "))
            cuenta_normal.retirar(cantidad_retiro)
        elif opcion == 3:
            cuenta_normal.mostrar()

        print("\nOperaciones con la cuenta joven:")
        cuenta_joven.mostrar()
        print("1. Depositar dinero")
        print("2. Retirar dinero")
        print("3. Mostrar información de la cuenta")
        opcion = int(input("Seleccione una opción (1/2/3): "))

        if opcion == 1:
            cantidad_deposito = float(input("Ingrese la cantidad a depositar: "))
            cuenta_joven.depositar(cantidad_deposito)
            print("Depósito realizado con éxito.")
        elif opcion == 2:
            cantidad_retiro = float(input("Ingrese la cantidad a retirar: "))
            cuenta_joven.retirar(cantidad_retiro)
        elif opcion == 3:
            cuenta_joven.mostrar()

        continuar = input("¿Desea realizar más operaciones? (s/n): ")
        if continuar.lower() != 's':
            break

    print("¡Gracias por utilizar nuestro programa!")

# Iniciar el programa principal
realizar_operaciones()
