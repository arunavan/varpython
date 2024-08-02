# Python program to show how to create a tuple    
# Creating an empty tuple    
empty_tuple = ()    
print("Empty tuple: ", empty_tuple)    
    
# Creating tuple having integers    
tuple = (4, 6, 8, 10, 12,10,8,6,12,12,12, 14)   

print(tuple.count(12))

print("Tuple with integers: ", tuple)    
    
# Creating a tuple having objects of different data types    
mixed_tuple = (4, "Python", 9.3)    
print("Tuple with different data types: ", mixed_tuple)    
    
# Creating a nested tuple    
nested_tuple = ("Python", {4: 5, 6: 2, 8:2}, (5, 3, 5, 6))    
print("A nested tuple: ", nested_tuple) 