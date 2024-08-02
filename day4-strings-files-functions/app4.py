str = "Hello"     
str1 = " world"    
print(str*3) # prints HelloHelloHello    
print(str+str1)# prints Hello world     
print(str[4]) # prints o                
print(str[2:4]); # prints ll                    
print('w' in str) # prints false as w is not present in str    
print('wo' not in str1) # prints false as wo is present in str1.     
print(r'C://python37') # prints C://python37 as it is written    
print("The string str : %s"%(str)) # prints The string str : Hello     

print('Hello \n World')  # line feed
# using triple quotes  
print('''''They said, "What's there?"''')  
# escaping single quotes  
print('They said, "What\'s going on?"')  
  
# escaping double quotes  
print("They said, \"What's going on?\"")  
print(r"C:\\Users\\DEVANSH SHARMA\\Python32")    # raw print