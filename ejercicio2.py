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


> Nota: Pedile ayuda a tu monitor para pensar cómo implementar los métodos solicitados. Pensá en aquellos atributos creados u otros adicionales que les den funcionalidad y practicidad a dichos métodos. Si es necesario, podés investigar el uso de `datetime` u otra librería que requieras. Recordá informar siempre al usuario sobre las acciones realizadas en el sistema. Probá todos los métodos creados para testear su funcionamiento.

- Elegí algún componente de hardware o software de la máquina (atributo) y dale identidad. Para ello, creá otra clase, definí el constructor, el `__str__` y pensá en al menos una función que sea aplicable al componente elegido. Codificá el/los métodos pensados. ¿Qué acciones realizan los métodos elegidos sobre los atributos? ¿Una lectura (read)? ¿Una escritura (write)? ¿Una ejecución (exec)?

"""
class Disco:
    def __init__ (self, capacidad_gb: int, espacio_ocupado: int, tipo = 'SSD'):
        self.capacidad_gb = capacidad_gb
        self.espacio_ocupado = espacio_ocupado
        self.tipo = self.validar_cadena(tipo)
    
    def __str__(self):
        return f'Disco con capacidad de {self.capacidad_gb}GB, tipo {self.tipo}, disponibles {self.espacioDisponible()}GB'
    
    def vaciarDisco(self): #método de escritura
        self.espacio_ocupado = 0
        print("Disco formateado.")

    def espacioDisponible (self): #lectura de los atributos
        return self.capacidad_gb - self.espacio_ocupado
        
    def validar_cadena(self,cadena):
        if not isinstance(cadena, str):
            raise TypeError(f"{cadena} debe ser una cadena de texto")
        if len(cadena)<1:
            raise ValueError(f"{cadena} no puede ser una cadena vacía")
        return cadena
    
class Computadora:
    conteoComputadora = 0
    posiblesSistOperativos = ['Windows 11', 'macOs']

    def __init__(self, marca:str, modelo:str, memoriaRAM:int, procesador: str, disco: Disco, sistemaOperativo = 'Windows 11'):
        self.marca = self.validar_cadena(marca)
        self.modelo = self.validar_cadena(modelo)
        self.memoriaRAM = memoriaRAM
        self.disco = disco
        self.procesador = self.validar_cadena(procesador)
        self.sistemaOperativo = self.validar_cadena(sistemaOperativo)
        Computadora.conteoComputadora += 1

    def __str__(self):
        return f'Computadora: {self.marca}, {self.modelo} (Almacenamiento: {self.disco},RAM: {self.memoriaRAM}, CPU: {self.procesador}, OS: {self.sistemaOperativo})'
    
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
        print(f"La capacidad del disco es: {self.disco.capacidad_gb} gb")
        return self.disco.capacidad_gb
    
    @classmethod
    def mostrar_conteo (cls):
        print(f'El número de computadoras es {cls.conteoComputadora}')


if __name__ == '__main__':
    try:
        discoLenovo = Disco(256, 120)
        discoMac = Disco(512, 352)
        discoDell = Disco(128, 70)

        lenovo1 = Computadora("Lenovo", "ThinkPad T14s", 16, "Intel i8", discoLenovo)
        mac1 = Computadora("Apple", "Mac Air", 16, "Apple Silicon", discoMac, "macOs")
        dell1 = Computadora("Dell", "Dell 123", 8, "Intel i9", discoDell)

        print(lenovo1, '\n')
        print(mac1,'\n')
        print(dell1, '\n')

        lenovo1.addRAM(8)
        print('\n')
        mac1.updateOS("Mac Sonoma")
        print('\n')
        dell1.getter_capacity()

        #probando método de clase Disco, vaciando la capacidad utilizada del mismo
        discoLenovo.vaciarDisco()
        print(lenovo1)

        print(f"Cantidad de computadoras: {Computadora.conteoComputadora}")

    except ValueError as e:
        print("El error es", e)
    except TypeError as e:
        print("El error es", e)
    except Exception as e:
        print("El error es", e)
