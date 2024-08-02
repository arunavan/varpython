#blue print
#oops

class Person: # template, declaration
    def disp():
        print('person details')
    def show():
        print('another fucntion')
#object
p=Person  #instance of class
p1=Person  #instance of class
p2=Person
p.disp()
p.show()
p1.show()
p2.show()
p2.disp()
p1.disp()





# name, age
# self memberor variable of current class 
# constructor


#encapsulation  - binding data and function
# in object
class Person:
   # constructor
   def __init__(self,name,age,email):
       self.name=name
       self.age=age
       self.email=email
   def show(self):
        print(self.name, self.age)
   def showDetails(self):
       print(self.name,self.age,self.email)
   def addage(self,x):
       print(self.name)
       print(self.age+x)

p=Person('Ram',30,'ram@gmail.com')
p.show()
p.showDetails()
p.addage(7)


class Student:
    def __init__(self):
        self.id=100
        self.name='python developer'
        self.email='py@gmail.com'
    def __init__(self,id,name,email):     # constructor
        self.id=id
        self.name=name
        self.email=email
    def printData(self):   #BL some logic
        print(self.id,self.name,self.email)
s4=Student
s4.printData()
s1=Student(101,'ram','ram@gmail.com')
s2=Student(102,'raj','raj@gmail.com')
s3=Student(103,'kiran','kiran@gmail.com')
print(id(s1) ,id(s2),id(s3))
s1.printData()
s2.printData()
s3.printData()




