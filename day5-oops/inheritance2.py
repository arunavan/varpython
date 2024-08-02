# parent class
class Universe: 
   def universeMethod(self):
      print ("I am in the Universe")

# child class
class Earth(Universe): 
   def earthMethod(self):
      print ("I am on Earth")
      
# another child class
class India(Earth): 
   def indianMethod(self):
      print ("I am in India")      

# creating instance 
person = India()
u=Universe()  

print(isinstance(u,Earth))
print(isinstance(person,India))
# method calls
person.universeMethod() 
person.earthMethod() 
person.indianMethod() 