list=[]
fiblist=[]
for i in range(100):
    list.append(i)
list=iter(list)
#print(next(a))
n=0
a,b=0,1
while n<100:
    fiblist.append(b)
    a,b=b,a+b
    n+=1
for i in list:
    if i in fiblist:
        print(i)
