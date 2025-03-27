# def find_and_replace(lst, find_val, replace_val):
    # """
    # Task 1
    # - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    # - lst must be a list.
    # - Return the modified list.
    # """


def find_and_replace(lst, find_val, replace_val):   #define function with arguments passed
    if find_val.isnumeric() == True:                #if loop to check if find_val is a number 
        for i in range(len(lst)):                   #if find_val is number, for looping on each index in range object of length of 1st list
            if lst[i] == int(find_val):             #cast find_value as integer and check equality of item in list of index i
                lst[i] = int(replace_val)           #cast replace_val as integer and assign to item in list of index i
    else:
        for i in range(len(lst)):                   #if find_val is not number, for looping on each item in list (up to length size)
            if lst[i] == find_val:                  #check find_val is equal to item in list of index i
                lst[i] = replace_val                #if equal to item in list, replace with new value 
    return

# lst = [1, 2, 3, 4, 2, 2]   
# lst = ["apple", "banana", "apple"]

find_val = input("Please enter find value: ")      #Ask user to input value
replace_val = input("Please enter new value: ")    #Ask user to new value


find_and_replace(lst, find_val, replace_val)        #Call function with the arguments to pass
print(lst)                                          #print list with value updated


# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5
# - ["apple", "banana", "apple"], "apple", "orange"
