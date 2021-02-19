class NodoArbol:
  # Inicializamos el Nodo
  def __init__(self, val, derecha=None, izquierda=None, padreVal=None):
    self.val = val
    self.hijoDerecha = derecha
    self.hijoIzquierda = izquierda
    self.padreVal = padreVal
  
  # Representamos el nodo como expresion infija con sus hijos
  def __str__(self):
    izq = ""
    der = ""

    # Buscamos la representacion infija de su hijo izquierdo
    if(self.hijoIzquierda != None):
        izq = self.hijoIzquierda.__str__()
    # Buscamos la representacion infija de su hijo derecho
    if(self.hijoDerecha != None):
        der = self.hijoDerecha.__str__()
    # Si no tiene hijos, se devuelve el valor del nodo
    if(izq=="" and der==""):
        return self.val + " "
    # Aqui juntamos la representacion infija de los hijos con el valor el nodo
    # Cada if es un caso que se toma en cuenta para no agregar parentesis innecesarios
    else:
      if self.val == "*" or self.val == "/":
        return izq + self.val + " " + der
      elif (self.val == "+" and self.padreVal == "+") or (self.val == "-" and self.padreVal == "-"):
        return izq + self.val + " " + der
      elif (self.val == "+" or self.val == "-") and self.padreVal == None:
        return izq + self.val + " " + der
      return "( " + izq + self.val + " " + der  + ") "
  
  # Metodo que evalua la expresion
  def evaluar(self):
    if (self.val == "+"):
      return self.hijoIzquierda.evaluar() + self.hijoDerecha.evaluar()
    elif (self.val == "-"):
      return self.hijoIzquierda.evaluar() - self.hijoDerecha.evaluar()
    elif (self.val == "*"):
      return self.hijoIzquierda.evaluar() * self.hijoDerecha.evaluar()
    elif (self.val == "/"):
      return self.hijoIzquierda.evaluar() / self.hijoDerecha.evaluar()
    else:
      return int(self.val)


# Funcion que construye el arbol de la expresion
# Si swap == True, se calcula el arbol de la expresion postfija
# Si swap == False, se calcula el arbol de la expresion prefija
def expresionPrefijo(expresionStack, swap, padre=None):
  val = expresionStack.pop(0)
  # Si el valor es un operador, obtenemos el arbol de sus hijos para luego agregarlos al nodo
  if (val == "+") or (val == "-") or (val == "*") or (val == "/"):
    if swap:
      derecha = expresionPrefijo(expresionStack, swap, val)
      izquierda = expresionPrefijo(expresionStack, swap, val)
    else:
      izquierda = expresionPrefijo(expresionStack, swap, val)
      derecha = expresionPrefijo(expresionStack, swap, val)
    return NodoArbol(val, derecha, izquierda, padre)
  # Si el valor es un entero, se crea el nodo sin hijos
  else:
    return NodoArbol(val, None, None, padre)


def Menu():
  while(True):
    # Obtenemos el input
    print("\n\nPosibles acciones:\n\tEVAL <orden> <expr>\n\tMOSTRAR <orden> <expr>\n\tSALIR")
    accion = input("Ingrese una accion para proceder: ").split(" ", 2)
    # Si la accion es SALIR, abortamos la ejecucion del loop
    if accion[0] == "SALIR":
      break
    
    # Error checking
    if len(accion) < 3:
      print("\nLa acción que ingresó no existe, intente de nuevo.")
      continue

    # Define el arbol de la expresion dependiendo del orden dado
    if accion[1] == "PRE":
      arbol = expresionPrefijo(accion[2].split(" "), False)
    elif accion[1] == "POST":
      arbol = expresionPrefijo(accion[2].split(" ")[::-1], True)
    else:
      print("\nEl orden que ingresó no existe, intente de nuevo.")
      continue
    
    # Revisamos si la accion es valida y la ejecutamos
    if accion[0] == "EVAL":
      print("\n Resultado: " + str(arbol.evaluar()))
    elif accion[0] == "MOSTRAR":
      print("\n Resultado: " + str(arbol))
    else:
      print("\nLa acción que ingresó no existe, intente de nuevo.")


# Hacemos esto para poder aplicar al script las pruebas unitarias
if __name__ == "__main__":
  Menu()