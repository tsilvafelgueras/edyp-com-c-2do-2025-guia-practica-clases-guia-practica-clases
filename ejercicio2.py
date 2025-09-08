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

Primero, pensá un rato en todas las características que mirarías al momento de comprar una. ¿Cómo llamamos a esas características en el paradigma de la programación orientada a objetos?

Luego de pensarlo, continuá con la consigna.

- El objeto computadora debe ser instanciado con todos sus atributos pasados como parámetros al método constructor. Al momento de crear el equipo, asignales a los atributos valores por defecto. ¿Qué criterio tuviste en cuenta para elegir esos valores?

- El método `__str__` nos ayuda a conocer la información esencial de nuestros objetos. ¡Implementalo! Recordá que siempre debería estar presente en las clases que creás.

- Instanciá 3 computadoras y asignales distintos valores a sus atributos.

- ¿Cómo podrías llevar la cuenta de la cantidad de computadoras creadas? ¿Qué tipo de variable resuelve lo pedido?

- Implementá al menos 2 de los siguientes métodos en la clase Computadora:

  - `updateOS`: Actualiza el sistema operativo.
  - `PM`: Brinda un mantenimiento programado al hardware del equipo.
  - `addRAM`: Instala un nuevo módulo de RAM en la computadora.
  - `getCapacity`: Muestra la capacidad del componente de hardware que se desee conocer.

> Nota: Pedile ayuda a tu monitor para pensar cómo implementar los métodos solicitados. Pensá en aquellos atributos creados u otros adicionales que les den funcionalidad y practicidad a dichos métodos. Si es necesario, podés investigar el uso de `datetime` u otra librería que requieras. Recordá informar siempre al usuario sobre las acciones realizadas en el sistema. Probá todos los métodos creados para testear su funcionamiento.

- Elegí algún componente de hardware o software de la máquina (atributo) y dale identidad. Para ello, creá otra clase, definí el constructor, el `__str__` y pensá en al menos una función que sea aplicable al componente elegido. Codificá el/los métodos pensados. ¿Qué acciones realizan los métodos elegidos sobre los atributos? ¿Una lectura (read)? ¿Una escritura (write)? ¿Una ejecución (exec)?

"""

class Computadora:
    conteoComputadora = 0
    posiblesSistOperativos = ['Windows 11', 'iOs 18']

    def __init__(self, marca:str, modelo:str, memoriaRAM:int, almacenamiento: int, procesador: str, esta_prendida = False, sistemaOperativo = 'Windows 11'):
        self.marca = self.validar_cadena(marca)
        self.modelo = self.validar_cadena(modelo)
        self.memoriaRAM = memoriaRAM
        self.almacenamiento = almacenamiento
        self.procesador = self.validar_cadena(procesador)
        self.esta_prendida = esta_prendida
        self.sistemaOperativo = self.validar_cadena(sistemaOperativo)

        def validar_cadena(self,cadena):
            if not isinstance(cadena, str):
                raise TypeError(f"{cadena} debe ser una cadena de texto")
            if len(cadena)<1:
                raise ValueError(f"{cadena} no puede ser una cadena vacía")
            return cadena
    
        Computadora.conteoComputadora += 1

    @classmethod
    def mostrar_conteo (cls):
        print(f'El número de computadoras es {cls.conteoComputadora}')

