# Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase
# CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase,
# además del titular y la cantidad se debe guardar una bonificación que estará expresada en
# tanto por ciento. Crear los siguientes métodos para la clase:
#  Un constructor.
#  Los setters y getters para el nuevo atributo.
#  En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo
# tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es
# mayor de edad pero menor de 25 años y falso en caso contrario.
#  Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
#  El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la
# cuenta

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

# Crear una instancia de Persona
nombre_persona = input("Ingrese el nombre de la persona: ")
edad_persona = int(input("Ingrese la edad de la persona: "))
dni_persona = input("Ingrese el DNI de la persona: ")
persona = Persona(nombre_persona, edad_persona, dni_persona)

# Crear una instancia de Cuenta
cantidad_inicial = float(input("Ingrese la cantidad inicial de la cuenta: "))
cuenta_normal = Cuenta(persona, cantidad_inicial)

# Crear una instancia de CuentaJoven
bonificacion_cuenta_joven = float(input("Ingrese la bonificación de la cuenta joven (%): "))
cuenta_joven = CuentaJoven(persona, cantidad_inicial, bonificacion_cuenta_joven)

# Interacción con las cuentas
print("\nOperaciones con la cuenta normal:")
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
