# Este archivo corresponde al Ejercicio 1 de la guía práctica sobre Clases.
# Aquí deberás implementar la clase Camion y resolver los puntos a, b, c, d y f según las consignas

class Camion:
    def __init__(self, patente:str, marca:str, carga:int, anio:int):
        self.patente = patente
        self.marca = marca
        self.carga = carga
        self.anio = anio

    def __str__(self):
        return f"Camión: #{self.patente} \nCarga: {self.carga} \nMarca: {self.marca} \nAño: {self.anio}"
    
    def __eq__(self, other):
        if not isinstance(other, Camion):
            return False
        
        return (self.patente == other.patente and self.marca == other.marca and self.carga == other.carga and self.anio == other.anio)
    
    # def validarCamionesIguales (self, patente):
    #     if
    

"""a. Indicá qué devuelven las siguientes expresiones. Analizalo con tus compañeros y luego ejecutá las instrucciones en la máquina para comprobar tu respuesta.
"""
furgon1 = Camion("ABC123", "Mercedes", 1000, 2020)
furgon2 = furgon1
furgon3 = Camion("DEF456", "Volvo", 2000, 2021)
furgon4 = Camion("ABC123", "Mercedes", 1000, 2020)

print(furgon1 == furgon2)
print(furgon1 is furgon2)
print(furgon3 == furgon4)
print(furgon3 is furgon4)
print(furgon1 == furgon4)  

# RTA A: primero, no puede devolver nada debido a que los atributos dentro de la clase no están definidos, por lo que en caso de querer visualizarlos y compararlos, me va a tirar error porque no puedo poner ese objeto con esa plantilla que no coincide.
# Después de probarlo me dio el siguiente error: TypeError: Camion.__init__() takes 3 positional arguments but 5 were given

"""
b. Modificá el código dado para que la comparación de dos objetos de la clase Camion devuelva True cuando todos sus atributos sean iguales.
"""

"""
c. ¿Qué atributo hace único a nuestros objetos? Identificá el atributo que hace único al objeto Camion y modificá el código para que la comparación de dos objetos de la clase Camion devuelva True cuando ese atributo sea igual.
"""
# la patente hace único a nuestros objetos dentro de la clase Camion

"""
d. Si dos personas tienen el mismo DNI, entonces... ¡Son la misma persona! ¿Cómo evitarías asignar el mismo DNI a dos personas distintas? Siguiendo esta analogía, adaptá el código anterior para el caso de los camiones.

f. Creá un pequeño menú que te permita:

1. Registrar un nuevo camión.
1. Modificar la carga de un camión.
1. Mostrar por terminal la lista de camiones registrados, del más antiguo al más moderno.
1. Mostrar por terminal la marca que más veces fue registrada.""" 