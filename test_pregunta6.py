#test_tutorial.py
from pregunta6_1510718 import *
from unittest import TestCase
from io import StringIO
from unittest.mock import patch
import os
import subprocess

# Para correr pruebas de cobertura: pip install coverage

# Arboles para las pruebas
arbol1 = expresionPrefijo("+ 5 + 2 - 2 * 3 / 4 2".split(" "), False)
arbol2 = expresionPrefijo("* + 2 1 - 6 1".split(" "), False)
arbol3 = expresionPrefijo("2 3 4 + + 5 *".split(" ")[::-1], True)

class pregunta6Test(TestCase):


    def test_evaluar_expresion_prefija(self):

        output = arbol1.evaluar()
        expected_output = 3

        self.assertEqual(output, expected_output)
    

    def test_evaluar_expresion_postfija(self):

        output = arbol3.evaluar()
        expected_output = 45

        self.assertEqual(output, expected_output)


    def test_print_expresion_prefija(self):
        output = arbol1.__str__()
        expected_output = "5 + 2 + ( 2 - 3 * 4 / 2 ) "

        self.assertEqual(output, expected_output)
    

    def test_print_expresion_postfija(self):
        output = arbol3.__str__()
        expected_output = "( 2 + 3 + 4 ) * 5 "

        self.assertEqual(output, expected_output)
    

    def test_menu(self):

        input_ = "EVAL PRE + * + 3 4 5 7\nMOSTRAR POST 8 3 - 8 4 4 + * +\nTestFailure\nMOSTRAR idk 8 3 -\nSALIR\n"
        
        with patch('sys.stdin', StringIO(input_)) as mocked_stdin:
            with patch('sys.stdout', new=StringIO()) as mocked_stdout:

                Menu()

                output = mocked_stdout.getvalue()
                expected_output = "\n\nPosibles acciones:\n\tEVAL <orden> <expr>\n\tMOSTRAR <orden> <expr>\n\tSALIR\nIngrese una accion para proceder: \n" \
                    " Resultado: 42\n\n\nPosibles acciones:\n\tEVAL <orden> <expr>\n\tMOSTRAR <orden> <expr>\n\tSALIR\nIngrese una accion para proceder: \n" \
                    " Resultado: ( 8 - 3 ) + 8 * ( 4 + 4 ) \n\n\nPosibles acciones:\n\tEVAL <orden> <expr>\n\tMOSTRAR <orden> <expr>\n\tSALIR\nIngrese una accion para proceder: \n" \
                    "La acción que ingresó no existe, intente de nuevo.\n\n\nPosibles acciones:\n\tEVAL <orden> <expr>\n\tMOSTRAR <orden> <expr>\n\tSALIR\nIngrese una accion para proceder: \n" \
                    "El orden que ingresó no existe, intente de nuevo.\n\n\nPosibles acciones:\n\tEVAL <orden> <expr>\n\tMOSTRAR <orden> <expr>\n\tSALIR\nIngrese una accion para proceder: "

                self.assertEqual(output, expected_output)