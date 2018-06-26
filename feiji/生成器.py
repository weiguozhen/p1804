'''
def hanshu(a,b):
    while a<b:
        yield a
        a=a+1
a=hanshu(1,4)
for i in a:
    print(i)
from inspect import isgeneratorfunction
print(isgeneratorfunction(hanshu))

'''
l=(i for i in range(1,5))
from collections import Iterable
print(isinstance(l,Iterable))
