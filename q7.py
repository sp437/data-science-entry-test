class Car:                            #define class object
    """
    Task 1
    - Define a class named Car with attributes: make, model, year
    - Initialize these attributes in the __init__ method
    - Add a method named describe_car() that prints information about the car as "Year Make Model"
    """
    def __init__(self, make, model, year):          #define attributes of Car object
        self.make = make                            
        self.model = model
        self.year = year
        
    def describe_car(self):                         
        print(f"{self.make}, {self.model}, {self.year}")      #print result of each placeholders
        
car1 = Car("Make: Toyota", "Model: Corolla", "Year: 2020")     #to create instance of Car object
car1.describe_car()                                            #call function 

# Task 2
# Create an instance of the Car class with the following attributes and call describe_car method:
# - Make: Toyota, Model: Corolla, Year: 2020
