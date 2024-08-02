
list = [1,32,12,98,45,67,24,24,4,5,4,5,6,7,6,7,3,4,5]  
          
print(list[0])    
print(list[1])    
print(list[2])    
print(list[3])   
list.insert(3,67)
list.append(78)
print(list.sort())


for i in list:
    print(i)

# Slicing the elements    
print(list[0:6])    
# By default, the index value is 0 so its starts from the 0th element and go for index -1.    
print(list[:])    
print(list[2:5])    
print(list[1:6:2])    