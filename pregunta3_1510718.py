import sys
import math

class espacioMemoria:
  # Inicializamos el bloque de memoria con sus propiedades
  def __init__(self, numBloq, padre=None, nombre=None, ocupado=False):
    self.size = numBloq
    self.espacio_disponible = self.size
    self.padre = padre
    self.nombre = nombre
    self.ocupado = ocupado
    # Si el tamaño del bloque es mayor o igual que 2, podemos crearle bloques de memoria hijos
    if numBloq != 1:
      self.hijoIzquierda = espacioMemoria(numBloq//2, self)
      self.hijoDerecha = espacioMemoria(numBloq//2, self)
    else:
      self.hijoIzquierda = None
      self.hijoDerecha = None


  def __str__(self):
    string = "Espacio de memoria de " + str(self.size) + ". "
    if self.nombre:
      string += "Identificador del bloque: " + str(self.nombre)
    return string

  # Método que busca en la memoria el bloque perfecto para reservar la cantidad de memoria pedida
  def reservar(self, nombre, numBloq):
    if self.hijoIzquierda or self.hijoDerecha:
      # Si la cantidad de memoria pedida es menor o igual al espacio disponible del bloque actual y
      # mayor que el tamaño de sus bloques hijos, entonces reservamos este bloque y lo ocupamos
      if self.hijoIzquierda.size < numBloq <= self.espacio_disponible and not self.ocupado and self.espacio_disponible == self.size:
        self.nombre = nombre
        self.espacio_disponible = 0
        self.ocupado = True
        self.__actualizarMemoria(1)
        return True
      # Si la cantidad de memoria pedida es menor o igual al espacio disponible de alguno de los bloques hijos
      # del bloque actual, y este bloque hijo no está ocupado, entonces iteramos a este hijo para revisar si es 
      # del tamaño perfecto para reservarlo
      elif (numBloq <= self.hijoIzquierda.espacio_disponible) and not self.hijoIzquierda.ocupado:
        return self.hijoIzquierda.reservar(nombre, numBloq)
      elif (numBloq <= self.hijoDerecha.espacio_disponible) and not self.hijoDerecha.ocupado:
        return self.hijoDerecha.reservar(nombre, numBloq)
    # Si el bloque de memoria sin hijos (el de menor tamaño) es de tamaño perfecto, entonces reservamos este bloque
    # y lo ocupamos 
    else:
      self.nombre = nombre
      self.espacio_disponible = 0
      self.ocupado = True
      self.__actualizarMemoria(1)
      return True
    return False
  
  # Método que busca en la memoria el nombre identificador del bloque y lo liberamos
  def liberar(self, nombre):
    # Si encontramos el bloque, lo liberamos
    # Si no lo encontramos y el bloque tiene hijos, iteramos por sus hijos hasta encontrar el bloque
    if self.nombre == nombre:
      self.nombre = None
      self.espacio_disponible = self.size
      self.ocupado = False
      # Actualizamos la memoria debido a la acción liberar
      self.__actualizarMemoria(2)
      return True
    elif self.nombre != nombre and (self.hijoIzquierda or self.hijoDerecha):
      if self.hijoIzquierda.liberar(nombre) or self.hijoDerecha.liberar(nombre):
        return True
    # Si no encontramos el bloque
    return False
  
  def __actualizarMemoria(self, accion):
    self.__actualizarMemoriaArriba(accion)
    self.__actualizarMemoriaAbajo(accion)

  # Método con el que actualizamos el estatus de ocupado y el espacio disponible del bloque padre del bloque de memoria actual
  def __actualizarMemoriaArriba(self, accion):
    # acción == 1: acción reservar
    # acción == 2: acción liberar
    if self.padre:
      # Actualizamos el espacio disponible del padre con la suma de los espacios disponible de los hijos
      self.padre.espacio_disponible = self.padre.hijoIzquierda.espacio_disponible + self.padre.hijoDerecha.espacio_disponible
      # Si la acción fue reservar y el padre no tiene espacio disponible, cambiamos a ocupado el bloque de memoria padre
      # Si la acción fue liberar y el espacio disponible del padre es mayor que 0, cambiamos a desocupado el bloque de memoria padre
      if accion == 1:
        if self.padre.espacio_disponible == 0:
          self.padre.ocupado = True
      elif accion == 2:
        if self.padre.espacio_disponible > 0:
          self.padre.ocupado = False

      self.padre.__actualizarMemoriaArriba(accion)

  # Método con el que actualizamos el estatus de ocupado y el espacio disponible de los bloques hijos del bloque de memoria actual
  def __actualizarMemoriaAbajo(self, accion):
    # acción == 1: acción reservar
    # acción == 2: acción liberar
    if self.hijoIzquierda or self.hijoDerecha:
      # Si la acción fue reservar, ocupamos todos los bloques de memoria hijos del bloque que se reservó
      # Si la acción fue liberar, liberamos todos los bloques de memoria hijos del bloque que se liberó
      if accion == 1:
        self.hijoIzquierda.ocupado = True
        self.hijoIzquierda.espacio_disponible = 0
        self.hijoDerecha.ocupado = True
        self.hijoDerecha.espacio_disponible = 0
      elif accion == 2:
        self.hijoIzquierda.ocupado = False
        self.hijoIzquierda.espacio_disponible = self.hijoIzquierda.size
        self.hijoDerecha.ocupado = False
        self.hijoDerecha.espacio_disponible = self.hijoDerecha.size

      # Iteramos por los bloques hijos
      self.hijoIzquierda.__actualizarMemoriaAbajo(accion)
      self.hijoDerecha.__actualizarMemoriaAbajo(accion)

      



# Funcion para imprimir bloques de memoria con su información
def printMemoria(bloqMemoria, nivel=0):
  print(("\t"*nivel) + bloqMemoria.__str__())
  if (bloqMemoria.hijoIzquierda or bloqMemoria.hijoDerecha) and bloqMemoria.size != bloqMemoria.espacio_disponible and not bloqMemoria.nombre:
    print(("\t"*nivel) + "Compuesto por:")
    printMemoria(bloqMemoria.hijoIzquierda, nivel+1)
    printMemoria(bloqMemoria.hijoDerecha, nivel+1)

# Funcion que inicializa la memoria
def initMemoria(numBloques):
  def Log2(x):
    if x == 0:
      return False
  
    return (math.log10(x) /  math.log10(2)) 
  def isPowerOfTwo(n):
    return (math.ceil(Log2(n)) == math.floor(Log2(n)))

  if isPowerOfTwo(numBloques):
    return [espacioMemoria(numBloques, None)]
  else:
    memoria = []
    while(numBloques > 0):
      for i in range(numBloques):
        if 2**i <= numBloques < 2**(i+1):
          numBloques -= 2**i
          memoria.insert(0, espacioMemoria(2**i, None))
    return memoria
  

def Menu(numBloques):

  # Construimos la memoria vacia y la lista de nombres en memoria
  memoria = initMemoria(numBloques)
  nombres = []

  while(True):
    # Obtenemos el input
    print("\n\nPosibles acciones:\n\tRESERVAR <nombre> <cantidad>\n\tLIBERAR <nombre>\n\tMOSTRAR\n\tSALIR")
    accion = input("Ingrese una acción para proceder: ").split(" ")
    while '' in accion: accion.remove('')
    # Si no se ingresó ningun tipo de acción, devolvemos un error
    if not accion:
      print("\nNo se ingresó ninguna acción.")
      continue
    
    # Si la acción a realizar es reservar un espacio en memoria
    if accion[0] == "RESERVAR" and len(accion) == 3:
      # Errror checking
      if int(accion[2]) > numBloques:
        print("\nEl numero de bloques ingresado es mayor al tamaño total de la memoria.")
        continue
      if accion[1] in nombres:
        print("\n" + accion[1] + " ya tiene bloques de memoria reservada.")
        continue

      # Si la reserva de memoria fue exitosa, se agrega el nombre a la lista de nombres en memoria
      # Si no, se devuelve un error e ignora la acción
      reservado = False
      for i in range(len(memoria)):
        if memoria[i].espacio_disponible >= int(accion[2]):
          if memoria[i].reservar(accion[1], int(accion[2])):
            reservado = True
            nombres += [accion[1]]
            break
      if not reservado:
        print("\nNo existe espacio libre contiguo lo suficientemente grande para satifacer la acción.")

    # Si la acción a realizar es liberar un espacio en memoria
    elif accion[0] == "LIBERAR" and len(accion) == 2:

      # Si la liberacion de memoria fue exitosa, se elimina el nombre de la lista de nombres en memoria
      # Si no, se devuelve un error e ignora la acción
      liberado = False
      for i in range(len(memoria)):
        if memoria[i].liberar(accion[1]):
          liberado = True
          nombres.remove(accion[1])
          break
      if not liberado:
        print("\n" + accion[1] + " no tiene memoria reservada.")

    # Si la acción es mostrar la memoria
    elif accion[0] == "MOSTRAR" and len(accion) == 1:
      print()
      for i in range(len(memoria)):
        printMemoria(memoria[i])

    # Si la acción es salir del programa
    elif accion[0] == "SALIR" and len(accion) == 1:
      break

    # Si se ingreso una acción invalida
    else:
      print("\nLa acción que ingresó no existe, intente de nuevo.")


# Hacemos esto para poder aplicar al script las pruebas unitarias
if __name__ == "__main__":
  try:
    Menu(int(sys.argv[1]))
  except:
    print("El argumento ingresado no es un entero.")