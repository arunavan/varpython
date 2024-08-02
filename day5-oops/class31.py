
#classmethods 

class Employee:
   empCount = 0
   def __init__(self, name, age):
      self.__name = name
      self.__age = age
      Employee.empCount += 1
   def showcount(self):
      print (self.empCount)
      
   

e1 = Employee("Bhavana", 24)
e2 = Employee("Rajesh", 26)
#e3 = Employee("John", 27)
#e4=Employee('ramesh',40)

e1.showcount()
#e4.showcount()


# @classmethod

class Cloth:
   # Class attribute
   price = 4000
   def __init__(self,qty,discount):  #instance variable
     self.qty=qty
     self.discount=discount

   @classmethod
   def showPrice(cls):
      return cls.price

# Accessing class attribute
print(Cloth.showPrice())  
c=Cloth()
print(c.showPrice())
c1=Cloth()
print(c1.showPrice())