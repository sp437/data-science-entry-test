def update_dictionary(dct, key, value):           #define function with arguments to be passed
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """

    dct.update({key:value})                      #Update dictionary dct with key and value
    
    return                                        #return new output of dct, key, value


dct = {}                                          #initialize new blank dictionary

key = input("Enter Key: ")                         #ask user to enter key and value 
value = input("Enter Value: ")

update_dictionary(dct, key, value)                 #call fuction with arguments 
print(dct)                                         #print dictionary dct

# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# - {"age": 25}, "age", 26
