# Implements operations on binary numbers.
# CSC 225, Assignment 1
# Given code, Spring '22


def add(addend_a, addend_b):
    """
    Add two 16-bit, two's complement numbers; ignore carries/overflows.
    TODO: Implement this function. Do *not* convert the numbers to decimal.

    :param addend_a: A bitstring representing the first number
    :param addend_b: A bitstring representing the second number
    :return: A bitstring representing the sum
    """
    output = ""
    carry = "0"
    for c in range(len(addend_a)):
        if addend_a[len(addend_a) - c - 1] == "0" and addend_b[len(addend_b) - c - 1] == "0":
            if carry == "1":
                output = "1" + output
                carry = "0"
            elif carry == "0":
                output = "0" + output
                carry = "0"

        elif (addend_a[len(addend_a) - c - 1] == "1" and addend_b[len(addend_b) - c - 1] == "0") or \
                (addend_a[len(addend_a) - c - 1] == "0" and addend_b[len(addend_b) - c - 1] == "1"):
            if carry == "1":
                output = "0" + output
                carry = "1"
            elif carry == "0":
                output = "1" + output
                carry = "0"
        elif addend_a[len(addend_a) - c - 1] == "1" and addend_b[len(addend_b) - c - 1] == "1":
            if carry == "1":
                output = "1" + output
                carry = "1"
            elif carry == "0":
                output = "0" + output
                carry = "1"
    return output


def negate(number):
    """
    Negate a 16-bit, two's complement number.
    TODO: Implement this function. Do *not* convert the number to decimal.

    :param number: A bitstring representing the number to negate
    :return: A bistring representing the negated number
    """
    output = ""
    for c in range(len(number)):
        if number[len(number) - 1 - c] == "0":
            output = "1" + output
        else:
            output = "0" + output
    output = add(output, "0000000000000001")
    return output


def subtract(minuend, subtrahend):
    """
    Subtract one 16-bit, two's complement number from another.
    TODO: Implement this function. Do *not* convert the numbers to decimal.

    :param minuend: A bitstring representing the number from which to subtract
    :param subtrahend: A bitstring representing the number to subtract
    :return: A bitstring representing the difference
    """
    return add(minuend, negate(subtrahend))


def multiply(multiplicand_a, multiplicand_b):
    """
    Multiply two 16-bit, two's complement numbers; ignore carries/overflows.
    TODO: Implement this function. Do *not* convert the numbers to decimal.

    :param multiplicand_a: A bitstring representing the first number
    :param multiplicand_b: A bitstring representing the second number
    :return: A bitstring representing the product
    """
    output = "0000000000000000"
    partial_products = []
    for b in range(len(multiplicand_b) -1, -1, -1):
        if multiplicand_b[b] == "1":
            partial_products.append(multiplicand_a + "0" * (len(multiplicand_b) - b - 1))
    for p in partial_products:
        output = add(output, p)
    return output


def binary_to_decimal(number):
    """
    Convert a 16-bit, two's complement number to decimal.
    TODO: Implement this function.

    :param number: A bitstring representing the number to convert
    :return: An integer, the converted number
    """
    output = 0
    for c in range(len(number) - 1, -1, -1):
        if number[c] == "1":
            output += pow(2, len(number) - 1 - c)
    return output


def decimal_to_binary(number):
    """
    Convert a decimal number to 16-bit, two's complement binary.
    TODO: Implement this function.

    :param number: An integer, the number to convert
    :return: A bitstring representing the converted number
    :raise OverflowError: If the number cannot be represented with 8 bits
    """
    output = ""
    while number >= 1:
        if number % 2 == 0:
            output = "0" + output
        elif number == 1 or number % 2 == 1:
            output = "1" + output
        number = number // 2
    for i in range(16):
        if i > len(output) - 1:
            output = "0" + output
    return output


