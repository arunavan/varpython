l1 = [3, 4, 8, 10, 34, 45, 67,80]        # Initialize the list  

for x in l1:
    print(x)

i = 0  
while i < len(l1):  
    element = l1[i]  
    if element % 2 == 0:  
        print('It is an even number')       # Print if the number is even.  
    else:  
        print('It is an odd number')        # Print if the number is odd.  
    i += 1  