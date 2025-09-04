# Este archivo corresponde al Ejercicio 1 de la guía práctica sobre Clases.
# Aquí deberás implementar la clase Camion y resolver los puntos a, b, c, d y f según las consignas

class Camion:
    camiones_registrados = []
    def __init__(self, patente:str, marca:str, carga:int, anio:int):
        self.patente = patente
        self.marca = marca
        self.carga = carga
        self.anio = anio

        Camion.camiones_registrados.append(self) #el camion adelante porq es un atributo de clase, el self para indicar que se quiere appendear ese mismo camion

    def __str__(self):
        return f"Camión: #{self.patente} \nCarga: {self.carga} \nMarca: {self.marca} \nAño: {self.anio}"
    
    # def __eq__(self, other):
    #     if not isinstance(other, Camion):
    #         return False
        
    #     return (self.patente == other.patente and self.marca == other.marca and self.carga == other.carga and self.anio == other.anio)
    
     
    def __eq__(self, other):
        if not isinstance(other, Camion):
            return False
        
        return (self.patente == other.patente )

    # def validarCamionesIguales (self, patente):
    #     if
    

"""a. Indicá qué devuelven las siguientes expresiones. Analizalo con tus compañeros y luego ejecutá las instrucciones en la máquina para comprobar tu respuesta. """
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

""" b. Modificá el código dado para que la comparación de dos objetos de la clase Camion devuelva True cuando todos sus atributos sean iguales. """

""" c. ¿Qué atributo hace único a nuestros objetos? Identificá el atributo que hace único al objeto Camion y modificá el código para que la comparación de dos objetos de la clase Camion devuelva True cuando ese atributo sea igual. """
# la patente hace único a nuestros objetos dentro de la clase Camion

""" d. Si dos personas tienen el mismo DNI, entonces... ¡Son la misma persona! ¿Cómo evitarías asignar el mismo DNI a dos personas distintas? Siguiendo esta analogía, adaptá el código anterior para el caso de los camiones. """

"""f. Creá un pequeño menú que te permita:

1. Registrar un nuevo camión.
1. Modificar la carga de un camión.
1. Mostrar por terminal la lista de camiones registrados, del más antiguo al más moderno.
1. Mostrar por terminal la marca que más veces fue registrada.""" 

def registrarCamion():
    patente = input("Ingrese la patente: ").strip().upper()
    if patente in Camion.camiones_registrados:
        raise ValueError(f'La patente {patente} ya está registrada')
    
    for camion in Camion.camiones_registrados:
        if camion.patente.upper() == patente:
            raise ValueError("La patente ya está registrada")
    
    marca = input("Ingrese la marca: ").strip()
    if not marca:
        raise ValueError("La marca no puede estar vacía")

    try:
        carga = int(input("Ingrese la carga del camión: "))
        anio = int(input("Ingrese el año: "))
    except ValueError:
        raise ("Carga y año deben ser números enteros")

    Camion(patente, marca, carga, anio)
    print("Camion registrado")
    
def buscarPorPatente(pat):
    for c in Camion.camiones_registrados:
        if c.patente.strip().upper() == pat:
            return c
    raise LookupError (f"No existe el camión con patente {pat}")

def modificarCarga():
    patente = input("Ingrese la patente del camión a modificar")
    camion = buscarPorPatente(patente)

    try:
        nuevaCarga = int(input("Ingrese la nueva carga: "))
    except ValueError as e:
        print("El error es:", e)
    except Exception as e:
        print("El error es:", e)

    camion.carga = nuevaCarga
    print("Carga actualizada.")

def mostrarCamiones():
    if not Camion.camiones_registrados:
        print("No hay camiones registrados")
    
    print("Camiones (antiguo a moderno)")

    for cam in sorted(Camion.camiones_registrados, key=lambda x: x.anio):
        print(cam)

def mostrarMarca():
    if not Camion.camiones_registrados:
        print("No hay camiones registrados")
    
    conteo = {}

    for c in Camion.camiones_registrados:
        marca = c.marca
        if marca in conteo:
            conteo[marca] += 1
        else:
            conteo[marca] = 1
    
    maxCantidad = 0
    maxMarca = None

    for marca in conteo:
        if conteo[marca]>maxCantidad:
            maxCantidad = conteo[marca]
            maxMarca = marca

    print(f"La marca más registrada es {maxMarca}, con un número de {maxCantidad} veces.")
    
def menu():
    op = 0
  
    while op != 5:
        print("Menú")
        print("1. Registrar un nuevo camión.")
        print("2. Modificar la carga de un camión.")
        print("3. Mostrar por terminal la lista de camiones registrados, del más antiguo al más moderno.")
        print("4. Mostrar por terminal la marca que más veces fue registrada.")
        print("5. Salir del menú.")
        try:
            op = int(input("Ingrese una opción: "))

            if op == 1:
                registrarCamion()
            elif op == 2:
                modificarCarga()
            elif op == 3:
                mostrarCamiones()
            elif op == 4:
                mostrarMarca()
            elif op == 5:
                print("Fin del programa")

        except ValueError:
            print("La opción no es válida, ingrese un número de nuevo")
        except Exception as e:
            print ("El error es: ", e)

if __name__ == "__main__":
    menu()