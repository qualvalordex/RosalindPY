#Program that recieve a binary number as a string and convert it and returns it as a string

def isBinary(number):
    bin_characters = ['0','1']
    for charactere in str(number):
        if charactere not in bin_characters:
            return False
    return True

def binToDec(binary_number):
    if isBinary(binary_number) == True:
        binary_number = str(binary_number)
        position_control = len(binary_number) - 1
        decimal_number = 0
        for number in binary_number:
            number = int(number)
            decimal_number += number * (2 ** position_control)
            position_control -= 1
        return decimal_number
    return 'Not a binary number inserted.'

# LOGS: 12
# print(binToDec(1100))

# LOGS: Not a binary number inserted.
# print(binToDec(1234))