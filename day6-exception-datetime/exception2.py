#custom exception

class DepositError(Exception):
   def __init__(self,msg="Minimum deposit is 1000,plea try again"):
      self.msg=msg
     #print(msg)

deposit=int(input('enter deposit'))


def check(deposit):
   print('deposit amount is ',deposit)
   if(deposit<1000):
      raise DepositError()
   


try:
   check(deposit)
except DepositError as e:
   print(f" {e.msg}")
print('deposit success')

class InvalidAgeError(Exception):
   def __init__(self, age, message="Age must be between 1 and 100"):
      self.age = age
      self.message = message
      super().__init__(self.message)

   def __str__(self):
     return f"{self.message}. Provided age: {self.age}"

def set_age(age):
   if age < 0  or age > 100:
      raise InvalidAgeError(age)
   print(f"Age is set to {age}")

try:
   set_age(89)
except InvalidAgeError as e:
   print(f"Invalid age: {e.age}. {e.message}")