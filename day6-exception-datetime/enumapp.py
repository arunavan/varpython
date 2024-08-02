# importing enum 
from enum import Enum

class subjects(Enum):
   ENGLISH = 1
   MATHS = 2
   SCIENCE = 3
   SANSKRIT = 4

obj = subjects.MATHS
print (type(obj))
for s in subjects:
   print(s)

seasons = Enum("seasons", "SPRING SUMMER  MONSOON AUTUMN")
print(seasons.SPRING)
print(seasons)
