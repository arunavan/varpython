def myfunction(a: int, b: int):   # without return type
   c = a+b
   return c
   
print (myfunction(10,20))
print (myfunction("Hello ", "Python"))


def myfunction1(a: int, b: int) -> int:  # with return type
   c = a+b
   return c
print(myfunction1(20,30))