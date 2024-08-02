num = int(input('enter table number'))       
c = 1      
# we will use a while loop for iterating 10 times for the multiplication table        
print("The Multiplication Table of: ", num)      
while c <= 10: # specifying the condition  
    print (num, 'x', c, '=', num *c)      
    c += 1 # expression to increment the counter