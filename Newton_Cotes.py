from function_value import get_function_value
from math import sqrt


def calculate_limit_of_function(function_number, epsilon):
    result, temp = 0, 0

    # function_limit to +1
    left_border, right_border = 0, 0.5

    temp = calculate_integral(function_number, left_border, right_border, epsilon)
    result += temp
    left_border = right_border
    right_border += (1 - right_border) * 1 / 2

    while abs(temp) > epsilon:
        temp = calculate_integral(function_number, left_border, right_border, epsilon)
        result += temp
        left_border = right_border
        right_border += (1 - right_border) * 1 / 2

    # function_limit to -1
    left_border, right_border = -0.5, 0

    temp = calculate_integral(function_number, left_border, right_border, epsilon)
    result += temp
    right_border = left_border
    left_border += (1 - abs(right_border)) * 1 / 2

    while abs(temp) > epsilon:
        temp = calculate_integral(function_number, left_border, right_border, epsilon)
        result += temp
        right_border = left_border
        left_border -= (1 - abs(right_border)) * 1 / 2

    return result


def calculate_integral(function_number, left_border, right_border, epsilon):
    delta = right_border - left_border
    subrange, result, temp = 1, 0, 0

    subrange *= 2
    length = delta / subrange
    temp = result
    result = 0
    result += calculate_function_and_weight_product(left_border, function_number) + \
              calculate_function_and_weight_product(right_border, function_number)

    i = 1
    while i < subrange / 2:
        result += 4 * calculate_function_and_weight_product(left_border + ((2 * i - 1) * length), function_number)
        result += 2 * calculate_function_and_weight_product(left_border + ((2 * i) * length), function_number)
        i += 1

    result *= length / 3

    while abs(temp - result) > epsilon:
        subrange *= 2
        length = delta / subrange
        temp = result
        result = 0
        result += calculate_function_and_weight_product(left_border, function_number) + \
                  calculate_function_and_weight_product(right_border, function_number)

        i = 1
        while i < subrange / 2:
            result += 4 * calculate_function_and_weight_product(left_border + ((2 * i - 1) * length), function_number)
            result += 2 * calculate_function_and_weight_product(left_border + ((2 * i) * length), function_number)
            i += 1

        result *= length / 3

    return result


def calculate_function_and_weight_product(argument, function_number):
    return get_function_value(argument, function_number) * (1 / sqrt(1 - argument * argument))
