def string_reverse(s):                 #define function with argument s
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    a = ""                             #initialize a as empty string   
    for i in s:                        #for looping each item in s
        a = i + a                      #concatenate i and old a value so that it turn out as reverse order, and assign to a
    
    return a                           # return string s to output of function
s = input("Enter string: ")            #user to input to string s
# s = "Hello World"[::-1]

string_reverse(s)                      #call function with argument s
print(s)                               #print result

# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"
