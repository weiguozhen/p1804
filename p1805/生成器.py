def hanshu(a,b):
    while a<b:
        yield a
        a=a+1
a=hanshu(1,5)
next(a)
for i in a:
    print(i)
