import numpy as np
from function_value import get_function_value


def calculate_integral(function_number, nodes_number):
    result = 0
    currentWeight = ...
    currentNode = ...
    pi = 3.14159265359
    for i in range(nodes_number):
        currentWeight = pi / nodes_number
        currentNode = -np.cos(((2 * i - 1) * pi) / (2 * nodes_number))
        result += currentWeight * get_function_value(currentNode, function_number)
    return result
