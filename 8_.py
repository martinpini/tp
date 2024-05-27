class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        self.titular = titular
        self.cantidad = cantidad

    def retirar(self, cantidad):
        if cantidad > self.cantidad:
            print("Fondos insuficientes.")
        else:
            self.cantidad -= cantidad

class Persona:
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0.0, bonificacion=0.0):
        # Inicializa los atributos de la cuenta joven heredando de Cuenta
        super().__init__(titular, cantidad)
        self._bonificacion = bonificacion

    @property
    def bonificacion(self):
        # Getter para la bonificación
        return self._bonificacion

    @bonificacion.setter
    def bonificacion(self, valor):
        # Setter para la bonificación
        self._bonificacion = valor

    def es_titular_valido(self):
        # Devuelve True si el titular es mayor de edad pero menor de 25 años
        return 18 <= self.titular.edad < 25

    def retirar(self, cantidad):
        # Permite retirar dinero sólo si el titular es válido
        if self.es_titular_valido():
            super().retirar(cantidad)
        else:
            print("El titular no es válido para retirar dinero.")

    def mostrar(self):
        # Muestra los datos de la cuenta joven
        print(f"Cuenta Joven\nTitular: {self.titular.nombre}, Cantidad: {self.cantidad}, Bonificación: {self.bonificacion}%")

# Ejemplo de uso
titular_joven = Persona("Ana", 22, "43654300")
cuenta_joven = CuentaJoven(titular_joven, 200.0, 10)
cuenta_joven.mostrar()  # Salida: Cuenta Joven\nTitular: Ana, Cantidad: 200.0, Bonificación: 10%
print(cuenta_joven.es_titular_valido())  # Salida: True
cuenta_joven.retirar(50)
cuenta_joven.mostrar()  # Salida: Cuenta Joven\nTitular: Ana, Cantidad: 150.0, Bonificación: 10%
