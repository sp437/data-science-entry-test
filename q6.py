def find_first_negative(lst):          #define function
    """
    Task 1
    - Create a function that finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
    """
    i = 0                              #initialize i as zero
    while i < len(lst):                #while looping to check if i is less than length of lst list
        if lst[i] < 0:                 #if looping to check each item in lst is negative
            return lst[i]              # return item i of list if there is a item with negative value, only for 1st item is negative
        i = i + 1                      # update count i 
        
    return "No negatives"              # return result if there is no negative item


        
numbers =  [3, 5, -1, 7, -2, 8]   
find_first_negative(numbers)           #call function
print(find_first_negative(numbers))    #print result

# Task 2
# Invoke the function "find_first_negative" using the following scenario:
# - [3, 5, -1, 7, -2, 8]
# - [2, 10, 7, 0]
