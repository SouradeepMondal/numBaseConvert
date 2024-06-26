#!/usr/bin/env python3

# Function to return ASCII value of a character
def returnASCIIVal(c):
    if (c >= '0' and c <= '9'):
        return ord(c) - 48
    else:
        return ord(c) - 65  + 10
 
# Function to convert a number from given base to decimal number
def toDeci(strr, base):
     
    # Stores the length of the string
    lenn = len(strr)
     
    # Initialize power of base
    power = 1
     
    # Initialize result
    num = 0
     
    # Decimal equivalent is strr[len-1]*1 + strr[len-2]*base + strr[len-3]*(base^2) + ...
    for i in range(lenn - 1, -1, -1):
        # A digit in input number must be less than number's base
        if (returnASCIIVal(strr[i]) >= base):
            print("Invalid Number")
            return -1
             
        # Update num
        num += returnASCIIVal(strr[i]) * power
         
        # Update power
        power = power * base
     
    return num
 
# Function to return equivalent character of a given value
def reVal(num):
     
    if (num >= 0 and num <= 9):
        return chr(num + 48)
    else:
        return chr(num - 10 + 65)
 
 
# Function to convert a given decimal number to a given base
def fromDeci(base, inputNum):
     
    # Store the result
    res = ""
     
    # Repeatedly divide inputNum by base and take remainder
    while (inputNum > 0):
         
        # Update res
        res += reVal(inputNum % base)
         
        # Update inputNum
        inputNum //= base
         
    # Reverse the result
    res = res[::-1]
     
    return res
 
 
# Function to convert a given number from a base to another base
def convertBase(s, a, b):
     
    # Convert the number from base A to decimal
    num = toDeci(s, a)
 
    # Convert the number from decimal to base B
    ans = fromDeci(b, num)
 
    # Return the result
    return ans
 
 
# Driver Code
def main():
    # Given input
    s = input("input number as string: ")
    a = int(input("input base of input value: "))
    b = int(input("input base of output value: "))
 
    # Function Call
    print(convertBase(s, a, b))

if __name__ == "__main__":
    main()