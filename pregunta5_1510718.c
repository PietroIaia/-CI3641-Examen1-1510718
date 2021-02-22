#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <time.h>

// X = 7, Y = 1, Z = 8
// α = ((7 + 1) mod 5) + 3
// α == 6
// β = ((1 + 8) mod 5) + 3
// β == 7

// 5.a
int F67(int n) {
  if (n < 42) {
    return n;
  }

  return F67(n - 7) + F67(n - 14) + F67(n - 21) + F67(n - 28) + F67(n - 35) + F67(n - 42);
}

// 5.b
// Funcion auxiliar que calcula la recursion en cola. 
// Esta inspirada en la version recursiva de cola de los numeros de Fibonacci
// Iremos decrementando el numero ingresado de 7 en 7 hasta llegar a 42, luego de eso regresaremos los valores acumulados de la recursion.
// Parametros:
//    int n: El numero ingresado por el usuario que se desea encontrar su valor.
//    int a: El valor acumulado de las recursiones pasadas.
//    int b: El valor de la recursion anterior a la actual.
//    int c: El valor de hace 2 recursiones atras.
//    int d: El valor de hace 3 recursiones atras.
//    int e: El valor de hace 4 recursiones atras.
//    int f: El valor de hace 5 recursiones atras.
int F67_calc_cola(int n, int a, int b, int c, int d, int e, int f) {
  if (n == 42) {
    return (a + b + c + d + e + f);
  }
  return F67_calc_cola(n - 7, (a + b + c + d + e + f), a, b, c, d, e);
}

int F67_cola(int n) {
  // Si el numero ingresado es menor que 42, no es necesario la recursion de cola
  if (n < 42) {
    return n;
  } else {
    int mod7 = (n % 7);
    return F67_calc_cola(n - mod7, 35 + mod7, 28 + mod7, 21 + mod7, 14 + mod7, 7 + mod7, mod7);
  };
}


// 5.c
// La explicacion de esta funcion es identica a la de la funcion anterior, solo que iteramos en vez de utilizar recursion.
int F67_iterativa(int n) {
  if (n < 42) {
    return n;
  } 

  int mod7 = (n % 7);
  n -= mod7; 
  int a = 35 + mod7;
  int b = 28 + mod7;
  int c = 21 + mod7;
  int d = 14 + mod7;
  int e = 7 + mod7;
  int f = mod7;
  int aux_a;
  while (n != 42) {
    aux_a = a;
    a = (a + b + c + d + e + f);
    f = e; e = d; d = c; c = b; b = aux_a;
    n -= 7;
  }
  return (a + b + c + d + e + f);
}

int main (void){
  clock_t begin;
  clock_t end; 
  int inputs[5] = {39, 60, 150, 250, 300};
  int F67_val;
  int F67_cola_val;
  int F67_iterativa_val;
  double time_spent_recursion;
  double time_spent_cola;
  double time_spent_iterativo;

  for (int i=0; i<5; i++)
  {
    printf("Ejecución con n = %i\n", inputs[i]);
    begin = clock();
    F67_val = F67(inputs[i]);
    end = clock();
    time_spent_recursion = (double)(end - begin) / CLOCKS_PER_SEC;
    printf("Recursión: %i, Tiempo de ejecución: %f\n", F67_val, time_spent_recursion);

    begin = clock();
    F67_cola_val = F67_cola(inputs[i]);
    end = clock();
    time_spent_cola = (double)(end - begin) / CLOCKS_PER_SEC;
    printf("Cola: %i, Tiempo de ejecución: %f\n", F67_cola_val, time_spent_cola);

    begin = clock();
    F67_iterativa_val = F67_iterativa(inputs[i]);
    end = clock();
    time_spent_iterativo = (double)(end - begin) / CLOCKS_PER_SEC;
    printf("Iterativa: %i, Tiempo de ejecución: %f\n\n", F67_iterativa_val, time_spent_iterativo);
  }
}