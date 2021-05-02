from sys import exit as exitProgram
from function_value import get_function_value
from horner import get_polynomial_value
from Newton_Cotes import calculate_limit_of_function
from Gauss import calculate_integral
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

    epsilon = float(input("""
Podaj dokladnosc: """))
    while epsilon < 0:
        print("Podaj dokladnosc wieksza od 0!")
        epsilon = float(input("""
Podaj dokladnosc: """))

    calculations(function_number, epsilon)


def calculations(function_number, epsilon):
    print()
    print()
    print("Wartosc dla metody Newtona-Cotesa:", calculate_limit_of_function(function_number, epsilon))
    print()

    for i in range(2, 6):
        print("Liczba wezlow:", i)
        print("Wartosc dla metody Gaussa-Czebyszewa:", calculate_integral(function_number, i))
        print()


##########################################################################
# START
##########################################################################
menu()
