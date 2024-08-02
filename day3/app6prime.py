num = [34, 12, 54, 23, 75, 34, 11]    
  
def prime_number(number):  
    flag = 0  
    i = 2  
    while i <= number / 2:  
        if number % i == 0:  
            flag = 1  
            break  
        i = i + 1  
  
    if flag == 0:  
        print(f"{number} is a PRIME number")  
    else:  
        print(f"{number} is not a PRIME number")  
for i in num:  
    prime_number(i)  


for k in num:
    print(k)