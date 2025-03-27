def check_divisibility(num, divisor):         #define function
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    
    while num.isnumeric() != True or divisor.isnumeric() != True:            #while loop to check if num or divisor is not number
        print("Please enter numeric for both num divisor again: ")           #ask user to input num and divisor again
        break                                                                #exit while loop

    if float(num) % float(divisor) == 0:                                     #cast num and divisor as float data, condition if to check remainder of their division is zero
        return True                                                          #return True if no remainder
    else:
        return False                                                          #return False if no remainder


num = input("Enter num: ")                                                   # ask user to input num and divisor and assign to variables
divisor = input("Enter divisor")                                              

check_divisibility(num, divisor)                                              # call function

# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3
