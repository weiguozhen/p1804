def wai(a,b):
    def nei(x):
        nonlocal a
        a+=1
        print("y=%d*%d+%d"%(a,x,b))
        y=a*x+b
        print(a)
        return y
    return nei
print(wai(2,3)(3))
w=wai(2,3)
#w(3)
