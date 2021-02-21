#test_tutorial.py
from pregunta3_1510718 import *
from unittest import TestCase
from io import StringIO
from unittest.mock import patch
import os
import subprocess

# Para correr pruebas de cobertura: pip install coverage

class pregunta6Test(TestCase):

    # Probamos: 
    #   Acción inexistente por escribir mal RESERVAR
    #   Acción inexistente por ingresar argumentos de mas
    #   Acción inexistente por escribir cualquier texto
    #   No se ingresa ninguna acción
    #   Tratamos de reservar mas bloques que los bloques totales de la memoria
    #   Tratamos de reservar un bloque sin espacio suficiente en la memoria
    #   Liberamos un bloque con identificador inexistente
    #   Tratamos de reservar un bloque de memoria con identificador repetido
    def test_input_errors(self):
        self.maxDiff = None

        input_ = "RESERVA a 1\nMOSTRAR 2\nTestAccionError\n \nRESERVAR a 4\nRESERVAR a 3\nRESERVAR b 1\nLIBERAR c\nRESERVAR a 1\nSALIR\n"

        menu_string = "\n\nPosibles acciones:\n\tRESERVAR <nombre> <cantidad>\n\tLIBERAR <nombre>\n\tMOSTRAR\n\tSALIR\nIngrese una acción para proceder: "

        with patch('sys.stdin', StringIO(input_)) as mocked_stdin:
            with patch('sys.stdout', new=StringIO()) as mocked_stdout:

                Menu(3)

                output = mocked_stdout.getvalue()
                expected_output = menu_string + "\nLa acción que ingresó no existe, intente de nuevo.\n" + menu_string + "\nLa acción que ingresó no existe, intente de nuevo.\n" \
                + menu_string + "\nLa acción que ingresó no existe, intente de nuevo.\n" + menu_string +"\nNo se ingresó ninguna acción.\n" + menu_string + \
                "\nEl numero de bloques ingresado es mayor al tamaño total de la memoria.\n" + menu_string + menu_string + \
                "\nNo existe espacio libre contiguo lo suficientemente grande para satifacer la acción.\n" + menu_string + "\nc no tiene memoria reservada.\n" + menu_string + \
                "\na ya tiene bloques de memoria reservada.\n" + menu_string

                self.assertEqual(output, expected_output)
    

    # Programa que simula reserva y liberacion en una memoria de tamaño 4KB.
    def test_memoria_size_2(self):
        self.maxDiff = None

        input_ = "RESERVAR a 1\nMOSTRAR\nRESERVAR b 1\nMOSTRAR\nLIBERAR b\nMOSTRAR\nLIBERAR a\nMOSTRAR\nRESERVAR a 2\nMOSTRAR\nSALIR\n"

        menu_string = "\n\nPosibles acciones:\n\tRESERVAR <nombre> <cantidad>\n\tLIBERAR <nombre>\n\tMOSTRAR\n\tSALIR\nIngrese una acción para proceder: "

        with patch('sys.stdin', StringIO(input_)) as mocked_stdin:
            with patch('sys.stdout', new=StringIO()) as mocked_stdout:

                Menu(2)

                output = mocked_stdout.getvalue()
                expected_output = menu_string + menu_string + "\nEspacio de memoria de 4KB. Espacio libre de memoria: 2KB. \n\tEspacio de memoria de 2KB. " \
                "Espacio libre de memoria: 0KB. Identificador del bloque: a\n\tEspacio de memoria de 2KB. Espacio libre de memoria: 2KB. \n" + menu_string + menu_string + \
                "\nEspacio de memoria de 4KB. Espacio libre de memoria: 0KB. \n\tEspacio de memoria de 2KB. Espacio libre de memoria: 0KB. Identificador del bloque: a" \
                "\n\tEspacio de memoria de 2KB. Espacio libre de memoria: 0KB. Identificador del bloque: b\n" + menu_string + menu_string + "\nEspacio de memoria de 4KB. Espacio libre de memoria: 2KB. " \
                "\n\tEspacio de memoria de 2KB. Espacio libre de memoria: 0KB. Identificador del bloque: a\n\tEspacio de memoria de 2KB. Espacio libre de memoria: 2KB. \n" \
                + menu_string + menu_string + "\nEspacio de memoria de 4KB. Espacio libre de memoria: 4KB. \n\tEspacio de memoria de 2KB. Espacio libre de memoria: 2KB. " \
                "\n\tEspacio de memoria de 2KB. Espacio libre de memoria: 2KB. \n" + menu_string + menu_string + "\nEspacio de memoria de 4KB. Espacio libre de memoria: 0KB. " \
                "Identificador del bloque: a\n\tEspacio de memoria de 2KB. Espacio libre de memoria: 0KB. \n\tEspacio de memoria de 2KB. Espacio libre de memoria: 0KB. \n" + menu_string

                self.assertEqual(output, expected_output)