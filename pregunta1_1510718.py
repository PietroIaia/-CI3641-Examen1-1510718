# Factorial
def fact(n):
  if type(n) == int:
    if n == 0:
      return 1
    elif n > 0:
      return n * fact(n-1)

# Producto de matrices AxB
def prodMatrices(A, B):
  C = [[0 for x in range(len(B[0]))] for y in range(len(A))] 
  # Iteramos por las filas de A
  for i in range(len(A)):
    # Iteramos por las columnas de B
    for j in range(len(B[0])):
      # Iteramos por las filas de B
      for k in range(len(B)):
        C[i][j] += A[i][k] * B[k][j]
  return C