def swap(x, y):
    # """
    # Task 1
    # - Create a function that would swap the value of x and y using only x and y as variables.
    # - x and y must be numeric.
    # - Return -1 if x and y is not numeric, and
    # - print the swapped values if both x and y are numeric.
    # """   
    if x.isnumeric() and y.isnumeric:     #if loop to check if both x and y values are numbers
        z = x                             #Assign x value to z variable 
        x = y                             #Assign y value to x variable
        y = z                             #Assign z value to y variable
        print("x is " + x)                #print comment concatenate to x value
        print("y is " + y)                #print comment concatenate to y value
    else: 
        return -1                         #if loop both x and y values are not numbers, return -1 as output of function
        
    return                                #return x and y values

x = input("Please enter x value: ")       #user to input the x value
y = input("Please enter y value: ")       #user to input the y value
swap(x, y)                                #Call swap function

# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17
