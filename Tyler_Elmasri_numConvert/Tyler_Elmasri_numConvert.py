
def toDecimal(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal * 2 + int(digit)
    return decimal

def toOctal(binary):
    decimal = toDecimal(binary)
    octal = ""
    while decimal > 0:
        octal = str(decimal % 8) + octal
        decimal //= 8
    return octal

def toHexadecimal(binary):
    decimal = toDecimal(binary)
    hexadecimal = ""
    while decimal > 0:
        remainder = decimal % 16
        if remainder < 10:
            hexadecimal = str(remainder) + hexadecimal
        else:
            hexadecimal = chr(ord('A') + remainder - 10) + hexadecimal
        decimal //= 16
    return hexadecimal

def negativeSM(binary):
    if binary[0] == '0':
        return '1' + binary[1:]
    else:
        return '0' + binary[1:]

def negativeOnes(binary):
    negative = ""
    for digit in binary:
        if digit == '0':
            negative += '1'
        else:
            negative += '0'
    return negative

def negativeTwos(binary):
    carry = 1
    negative = ""
    for digit in binary[::-1]:
        if digit == '0':
            negative = str(1 - carry) + negative
            carry = 0
        else:
            negative = str(carry) + negative
    return negative

def userInput():
    binary = input("Enter a binary number between 4 and 12 bits: ")
    while not (binary.isdigit() and 4 <= len(binary) <= 12 and all(bit in '01' for bit in binary)):
        print("Enter only binary digits (0 or 1) within the specified range.")
        binary = input("Enter a binary number between 4 and 12 bits: ")
    if len(binary) < 12:
        binary = '0' * (12 - len(binary)) + binary
    return binary

def main():
    binary = userInput()
    print("The bits entered:", binary)
    
    decimal = toDecimal(binary)
    octal = toOctal(binary)
    hexadecimal = toHexadecimal(binary)
    
    print("The Decimal equivalent:", decimal)
    print("The Octal equivalent:", octal)
    print("The Hexadecimal equivalent:", hexadecimal)
    
    print("The negative no (-{}) using Signed Magnitude: {}".format(decimal, sm_negative))
    print("The negative no (-{}) using 1's Complement: {}".format(decimal, ones_negative))
    print("The negative no (-{}) using 2's Complement: {}".format(decimal, twos_negative))

if __name__ == "__main__":
    main()