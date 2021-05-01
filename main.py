from sys import exit as exitProgram
from function_value import get_function_value
from horner import get_polynomial_value
from Newton_Cotes import *
import numpy as np
import sympy as sp


def menu():
    while True:
        print("""

-------------------------------------------------------------------------        
Metody calkowania numerycznego
Lukasz Janiszewski, Maciej Kubis""")
        print("""
Wybierz opcję:
1. Rozpocznij program
2. Zakończ program""")
        user_choice = int(input("""
Wybór: """))
        if user_choice == 1:
            data_load()
        elif user_choice == 2:
            exitProgram()
        else:
            print("""Wybrano nieprawidlowa opcje!""")


def data_load():
    print("""
Wybierz numer funkcji ktorej chcesz uzyc w programie:
    1. FUNKCJA LINIOWA: x - 3
    2. FUNKCJA WIELOMIANOWA:  2 * x^3 + 1 * x^2 - 3 * x + 7
    3. FUNKCJA TRYGONOMETRYCZNA:  4 * cos(x) + 6 * sin(x)
    4. FUNKCJA ZŁOŻONA:  |sin(x + 2) - 1.6|""")
    function_number = int(input("""
Wybór: """))
    while function_number not in [1, 2, 3, 4]:
        valid_number = False
        while not valid_number:
            function_number = int(input("""
                Wybierz jeszcze raz numer funkcji: """))
            if function_number in [1, 2, 3, 4]:
                valid_number = True

    epsilon = int(input("""
Podaj dokladnosc: """))
    while epsilon < 0:
        print("Podaj dokladnosc wieksza od 0!")
        epsilon = int(input("""
Podaj dokladnosc: """))

    calculations(function_number, epsilon)


def calculations(function_number, epsilon):
    pass


##########################################################################
# START
##########################################################################
menu()
