import time;  
  
#prints the number of ticks spent since 12 AM, 1st January 1970  
  
print(time.time())  

print(time.localtime(time.time()))  

print(time.asctime(time.localtime(time.time())))  

import datetime;  
  
#returns the datetime object for the specified date  
  
print(datetime.datetime(2018,12,10))  

print(datetime.datetime.now()) 

print(datetime.datetime(2018,12,10,14,15,10))  

import calendar;  
cal = calendar.month(2024,10)  
#printing the calendar of December 2018  
print(cal)