name = 'TutorialsPoint'
marks = 50
result = True
def myfunction():
   a = 10
   b = 20 #local
   print(name)
   return a+b
def fun2():
   print(result)
   print(marks)
def fun3():
   print(name)

print (globals())
print(locals())
print(myfunction())
result=myfunction()
print(result)
fun2()
fun3()