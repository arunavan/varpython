import array as a1


a=a1.array('i',[6,7,3,4,1,2,4,5,6,7])
print(a)

large=a[0]
small=a[0]
for i in range(1,len(a)):
    if(a[i]>large):
        large=a[i]

for i in range(1,len(a)):
    if(a[i]<small):
        small=a[i]
print(large)
print(small)