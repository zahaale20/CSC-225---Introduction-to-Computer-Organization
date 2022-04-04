# Implements operations on hexadecimal numbers.
# CSC 225, Assignment 1
# Given code, Winter '20
import math


def binary_to_hex(number):
    """
    Convert a 16-bit binary number to hexadecimal.
    TODO: Implement this function. Do *not* convert the number to decimal.

    :param number: A bitstring representing the number to convert
    :return: A hexadecimal string, the converted number
    """
    hexicon = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    temp = []
    output = ""
    for b in range(len(number)):
        temp.append(number[b])
        if (b+1) % 4 == 0:
            dec = 0
            for b2 in range(len(temp)):
                if temp[len(temp) - b2 - 1] == "1":
                    dec += pow(2, b2)
            output += hexicon[dec]
            temp = []
    output = "0x" + output
    return output



def hex_to_binary(number):
    """
    Convert a hexadecimal number to 16-bit binary.
    TODO: Implement this function. Do *not* convert the number to decimal.

    :param number: A hexadecimal string, the number to convert
    :return: A bitstring representing the converted number
    """
    hexicon = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    number = number[2:]
    output = ""
    for n in number:
        dec = hexicon.index(n)
        for i in range(3, -1, -1):
            if dec // pow(2, i) >= 1:
                dec -= pow(2, i)
                output += "1"
            else:
                output += "0"
    return output



