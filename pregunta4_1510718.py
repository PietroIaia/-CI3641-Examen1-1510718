
# 4.a Iterador zipWith
def zipWith(a, b, funcion):
  if a and b:
    # Devuelve el resultado de aplicar la funcion a los elementos
    yield funcion(a[0], b[0])

    for p in zipWith(a[1:], b[1:], funcion):
      yield p


# 4.b Iterador suspenso
def suspenso(p):
  # Toma cada elemento de la lista p, y lo devuelve uno por uno
  for eachP in p:
    yield eachP

  acum = []
  for p in zipWith([0, *p], [*p, 0], lambda x, y: x + y):
    acum += [p]
  for m in suspenso(acum):
    yield m