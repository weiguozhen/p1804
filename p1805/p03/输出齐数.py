def fib(times):
    n=0
    a,b=0,1
    while n<times:
        yield(b)
        a,b=b,a+b
        n=n+1
s=fib(1000)
print(next(s))
for i in s:
    print(i)

#def hanshu1(c):
   # for i in range(1,101):
  #      if i%2 != 0:
 #           yield(i)
#x=hanshu1(100)
#for n in x:
   # print(n)
