Days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}    
print(Days)    
print(type(Days))    
print("looping through the set elements ... ")    

sub={'Monday','Tuesday'}

if (sub.issubset(Days)):
    print('true')
else:
    print('false')
for i in Days:    
    print(i)    