# Ejercicio 2: Modelar una computadora
# 
# En este archivo debés crear la clase Computadora siguiendo las consignas del README.
# Recordá:
# - Definir atributos relevantes en el constructor (__init__), con valores por defecto.
# - Implementar el método __str__ para mostrar la información esencial.
# - Instanciar al menos 3 computadoras con distintos valores.
# - Llevar la cuenta de computadoras creadas (usar variable de clase).
# - Implementar al menos 2 métodos de los sugeridos (updateOS, PM, addRAM, getCapacity).
# - Crear otra clase para un componente (ej: Disco, RAM, etc.) con su propio __init__, __str__ y al menos un método.
# 
# ¡No olvides probar todos los métodos y comentar tu criterio para los valores

"""
En este ejercicio vamos a modelar una computadora, creando la clase `Computadora` para ello.

- El método `__str__` nos ayuda a conocer la información esencial de nuestros objetos. ¡Implementalo! Recordá que siempre debería estar presente en las clases que creás.

- Instanciá 3 computadoras y asignales distintos valores a sus atributos.

> Nota: Pedile ayuda a tu monitor para pensar cómo implementar los métodos solicitados. Pensá en aquellos atributos creados u otros adicionales que les den funcionalidad y practicidad a dichos métodos. Si es necesario, podés investigar el uso de `datetime` u otra librería que requieras. Recordá informar siempre al usuario sobre las acciones realizadas en el sistema. Probá todos los métodos creados para testear su funcionamiento.

- Elegí algún componente de hardware o software de la máquina (atributo) y dale identidad. Para ello, creá otra clase, definí el constructor, el `__str__` y pensá en al menos una función que sea aplicable al componente elegido. Codificá el/los métodos pensados. ¿Qué acciones realizan los métodos elegidos sobre los atributos? ¿Una lectura (read)? ¿Una escritura (write)? ¿Una ejecución (exec)?

"""

class Computadora:
    conteoComputadora = 0
    posiblesSistOperativos = ['Windows 11', 'macOs']

    def __init__(self, marca:str, modelo:str, memoriaRAM:int, almacenamiento: int, procesador: str, sistemaOperativo = 'Windows 11'):
        self.marca = self.validar_cadena(marca)
        self.modelo = self.validar_cadena(modelo)
        self.memoriaRAM = memoriaRAM
        self.almacenamiento = almacenamiento
        self.procesador = self.validar_cadena(procesador)
        self.sistemaOperativo = self.validar_cadena(sistemaOperativo)
        Computadora.conteoComputadora += 1

    def __str__(self):
        return f'Computadora: {self.marca}, {self.modelo} (Almacenamiento: {self.almacenamiento}, RAM: {self.memoriaRAM}, CPU: {self.procesador}, OS: {self.sistemaOperativo})'
    
    def validar_cadena(self,cadena):
        if not isinstance(cadena, str):
            raise TypeError(f"{cadena} debe ser una cadena de texto")
        if len(cadena)<1:
            raise ValueError(f"{cadena} no puede ser una cadena vacía")
        return cadena

    def updateOS(self, nueva_version):
        self.sistemaOperativo = nueva_version
        print(f"Sistema operativo actualizado a {self.sistemaOperativo}")

    def addRAM(self, cantidad_gb):
        if cantidad_gb > 0:
            self.memoriaRAM += cantidad_gb
            print(f'Se ha instalado {cantidad_gb}GB de RAM. Memoria actualizada: {self.memoriaRAM}')
        else:
            print("Error: la cantidad de RAM debe ser un número positivo") 

    def getter_capacity(self):
        print(f"La capacidad de almacenamietno es: {self.almacenamiento} gb")
        return self.almacenamiento
    

    @classmethod
    def mostrar_conteo (cls):
        print(f'El número de computadoras es {cls.conteoComputadora}')


if __name__ == '__main__':
    try:
        lenovo1 = Computadora("Lenovo", "ThinkPad T14s", 16, 250, "Intel i8")
        mac1 = Computadora("Apple", "Mac Air", 16, 512, "Apple Silicon", "macOs")
        dell1 = Computadora("Dell", "Dell 123", 8, 256, "Intel i9")

        print(lenovo1)
        print(mac1)

        lenovo1.addRAM(8)
        mac1.updateOS("Mac Sonoma")
        dell1.getter_capacity()

    except ValueError as e:
        print("El error es", e)
    except TypeError as e:
        print("El error es", e)
    except Exception as e:
        print("El error es", e)
