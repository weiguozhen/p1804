def fib(times):
    n=0
    a,b = 0,1
    while n<times:
        yield(b)
        a,b=b,a+b
        n+=1
    return "done"
f = fib(10)
#print(next(f))
for i in f:
    print(i,end="\n")
